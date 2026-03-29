"""
Centralized Logfire configuration — single source of truth.

Call configure_logfire() ONCE near process startup (api/app.py does this).
If no token is available, this becomes a complete no-op so the app runs
normally without a Logfire account.
"""

import os
import logging
from functools import lru_cache

_log = logging.getLogger(__name__)

_LOGFIRE_TOKEN = os.getenv("LOGFIRE_TOKEN", "").strip()


@lru_cache(maxsize=1)
def configure_logfire(service_name: str = "wargame-agent") -> None:
    """
    Configure Logfire and instrument HTTP + Pydantic AI.

    Idempotent: lru_cache ensures repeated calls in the same process are no-ops.
    Silently skipped when LOGFIRE_TOKEN env var is absent or empty.

    Instruments:
      - requests  (OpenRouterClient uses raw requests — this captures all LLM calls)
      - pydantic_ai  (if pydantic-ai is used anywhere)
    """
    if not _LOGFIRE_TOKEN:
        _log.debug("LOGFIRE_TOKEN not set — Logfire disabled.")
        return

    try:
        import logfire

        logfire.configure(
            token=_LOGFIRE_TOKEN,
            service_name=service_name,
            environment=os.getenv("ENV", "production"),
            # Console pretty-print when LOGFIRE_CONSOLE=true (local dev)
            console=os.getenv("LOGFIRE_CONSOLE", "false").lower() == "true",
            send_to_logfire=True,
        )

        # Instrument the raw `requests` library — this captures all OpenRouter calls
        # (spans will appear as HTTP client spans in the Logfire UI)
        try:
            logfire.instrument_requests()
            _log.debug("Logfire: requests instrumented.")
        except Exception as exc:
            _log.debug("Logfire: requests instrumentation skipped (%s).", exc)

        # Instrument pydantic-ai if available
        try:
            logfire.instrument_pydantic_ai()
            _log.debug("Logfire: pydantic-ai instrumented.")
        except Exception as exc:
            _log.debug("Logfire: pydantic-ai instrumentation skipped (%s).", exc)

        _log.info("Logfire configured — service='%s' | dashboard: https://logfire-us.pydantic.dev/mtech/wargame-agent", service_name)

    except Exception as exc:
        _log.warning("Logfire setup failed (%s) — continuing without observability.", exc)
