"""
Default scenario configuration for the War Game 2D.

This module provides a built-in scenario that can be used without 
uploading a JSON file. The configuration is easily modifiable.
"""

# =============================================================================
# CONFIGURATION (Easy to modify)
# =============================================================================

GRID_WIDTH = 20
GRID_HEIGHT = 13
MAX_TURNS = 50
SEED = 42

# Aircraft defaults
AIRCRAFT_RADAR_RANGE = 5.0
AIRCRAFT_MISSILES = 4
AIRCRAFT_MISSILE_RANGE = 4.0
AIRCRAFT_BASE_HIT_PROB = 0.8
AIRCRAFT_MIN_HIT_PROB = 0.1

# SAM defaults
SAM_RADAR_RANGE = 8.0
SAM_MISSILES = 6
SAM_MISSILE_RANGE = 6.0
SAM_BASE_HIT_PROB = 0.8
SAM_MIN_HIT_PROB = 0.1
SAM_COOLDOWN = 5

# AWACS defaults  
AWACS_RADAR_RANGE = 9.0


# =============================================================================
# DEFAULT SCENARIO (as dictionary for API consumption)
# =============================================================================

def get_default_scenario() -> dict:
    """
    Get the default scenario as a dictionary.
    
    Blue team (Human): 1 AWACS, 3 Fighters, 2 Decoys, 2 SAMs
    Red team (AI): 1 AWACS, 2 Fighters, 1 Decoy, 2 SAMs
    
    Entity positioning is tactical with proper spacing.
    
    Returns:
        Scenario dictionary ready for API consumption
    """
    return {
        "config": {
            "grid_width": GRID_WIDTH,
            "grid_height": GRID_HEIGHT,
            "max_stalemate_turns": 60,
            "max_no_move_turns": 100,
            "max_turns": MAX_TURNS,
            "check_missile_exhaustion": True,
            "seed": SEED,
        },
        "agents": [
            {"team": "BLUE", "type": "human", "name": "Human Player"},
            {"team": "RED", "type": "llm_agent_v2", "name": "AI Agent"},
        ],
        "entities": [
            # ========== BLUE TEAM (Human controlled) ==========
            # AWACS - Back line, protected position
            {
                "type": "AWACS",
                "id": 1,
                "team": "BLUE",
                "pos": [4, 6],  # Center-back for maximum radar coverage
                "kind": "awacs",
                "name": "Blue AWACS",
                "alive": True,
                "radar_range": AWACS_RADAR_RANGE,
                "can_move": True,
                "can_shoot": False,
            },
            # Fighter 1 - Front line, upper
            {
                "type": "Aircraft",
                "id": 2,
                "team": "BLUE",
                "pos": [7, 10],
                "kind": "aircraft",
                "name": "Blue Fighter 1",
                "alive": True,
                "radar_range": AIRCRAFT_RADAR_RANGE,
                "missiles": AIRCRAFT_MISSILES,
                "missile_max_range": AIRCRAFT_MISSILE_RANGE,
                "base_hit_prob": AIRCRAFT_BASE_HIT_PROB,
                "min_hit_prob": AIRCRAFT_MIN_HIT_PROB,
                "can_move": True,
                "can_shoot": True,
            },
            # Fighter 2 - Front line, middle
            {
                "type": "Aircraft",
                "id": 3,
                "team": "BLUE",
                "pos": [7, 6],
                "kind": "aircraft",
                "name": "Blue Fighter 2",
                "alive": True,
                "radar_range": AIRCRAFT_RADAR_RANGE,
                "missiles": AIRCRAFT_MISSILES,
                "missile_max_range": AIRCRAFT_MISSILE_RANGE,
                "base_hit_prob": AIRCRAFT_BASE_HIT_PROB,
                "min_hit_prob": AIRCRAFT_MIN_HIT_PROB,
                "can_move": True,
                "can_shoot": True,
            },
            # Fighter 3 - Front line, lower
            {
                "type": "Aircraft",
                "id": 4,
                "team": "BLUE",
                "pos": [7, 2],
                "kind": "aircraft",
                "name": "Blue Fighter 3",
                "alive": True,
                "radar_range": AIRCRAFT_RADAR_RANGE,
                "missiles": AIRCRAFT_MISSILES,
                "missile_max_range": AIRCRAFT_MISSILE_RANGE,
                "base_hit_prob": AIRCRAFT_BASE_HIT_PROB,
                "min_hit_prob": AIRCRAFT_MIN_HIT_PROB,
                "can_move": True,
                "can_shoot": True,
            },
            # Decoy 1 - Forward bait, upper
            {
                "type": "Decoy",
                "id": 5,
                "team": "BLUE",
                "pos": [6, 9],
                "kind": "decoy",
                "name": "Blue Decoy 1",
                "alive": True,
                "radar_range": 2.0,
                "can_move": True,
                "can_shoot": False,
            },
            # Decoy 2 - Forward bait, lower
            {
                "type": "Decoy",
                "id": 6,
                "team": "BLUE",
                "pos": [6, 3],
                "kind": "decoy",
                "name": "Blue Decoy 2",
                "alive": True,
                "radar_range": 2.0,
                "can_move": True,
                "can_shoot": False,
            },
            # SAM 1 - Ground defense, upper
            {
                "type": "SAM",
                "id": 7,
                "team": "BLUE",
                "pos": [4, 11],
                "kind": "sam",
                "name": "Blue SAM 1",
                "alive": True,
                "radar_range": SAM_RADAR_RANGE,
                "missiles": SAM_MISSILES,
                "missile_max_range": SAM_MISSILE_RANGE,
                "base_hit_prob": SAM_BASE_HIT_PROB,
                "min_hit_prob": SAM_MIN_HIT_PROB,
                "cooldown_steps": SAM_COOLDOWN,
                "on": True,
                "_cooldown": 0,
                "can_move": False,
                "can_shoot": True,
            },
            # SAM 2 - Ground defense, lower
            {
                "type": "SAM",
                "id": 8,
                "team": "BLUE",
                "pos": [4, 1],
                "kind": "sam",
                "name": "Blue SAM 2",
                "alive": True,
                "radar_range": SAM_RADAR_RANGE,
                "missiles": SAM_MISSILES,
                "missile_max_range": SAM_MISSILE_RANGE,
                "base_hit_prob": SAM_BASE_HIT_PROB,
                "min_hit_prob": SAM_MIN_HIT_PROB,
                "cooldown_steps": SAM_COOLDOWN,
                "on": True,
                "_cooldown": 0,
                "can_move": False,
                "can_shoot": True,
            },
            
            # ========== RED TEAM (AI controlled) ==========
            # AWACS - Back line
            {
                "type": "AWACS",
                "id": 9,
                "team": "RED",
                "pos": [15, 6],
                "kind": "awacs",
                "name": "Red AWACS",
                "alive": True,
                "radar_range": AWACS_RADAR_RANGE,
                "can_move": True,
                "can_shoot": False,
            },
            # Fighter 1 - Front line, upper
            {
                "type": "Aircraft",
                "id": 10,
                "team": "RED",
                "pos": [12, 9],
                "kind": "aircraft",
                "name": "Red Fighter 1",
                "alive": True,
                "radar_range": AIRCRAFT_RADAR_RANGE,
                "missiles": AIRCRAFT_MISSILES,
                "missile_max_range": AIRCRAFT_MISSILE_RANGE,
                "base_hit_prob": AIRCRAFT_BASE_HIT_PROB,
                "min_hit_prob": AIRCRAFT_MIN_HIT_PROB,
                "can_move": True,
                "can_shoot": True,
            },
            # Fighter 2 - Front line, lower
            {
                "type": "Aircraft",
                "id": 11,
                "team": "RED",
                "pos": [12, 3],
                "kind": "aircraft",
                "name": "Red Fighter 2",
                "alive": True,
                "radar_range": AIRCRAFT_RADAR_RANGE,
                "missiles": AIRCRAFT_MISSILES,
                "missile_max_range": AIRCRAFT_MISSILE_RANGE,
                "base_hit_prob": AIRCRAFT_BASE_HIT_PROB,
                "min_hit_prob": AIRCRAFT_MIN_HIT_PROB,
                "can_move": True,
                "can_shoot": True,
            },
            # Decoy
            {
                "type": "Decoy",
                "id": 12,
                "team": "RED",
                "pos": [13, 6],
                "kind": "decoy",
                "name": "Red Decoy",
                "alive": True,
                "radar_range": 2.0,
                "can_move": True,
                "can_shoot": False,
            },
            # SAM 1 - Ground defense, upper
            {
                "type": "SAM",
                "id": 13,
                "team": "RED",
                "pos": [15, 11],
                "kind": "sam",
                "name": "Red SAM 1",
                "alive": True,
                "radar_range": SAM_RADAR_RANGE,
                "missiles": SAM_MISSILES,
                "missile_max_range": SAM_MISSILE_RANGE,
                "base_hit_prob": SAM_BASE_HIT_PROB,
                "min_hit_prob": SAM_MIN_HIT_PROB,
                "cooldown_steps": SAM_COOLDOWN,
                "on": False,
                "_cooldown": 0,
                "can_move": False,
                "can_shoot": True,
            },
            # SAM 2 - Ground defense, lower
            {
                "type": "SAM",
                "id": 14,
                "team": "RED",
                "pos": [15, 1],
                "kind": "sam",
                "name": "Red SAM 2",
                "alive": True,
                "radar_range": SAM_RADAR_RANGE,
                "missiles": SAM_MISSILES,
                "missile_max_range": SAM_MISSILE_RANGE,
                "base_hit_prob": SAM_BASE_HIT_PROB,
                "min_hit_prob": SAM_MIN_HIT_PROB,
                "cooldown_steps": SAM_COOLDOWN,
                "on": False,
                "_cooldown": 0,
                "can_move": False,
                "can_shoot": True,
            },
        ],
    }
