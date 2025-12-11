ANALYST_OUTPUT = {
    # UNIT-LEVEL ANALYSIS (Foundation - analyze first, most detailed)
    "unit_insights": [
        {
            "unit_id": 10,
            "role": "SAM ambush position covering AWACS western approach",
            "key_considerations": [
                "In mutual weapon range with both enemies (2.8 distance, 40% hit chance)",
                "Only 4 missiles remaining",
                "Currently active and visible to enemies"
            ],
            "action_analysis": [
                {
                    "action": {"type": "SHOOT", "target": 2},
                    "implication": "Engage northern threat (40% hit), reveal position, enter 5-turn cooldown, use 1 of 4 missiles"
                },
                {
                    "action": {"type": "SHOOT", "target": 3},
                    "implication": "Engage southern threat (40% hit), reveal position, enter 5-turn cooldown, use 1 of 4 missiles"
                },
                {
                    "action": {"type": "TOGGLE", "on": False},
                    "implication": "Go stealth immediately, become invisible, lose current firing opportunity on both targets"
                },
                {
                    "action": {"type": "WAIT"},
                    "implication": "Remain active and targetable (31% enemy hit chance), maintain ambush readiness for next turn"
                }
            ]
        },
        {
            "unit_id": 9,
            "role": "Decoy screen forward of main force",
            "key_considerations": [
                "In enemy weapon range (distance 4 from enemy-2, 10% enemy hit chance)",
                "Likely target for enemy fire this turn",
                "No radar capability - relying on allies for detection"
            ],
            "action_analysis": [
                {
                    "action": {"type": "MOVE", "direction": "RIGHT", "destination": {"x": 19, "y": 8}},
                    "implication": "Retreat behind aircraft-7, escape enemy weapon range, maintain screening position"
                },
                {
                    "action": {"type": "MOVE", "direction": "DOWN", "destination": {"x": 18, "y": 7}},
                    "implication": "Fall back slightly, still exposed to enemy-2, closer to AWACS protection"
                },
                {
                    "action": {"type": "MOVE", "direction": "LEFT", "destination": {"x": 17, "y": 8}},
                    "implication": "Advance toward enemy, increase exposure risk, probe enemy response"
                },
                {
                    "action": {"type": "MOVE", "direction": "UP", "destination": {"x": 18, "y": 9}},
                    "implication": "BLOCKED - cell occupied by aircraft-7 (may move), collision risk"
                },
                {
                    "action": {"type": "WAIT"},
                    "implication": "Stay exposed in enemy weapon range, high risk of taking fire (10% hit chance)"
                }
            ]
        },
        {
            "unit_id": 7,
            "role": "Northern escort screening AWACS upper approach",
            "key_considerations": [
                "Just outside weapon range of enemy-2 (4.1 distance, need 0.1 closer)",
                "Full ammunition (7 missiles)",
                "Positioned behind decoy-9"
            ],
            "action_analysis": [
                {
                    "action": {"type": "MOVE", "direction": "LEFT", "destination": {"x": 17, "y": 9}},
                    "implication": "Close to weapon range of enemy-2, enable engagement next turn, move forward of current line"
                },
                {
                    "action": {"type": "MOVE", "direction": "UP", "destination": {"x": 18, "y": 10}},
                    "implication": "Move away from enemy, maintain distance outside range, edge of grid approach"
                },
                {
                    "action": {"type": "MOVE", "direction": "RIGHT", "destination": {"x": 19, "y": 9}},
                    "implication": "Fall back to AWACS column, maintain safe distance from enemy"
                },
                {
                    "action": {"type": "MOVE", "direction": "DOWN", "destination": {"x": 18, "y": 8}},
                    "implication": "BLOCKED - cell occupied by decoy-9 (may move), collision risk"
                },
                {
                    "action": {"type": "WAIT"},
                    "implication": "Maintain current position outside engagement range, no tactical change"
                }
            ]
        },
        {
            "unit_id": 8,
            "role": "Southern escort screening AWACS lower approach",
            "key_considerations": [
                "Just outside weapon range of enemy-3 (4.1 distance, need 0.1 closer)",
                "Full ammunition (7 missiles)",
                "Mirror position to aircraft-7 on opposite flank"
            ],
            "action_analysis": [
                {
                    "action": {"type": "MOVE", "direction": "LEFT", "destination": {"x": 17, "y": 3}},
                    "implication": "Close to weapon range of enemy-3, enable engagement next turn, move forward of current line"
                },
                {
                    "action": {"type": "MOVE", "direction": "UP", "destination": {"x": 18, "y": 4}},
                    "implication": "Move toward center, slightly closer to enemy but still outside range"
                },
                {
                    "action": {"type": "MOVE", "direction": "DOWN", "destination": {"x": 18, "y": 2}},
                    "implication": "Move away from enemy, maintain distance, edge of grid approach"
                },
                {
                    "action": {"type": "MOVE", "direction": "RIGHT", "destination": {"x": 19, "y": 3}},
                    "implication": "Fall back to AWACS column, maintain safe distance from enemy"
                },
                {
                    "action": {"type": "WAIT"},
                    "implication": "Maintain current position outside engagement range, no tactical change"
                }
            ]
        },
        {
            "unit_id": 6,
            "role": "AWACS - mission critical asset at rear",
            "key_considerations": [
                "At right edge of grid (x=19), limited maneuver space",
                "Both enemy aircraft at safe distance (5.4 cells away)",
                "Protected by layered screen of units"
            ],
            "action_analysis": [
                {
                    "action": {"type": "MOVE", "direction": "LEFT", "destination": {"x": 18, "y": 6}},
                    "implication": "Move away from edge, gain maneuver flexibility, closer to friendly units"
                },
                {
                    "action": {"type": "MOVE", "direction": "UP", "destination": {"x": 19, "y": 7}},
                    "implication": "Shift north along edge, maintain distance from enemies"
                },
                {
                    "action": {"type": "MOVE", "direction": "DOWN", "destination": {"x": 19, "y": 5}},
                    "implication": "Shift south along edge, maintain distance from enemies"
                },
                {
                    "action": {"type": "WAIT"},
                    "implication": "Hold current position at edge, no immediate threats"
                }
            ]
        }
    ],

    # HIGH-LEVEL SYNTHESIS (Derived from unit analysis)
    "critical_alerts": [
        "HIGH: Decoy-9 in enemy weapon range (10% hit chance) at distance 4 from enemy-2 [units: 9]",
        "HIGH: SAM-10 exposed and in mutual weapon range with both enemy aircraft (31% enemy hit chance) [units: 10]",
        "MEDIUM: AWACS-6 limited to 3 escape routes due to right edge positioning [units: 6]",
        "MEDIUM: Both aircraft just outside weapon range (0.1 cells) - cannot engage without closing [units: 7, 8]"
    ],

    "opportunities": [
        "HIGH: SAM-10 has 40% hit chance on both enemy aircraft at range 2.8 - can shoot either target [units: 10]",
        "MEDIUM: Both aircraft can close 0.1 cells to enable engagement next turn [units: 7, 8]",
        "LOW: Decoy-9 can retreat to safety behind aircraft-7, forcing enemy to advance [units: 9]"
    ],

    "constraints": [
        "HIGH - INFORMATION: Enemy AWACS location unknown, no winning strike available yet [affects: TEAM]",
        "MEDIUM - RESOURCE: SAM-10 limited ammunition (4 missiles remaining) [affects: 10]",
        "MEDIUM - POSITIONING: Team clustered on right side (formation spread 2.2), limited tactical flexibility [affects: TEAM]",
        "LOW - POSITIONING: Potential movement conflicts between aircraft-7 and decoy-9 at (18,8) [affects: 7, 9]"
    ],

    "spatial_status": "DEFENSIVE posture - team at right edge (x=18-19) facing enemy at center-left (x=14). Formation CLUSTERED within 3-cell radius providing mutual support but limited maneuver space. Distance control CONTESTED - at edge of engagement range (4.0-4.1 cells), enemy can force engagement by advancing 0.1-1.4 cells.",

    "situation_summary": "Mid-game defensive standoff. Enemy probing with 2 aircraft at center-left, our forces clustered at right edge. SAM has clear shots but exposed. AWACS safe but edge-limited. Enemy AWACS location unknown."
}