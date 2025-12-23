# TACTICAL_GUIDE = f"""
# ### TACTICAL PRINCIPLES & CONSIDERATIONS FOR 2D COMBAT GRID GAME
# **Purpose:** This guide presents core tactical concepts and strategic patterns observed in 2D combat grid scenarios. It is NOT a prescriptive rulebook—treat it as a menu of ideas to inform your own tactical decisions based on specific battlefield conditions.
#
#
# ### VICTORY CONDITION
# Destroy enemy AWACS while protecting yours. Time costs resources - aggressive progress required.
#
# ### CORE PRINCIPLES
#
# #### 1. AWACS PROTECTION (TOP PRIORITY)
# - Keep AWACS at maximum rear distance with clear escape routes
# - Maintain 2+ unblocked retreat paths at all times
# - Position multiple defensive layers between AWACS and threats
# - AWACS is valuable but, as long as it is in the safe distance, it can be used for radar spotting to support offensive actions.
#
# #### 2. INFORMATION WARFARE
# - Radar detection is SHARED across team (if one unit sees an enemy, all units can target it)
# - Use decoys to probe unknown areas and reveal enemy SAM positions
# - Avoid clustering units (limits tactical flexibility and creates single points of failure)
#
# #### 3. TARGET PRIORITY
# 1. Enemy AWACS (if accessible - game-winning)
# 2. Enemy aircraft threatening your AWACS
# 3. Enemy SAMs blocking your advance path
# 4. Enemy decoys (LOWEST - avoid wasting ammunition)
#
# #### 4. DISTANCE CONTROL & AMMUNITION ECONOMY
# - **Control engagement distance:** Stay outside enemy weapon range when not attacking; close distance to engage
# - Fire at closer range for higher hit probability (distance determines hit chance)
# - Coordinate multi-unit strikes on tough targets (avoid overkill)
# - Don't waste missiles on suspected decoys
# - Each shot counts - make them matter
#
# #### 5. SAM TACTICS
# - **Stealth Positioning:** Keep SAMs OFF until optimal moment and bait enemy into range.
# - **Ambush Pattern:** Toggle ON → Shoot → Toggle OFF immediately
# - **Cooldown Safety:** Stay stealthed during ~5-turn reload period
# - **Surprise > Sustained Fire:** One good ambush shot beats continuous exposure
# - **IMPORTANT:** SAM is a stationary but important asset, baiting enemy into range and ambushing them is a good use of SAMs.
#
# #### 6. DECOY OPERATIONS
# - Mix decoys with real aircraft to create targeting uncertainty
# - Use decoys to bait enemy fire away from valuable units
# - Send decoys ahead to absorb fire and clear paths
# - Still don't lose decoy for nothing, try to trade decoy for an enemy entity if possible
# - Enemy can't distinguish decoys - exploit this
#
# #### 7. FORMATION CONCEPTS
# **Defense:** Layered screen with aircraft forward, AWACS back, hidden SAMs for surprise, bait enemy into kill zones.
# **Offense:** Decoy(s) in front, aircraft follow 2-3 cells back to exploit cleared paths, AWACS behind for radar support.
#
# #### 8. TEMPO & AGGRESSION
# - Static defense loses to operational costs over time, still sometimes best offense is a good defense
# - Apply pressure to force enemy into reactive positions when you have advantage
# - Trading 1 aircraft for enemy AWACS = victory
# - Once enemy weakened, commit to AWACS strike
#
# #### 9. COMMON MISTAKES TO AVOID
# - Overlapping radar coverage (shared detection makes this wasteful)
# - Shooting at maximum range (low hit % wastes precious ammo)
# - Single escape route for AWACS (death trap)
# - Keeping SAMs constantly ON (makes them easy targets)
# - Engaging obvious decoys (ammo waste)
# - All units in one corridor (easily blocked/countered)
#
# #### 10. WINNING PATTERNS
# - **SAM Ambush:** Hide SAM → Bait enemy into range → Toggle ON + Shoot → Toggle OFF
# - **Decoy Screen:** Decoys lead, aircraft follow 2-3 cells back, exploit cleared path
# - **Pincer Movement:** Attack from multiple directions to trap enemy AWACS
# - **Breakthrough Timing:** Thin enemy defenses first, then commit to AWACS kill
#
# ### DECISION FRAMEWORK EACH TURN
# 1. Is my AWACS safe? (If no - prioritize defense immediately)
# 2. Can I damage/kill enemy AWACS? (If yes - consider aggressive strike)
# 3. What new enemy positions revealed? (Update threat assessment)
# 4. Which units can contribute to objective? (Advance those, position others)
# 5. Are SAMs optimally positioned for ambush? (Toggle timing critical)
# 6. Is ammunition being used efficiently? (High-value targets only)
#
# ### REMEMBER
# - Every turn costs resources - make progress toward enemy AWACS
# - Control distance: stay safe when repositioning, close in when engaging
# - Decoys are disposable intelligence assets - use them
# - SAMs are ambush weapons, not frontline fighters
# - Protect AWACS > Everything else"""

TACTICAL_GUIDE = """
### STRATEGIC IDEAS (NOT SET IN STONE)
- **Decoys:** Lead and scout; they are relatively dispensable (but for a reason), enemy will think they are aircrafts, you can use them to scout, protect other entities, or to make the enemy forces follow (keeping a safe distance if possible) it to the ambush.

- **Aircraft:** 
    - Use for discovery and/or to attack in coordinated groups; fire simultaneously for higher hit odds.
    - Firing from distance makes sense to get safe shots despite low probabilities, but if you limited missiles taking a closer shot despite the risk could make sense.
    - Fighting around your ON SAM will provide aircrafts a big advantage.
    - Shooting behind your decoy or sam also makes sense to both keep you safe and have a hit chance. 

- **SAMs:**
  - Use for defense and baiting
  - Keep it OFF to lure enemies or hide cooldowns
  - Turn ON when enemy is close for surprise attacks
  - Fights around (in the shoot distance) your SAM when it's ON, provides your aircrafts a big advantage.
  - For the enemy SAMs, it makes sense to turn around them if possible or accept a long shot from it (possibly by using a decoy), then suddenly getting closer to it and attack.
  
- **AWACS:**
  - Critical asset—protect at all costs
  - Move away from any threat (>=4 is safe by keeping this distance to the closest armed enemy you can use the radar capabilities freely)
  
- **Movement:**
  - Can use map edges for stealth
  - When faced enemies you can fight or flee depending on your (positioning, entitiy numbers, arming, etc...) 
  - Close distance for higher hit probability, but it is double-edged situation
  
- **General Suggestions to Consider***
    - It is a 2D game with limitations use them for your advantage.
    - At each turn, every entity can do only one thing. E.g. can't move and shoot at the same turn.
    - You can play defensive and use your SAM hidden for ambush to eliminate some of the enemy forces and then attack.
    - You can play offensive by directly attacking and using element of surprise.
    - You can walk on the shadow (edges) and set a surprise assasination to the awacs.
    - There are many options considering the game rules and entity capabilities, it's up to you.
"""