"""
Centralized Logfire configuration.

Call configure_logfire() once near process startup to set a consistent
service name and enable Pydantic AI instrumentation.
"""

from functools import lru_cache

import logfire


@lru_cache(maxsize=1)
def configure_logfire(service_name: str = "wargame2d") -> None:
    """
    Configure Logfire and instrument Pydantic AI.

    Idempotent: repeated calls in the same process no-op after the first.
    """
    logfire.configure(service_name=service_name)
    logfire.instrument_pydantic_ai()
