# meditation/memory_scanner.py


"""
Memory Scanner

Analyzes the agent's memory buffer to detect repeated failures,
redundant actions, or inconsistent patterns.

This helps identify confusion, loops, or stagnation.
"""


import logging
from collections import Counter


logger = logging.getLogger(__name__)


def scan_memory(memory):
    """
    Scan the agent's memory for patterns that suggest confusion or inconsistency.

    Args:
        memory (list of dict): Agent's memory of past steps.

    Returns:
        dict: Findings, including:
              - number of repeated failed actions
              - frequency of recent actions
              - possible confusion indicators
    """
        
    logger.debug("Scanning memory with %d entries", len(memory))
    
    repeated_failures = 0
    action_counter = Counter()
    failture_loop = False

    for entry in memory:
        action = entry.get("action")
        result = entry.get("result")
        action_counter[action] += 1
        if result == "fail":
            repeated_failures += 1

    # Detect if the most common action failed repeatedly
    most_common_action, count = action_counter.most_common(1)[0]
    if count >= 3 and repeated_failures >= 3:
        failure_loop = True
    
    findings = {
        "total_entries": len(memory), 
        "repeated_failures": repeated_failures,
        "most_common_action": most_common_action,
        "action_count": count,
        "failure_loop_detected": failure_loop,
        }

    logger.debug("Memory findings: %s", findings)
    return findings