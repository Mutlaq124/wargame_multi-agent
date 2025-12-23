TACTICAL_GUIDE = f"""
### TACTICAL PRINCIPLES & CONSIDERATIONS FOR 2D COMBAT GRID GAME
**Purpose:** This guide presents core tactical concepts and strategic patterns observed in 2D combat grid scenarios. 
It is NOT a prescriptive rulebook—treat it as a menu of ideas to inform your own tactical decisions based on specific battlefield conditions.


### VICTORY CONDITION
Destroy enemy AWACS while protecting yours.

### CORE PRINCIPLES

#### 1. AWACS PROTECTION (TOP PRIORITY)
- Keep AWACS safe (>= a threshold value is mainly enough) with clear escape routes
- Maintain unblocked retreat paths at all times
- As long as AWACS is safe (distance + open routes) it can move freely to provide vision for the team.
- AWACS is also useful for discovery/spotting enemy units for offensive moves as long as it is safe.

#### 2. TARGET PRIORITY
1. Enemy AWACS (if accessible - game-winning)
2. Enemy aircraft threatening your AWACS
3. Enemy SAMs blocking your advance path
4. Enemy decoys (LOWEST - avoid wasting ammunition)

#### 3. DISTANCE CONTROL & AMMUNITION ECONOMY
- **Control engagement distance:** Stay outside enemy weapon range when not attacking; close distance to engage
- Fire at closer range for higher hit probability (distance determines hit chance)
- Coordinate multi-unit strikes when possible
- Each shot counts especially when we have low ammo left, take closer shots when ammo is limited.

#### 4. SAM TACTICS
- **Stealth Positioning:** Keep SAMs OFF until optimal moment and bait enemy into the center of kill zone.
- **Ambush Pattern:** Toggle ON → Shoot → Toggle OFF immediately
- **Cooldown Safety:** Stay stealth during ~5-turn reload period, unless you want enemy to attack on SAM (to protect more valuable units)
- **Surprise > Sustained Fire:** One good ambush shot beats continuous exposure
- **IMPORTANT:** SAM is a stationary but important asset, baiting enemy into the center of the kill zone and ambushing them is a very good use of SAMs.

#### 5. DECOY OPERATIONS
- Decoys are expendable, you can use them relatively aggressively but still don't lose decoy for nothing.
- When engagement is inevitable, use decoys to absorb enemy fire instead of valuable aircraft. To do that simply position them enemy units closer than your aircrafts.
- Only waste them if there is a trade for a valuable enemy entity if possible
- You can use decoys to scout ahead, bait enemy, or clear paths for aircraft.
- Enemy can't distinguish decoys from aircraft.

#### 6. WINNING PATTERNS
- **SAM Ambush:** Hide SAM → Scout first, then run back make the enemy chase you, e.g. bait enemy into kill zone → Toggle ON + Shoot → Toggle OFF
- **Hit-and-Run:** Keep your distance, only engage when you have number advantage or high hit probability, then run back to to find another opportunity
- **Decoy Screen:** Decoys lead, aircraft follow 2-3 cells back, exploit cleared path
- **Pincer Movement:** Attack from multiple directions to trap enemy AWACS
- **Breakthrough Timing:** Thin enemy defenses first, then commit to AWACS kill

### REMEMBER
- Control distance: It is critical for both offense and defense as long as you keep your distance you can play more freely.
- Decoys are disposable intelligence assets - use them
- SAMs are ambush weapons, not frontline fighters
- Protect AWACS > Everything else"""


# ### DECISION FRAMEWORK EACH TURN
# 1. Is my AWACS safe? (If no - prioritize defense immediately)
# 2. Can I damage/kill enemy AWACS? (If yes - consider aggressive strike)
# 3. What new enemy positions revealed? (Update threat assessment)
# 4. Which units can contribute to objective? (Advance those, position others)
# 5. Are SAMs optimally positioned for ambush? (Toggle timing critical)
# 6. Is ammunition being used efficiently? (High-value targets only)
# TACTICAL_GUIDE = """
# ### STRATEGIC IDEAS (NOT SET IN STONE)
# - **Decoys:** Lead and scout; they are relatively dispensable (but for a reason), enemy will think they are aircrafts, you can use them to scout, protect other entities, or to make the enemy forces follow (keeping a safe distance if possible) it to the ambush.
#
# - **Aircraft:**
#     - Use for discovery and/or to attack in coordinated groups; fire simultaneously for higher hit odds.
#     - Firing from distance makes sense to get safe shots despite low probabilities, but if you limited missiles taking a closer shot despite the risk could make sense.
#     - Fighting around your ON SAM will provide aircrafts a big advantage.
#     - Shooting behind your decoy or sam also makes sense to both keep you safe and have a hit chance.
#
# - **SAMs:**
#   - Use for defense and baiting
#   - Keep it OFF to lure enemies or hide cooldowns
#   - Turn ON when enemy is close for surprise attacks
#   - Fights around (in the shoot distance) your SAM when it's ON, provides your aircrafts a big advantage.
#   - For the enemy SAMs, it makes sense to turn around them if possible or accept a long shot from it (possibly by using a decoy), then suddenly getting closer to it and attack.
#
# - **AWACS:**
#   - Critical asset—protect at all costs
#   - Move away from any threat (>=4 is safe by keeping this distance to the closest armed enemy you can use the radar capabilities freely)
#
# - **Movement:**
#   - Can use map edges for stealth
#   - When faced enemies you can fight or flee depending on your (positioning, entitiy numbers, arming, etc...)
#   - Close distance for higher hit probability, but it is double-edged situation
#
# - **General Suggestions to Consider***
#     - It is a 2D game with limitations use them for your advantage.
#     - At each turn, every entity can do only one thing. E.g. can't move and shoot at the same turn.
#     - You can play defensive and use your SAM hidden for ambush to eliminate some of the enemy forces and then attack.
#     - You can play offensive by directly attacking and using element of surprise.
#     - You can walk on the shadow (edges) and set a surprise assasination to the awacs.
#     - There are many options considering the game rules and entity capabilities, it's up to you.
# """