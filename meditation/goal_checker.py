# meditation/goal_checker.py


"""
Goal Evaluation

Evaluates the agent’s current goals for:
- Duplicates
- Conflicts (e.g. mutually exclusive goals)
- Priority misalignment (low-priority goals blocking high-priority ones)
"""


import logging
from collections import Counter


logger = logging.getLogger(__name__)

# Step 1: Define basic hardcoded goal conflict (domain-specific)
CONFLICT_PAIRS = [
    ("collect_items", "destroy_items"),
    ("stay_hidden", "attract_attention"),
    ("explore_freely", "follow_scripted_path"),
]


def evaluate_goals(goals):
    """
    Evaluate goal coherence, including redundancy, conflicts, and drift.

    Args:
        goals (list of dict): Goals with 'id' and 'priority' keys.

    Returns:
        dict: Summary including duplicates, conflicts, drift, and priority errors.
    """

    logger.debug("Evaluating %d goals...", len(goals))

    goal_ids = [g["id"] for g in goals]
    goal_counts = Counter(goal_ids)

    # Step 2: Find duplicate goals
    duplicates = {g: c for g, c in goal_counts.items() if c > 1}

    # Step 3: Detect explicit goal conflicts
    active_goal_ids = set(goal_ids)
    conflicts = []
    for g1, g2 in CONFLICT_PAIRS:
        if g1 in active_goal_ids and g2 in active_goal_ids:
            conflicts.append((g1, g2)) 

    # Step 4: Check priority logic (low priority goal blocks high)
    priority_conflicts = []
    sorted_goals = sorted(goals, key=lambda g: g.get("priority", 0), reverse=True)
    seen_ids = set()
    for g in sorted_goals:
        if g["id"] in seen_ids:
            priority_conflicts.append(g["id"])
        seen_ids.add(g["id"])

    # Step 5: Calculate drift score
    drift_score = 0.0
    if duplicates:
        drift_score += 0.5
    if conflicts:
        drift_score += 0.5
    if priority_conflicts:
        drift_score += 0.2

    result = {
        "total_goals": len(goals),
        "duplicates": duplicates,
        "conflicts": conflicts,
        "priority_conflicts": priority_conflicts,
        "drift_score": round(drift_score, 2),
    }

    logger.debug("Goal evaluation result: %s", result)
    return result