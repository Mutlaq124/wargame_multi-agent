"""
LLM client wrappers - OpenRouter only.
"""

import os
import logging
from typing import Optional, Dict
import requests
import json
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class BaseLLMClient(ABC):
    """Base class for LLM clients."""
    
    def __init__(self, model: str, api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key
        if not self.api_key:
            raise ValueError(f"{self.__class__.__name__} API key required")
        logger.info(f"{self.__class__.__name__}: {self.model}")
    
    @abstractmethod
    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.5,
        max_tokens: int = 2500,
        response_format: Optional[Dict[str, str]] = None
    ) -> str:
        """Call LLM API (subclass implements)."""
        pass
    
    def _validate_json(self, content: str, response_format: Optional[Dict]) -> str:
        """Validate JSON response early."""
        if response_format and response_format.get("type") == "json_object":
            try:
                json.loads(content)
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON: {e}")
                raise
        return content


RETRYABLE_STATUS = {429, 502, 503, 504}


class OpenRouterClient(BaseLLMClient):
    """OpenRouter client with JSON mode support (auto-instrumented by Logfire).

    Tries `model` first; if it's unavailable/saturated, falls back to
    `fallback_model` (OpenRouter's auto-router across all free models) instead
    of failing the turn outright.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "google/gemma-4-26b-a4b-it:free",
        fallback_model: str = "openrouter/free",
    ):
        super().__init__(model, api_key or os.getenv("OPENROUTER_API_KEY"))
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.fallback_model = fallback_model

    def _post(self, model: str, payload: Dict) -> Dict:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            # "HTTP-Referer": "https://github.com/yourusername/wargame",  # Optional: For OpenRouter analytics
            # "X-Title": "WarGame Agent"  # Optional
        }
        response = requests.post(self.base_url, headers=headers, json={**payload, "model": model}, timeout=60)
        response.raise_for_status()
        return response.json()

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.5,
        max_tokens: int = 2500,
        response_format: Optional[Dict[str, str]] = None
    ) -> str:
        """Call OpenRouter API. On a saturated/down primary model, fall back to the auto-router."""
        payload = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        if response_format:
            payload["response_format"] = response_format

        models_to_try = [self.model]
        if self.fallback_model != self.model:
            models_to_try.append(self.fallback_model)

        last_error: Optional[Exception] = None
        for i, model in enumerate(models_to_try):
            try:
                data = self._post(model, payload)
                content = data["choices"][0]["message"]["content"]
                return self._validate_json(content, response_format)
            except requests.exceptions.HTTPError as e:
                last_error = e
                status = e.response.status_code
                is_last = i == len(models_to_try) - 1
                if status in RETRYABLE_STATUS and not is_last:
                    logger.warning(f"OpenRouter {status} on '{model}' - falling back to '{models_to_try[i + 1]}'")
                    continue
                if status == 429:
                    logger.error("OpenRouter rate limit hit - consider upgrading plan")
                logger.error(f"OpenRouter HTTP error: {e}")
                raise
            except Exception as e:
                logger.error(f"OpenRouter error: {e}")
                raise
        raise last_error
