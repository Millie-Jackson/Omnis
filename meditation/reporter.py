# meditation/reporter.py


"""
Meditation Report Generator

Creates a structured diagnostic report based on memory and goal analysis.
This can be used both by the agent for planning and by human overseers
for interpretability or debugging.
"""


import logging


logger = logging.getLogger(__name__)


def generate_report(memory_findings, goal_findings):
    """
    Generate a self-reflection report.

    Args:
        memory_findings (dict)
        goal_findings (dict)

    Returns:
        dict: Reflection report
    """

    logger.debug("Generating report")

    summary = generate_summary(memory_findings, goal_findings)

    return {
        "memory": memory_findings,
        "goals": goal_findings,
        "summary": summary
    }

def generate_summary(memory_findings, goal_findings):
    """
    Generate a natural language summary of meditation results.

    Args:
        memory_findings (dict)
        goal_findings (dict)

    Returns:
        str: A short descriptive paragraph.
    """

    parts = []

    # Step 1: Memory issues
    if memory_findings.get("failure_loop_detected"):
        parts.append(
            f"Omnis is experiencing repeated failure in action '{memory_findings.get('most_common_action', '?')}'."   
        )
    else:
        parts.append("No repeated failure loops detected")

    # Step 2: Goal issues
    if goal_findings["duplicates"]:
        dup_count = len(goal_findings["duplicates"])
        parts.append(f"Detected {dup_count} duplicate goal(s).")

    if goal_findings["priority_conflicts"]:
        parts.append(f"Priority misalingment in {len(goal_findings['priority_conflicts'])} goal(s).")

    if goal_findings["conflicts"]:
        conflicts = goal_findings["conflicts"]
        parts.append(f"Found conflicting goals: {', '.join(f'{a} vs {b}' for a, b in conflicts)}.")
    else:
        parts.append("No logican contradiction between goals.")

    # Step 3: Final tone
    if goal_findings["drift_score"] >= 0.8:
        parts.append("Severe goal drift detected.")
    elif goal_findings["drift_score"] >= 0.5:
        parts.append("Moderate signs of goal misalignment.")
    else:
        parts.append("Goal system appears mostry alighned.")
    
    return " ".join(parts)