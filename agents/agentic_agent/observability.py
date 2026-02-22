"""Centralized Logfire observability configuration."""
import os
from typing import Optional
from contextlib import contextmanager
import logfire

# Configure Logfire once
logfire.configure(
    token=os.getenv("LOGFIRE_TOKEN"),
    environment=os.getenv("ENV", "production"),
    console=os.getenv("LOGFIRE_CONSOLE", "false").lower() == "true"
)

@contextmanager
def trace_strategic_planning():
    """Trace strategic planning phase."""
    with logfire.span("strategic_planning"):
        yield

@contextmanager
def trace_tactical_execution(role: str):
    """Trace tactical execution per role."""
    with logfire.span(f"tactical_{role.lower()}"):
        yield

@contextmanager
def trace_role_execution(role: str):
    """Trace single role execution (duration auto-captured by Logfire)."""
    with logfire.span(f"role_{role.lower()}", role=role):
        yield

@contextmanager
def trace_fallback(reason: str):
    """Trace fallback triggers."""
    with logfire.span("fallback", reason=reason):
        logfire.error("fallback_triggered", reason=reason, alert=True)
        yield
