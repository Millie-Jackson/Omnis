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
from meditation.config import CONFLICT_PAIRS


logger = logging.getLogger(__name__)


def compute_drift_score(current_goals, original_goals):
    """
    Calculates how much the agent has drifted from the original goal set.

    Drift = (# of unexpected goals) / (total current goals)
    """

    unexpected = [g for g in current_goals if g not in original_goals]
    if not current_goals:
        return 0.0 # No goals = no drift
    
    return round(len(unexpected) / len(current_goals), 2)

def evaluate_goals(goals_state):
    """
    Evaluates goals for duplicates, conflicts, and drift.

    Args:
        goal_state (dict): Dictionary with keys:
            - "current": list of current goal strings
            - "original": list of original goal strings
            - "priorities": dict of goal -> priority value (optional)

    Returns:
        dict: {
            total_goals,
            duplicates,
            conflicts,
            priority_conflicts,
            drift_score
        }
    """

    current_goals = goals_state.get("current", [])
    original_goals = goals_state.get("original", [])
    priorities = goals_state.get("priorities", {})

    # Step 1: Find duplicate goals
    seen = set()
    duplicates = {}
    for g in current_goals:
        if g in seen:
            duplicates[g] = duplicates.get(g, 1) + 1
        else:
            seen.add(g)

    # Step 2: Conflict detection (placeholder)
    conflicts = [] # Logic to be implimented later

    # Step 3: Check priority logic (low priority goal blocks high)
    priority_conflicts = []
    if priorities:
        sorted_goals = sorted(priorities.items(), key=lambda x: x[1], reverse=True)
        if sorted_goals and sorted_goals[0][1] == sorted_goals[-1][1]:
            priority_conflicts = [g for g, _ in sorted_goals]

    # Step 4: Drift scoring
    drift_score = compute_drift_score(current_goals, original_goals)

    result = {
        "total_goals": len(current_goals),
        "duplicates": duplicates,
        "conflicts": conflicts,
        "priority_conflicts": priority_conflicts,
        "drift_score": drift_score,
    }

    logger.debug("Goal evaluation result: %s", result)
    return result
