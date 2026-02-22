"""
Centralized Logfire configuration — gracefully disabled when LOGFIRE_TOKEN is not set.

Call configure_logfire() once near process startup.
If no token is available, this becomes a complete no-op so the app
runs normally on Render / any environment without a Logfire account.
"""

import os
import logging
from functools import lru_cache

_log = logging.getLogger(__name__)

_LOGFIRE_TOKEN = os.getenv("LOGFIRE_TOKEN", "").strip()


@lru_cache(maxsize=1)
def configure_logfire(service_name: str = "wargame2d") -> None:
    """
    Configure Logfire and instrument Pydantic AI.

    Idempotent: repeated calls in the same process no-op after the first.
    Silently skipped when LOGFIRE_TOKEN env var is absent or empty.
    """
    if not _LOGFIRE_TOKEN:
        _log.debug("LOGFIRE_TOKEN not set — Logfire disabled.")
        return

    try:
        import logfire
        logfire.configure(
            token=_LOGFIRE_TOKEN,
            service_name=service_name,
            send_to_logfire=True,
        )
        logfire.instrument_pydantic_ai()
        _log.info("Logfire configured for service '%s'.", service_name)
    except Exception as exc:
        _log.warning("Logfire setup failed (%s) — continuing without observability.", exc)
