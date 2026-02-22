"""HTTP API entrypoint for driving the game from a web UI."""

from pathlib import Path
from typing import List, Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from env.scenario import Scenario
from env.core.actions import Action
from runtime.runner import GameRunner
from infra.paths import UI_ENTRYPOINT
from runtime.logfire_config import configure_logfire
from scenarios import get_default_scenario

# Configure observability before app/agent imports are used.
configure_logfire()

app = FastAPI()
runner: GameRunner | None = None


# Allow the browser-based control panel (served from file:// or other origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class StartRequest(BaseModel):
    scenario: dict
    world: dict | None = None

class StepRequest(BaseModel):
    injections: dict | None = None


@app.get("/default-scenario")
def default_scenario():
    """Return the built-in default scenario for human vs agent gameplay."""
    return get_default_scenario()


@app.post("/start")
def start(request: StartRequest):
    global runner
    scenario = Scenario.from_dict(request.scenario)
    runner = GameRunner(scenario, world=request.world)
    return {"success": True}


@app.post("/step")
def step(request: StepRequest):
    if runner is None:
        raise HTTPException(400, "No active game")
    try:
        result = runner.step(request.injections)
        return result.to_dict()
    except RuntimeError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.get("/current-world")
def current_world():
    """Return the current world state without stepping. Used for immediate UI feedback."""
    if runner is None:
        raise HTTPException(400, "No active game")
    frame = runner.get_current_frame()
    result = frame.to_dict()

    # Include allowed actions for all alive entities (for smart action dropdowns)
    world = runner.state["world"]
    allowed_map = {}
    for entity in world.get_all_entities():
        if not entity.alive:
            continue
        actions = entity.get_allowed_actions(world)
        allowed_map[entity.id] = [
            {**a.to_dict(), "label": str(a)} for a in actions
        ]
    result["allowed_actions"] = allowed_map

    return result


@app.get("/allowed-actions/{entity_id}")
def get_allowed_actions(entity_id: int) -> Dict[str, Any]:
    """
    Get the allowed actions for a specific entity.
    
    Returns the entity info and a list of valid actions it can perform.
    """
    if runner is None:
        raise HTTPException(400, "No active game")
    
    world = runner.state["world"]
    entity = world.get_entity(entity_id)
    
    if entity is None:
        raise HTTPException(404, f"Entity {entity_id} not found")
    
    if not entity.alive:
        return {
            "entity_id": entity_id,
            "entity_kind": entity.kind.value,
            "entity_team": entity.team.name,
            "alive": False,
            "actions": []
        }
    
    # Get allowed actions from the entity
    allowed_actions = entity.get_allowed_actions(world)
    
    # Convert to serializable format
    actions_list = []
    for action in allowed_actions:
        action_dict = action.to_dict()
        action_dict["label"] = str(action)  # Human-readable label
        actions_list.append(action_dict)
    
    return {
        "entity_id": entity_id,
        "entity_kind": entity.kind.value,
        "entity_team": entity.team.name,
        "entity_name": entity.name,
        "alive": True,
        "position": list(entity.pos),
        "actions": actions_list,
        # Add entity-specific info
        "missiles": getattr(entity, "missiles", None),
        "radar_on": getattr(entity, "on", None),
        "cooldown_remaining": getattr(entity, "_cooldown", None),
    }


@app.get("/status")
def status():
    if runner is None:
        return {"active": False}
    return {"active": True, "turn": runner.turn, "step": runner.step_count, "done": runner.done}


@app.get("/", include_in_schema=False)
def serve_ui():
    """Serve the bundled control panel so the app runs from a single origin."""
    if not UI_ENTRYPOINT.exists():
        raise HTTPException(500, "UI entrypoint not found")
    return FileResponse(
        UI_ENTRYPOINT,
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        }
    )

