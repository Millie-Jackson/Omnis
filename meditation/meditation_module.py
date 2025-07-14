# meditation/meditation_module.py


"""
Meditation Module for Omnis
---------------------------
This module provides a reflective routine to detect and resolve
internal misalignments or stagnation in agent cognition.

Usage:
    from meditation.meditation_module import run_meditation
    run_meditation(agent_state)
"""


import logging
from meditation.triggers import check_meditation_trigger
from meditation.memory_scanner import scan_memory
from meditation.goal_checker import evaluate_goals
from meditation.compressor import compress_memory
from meditation.reporter import generate_report


logger = logging.getLogger(__name__)


def run_meditation(agent_state):
    """
    Main meditation loop.
    
    Args:
        agent_state (dict): Dictionary-like snapshot of the current agent's internal state.
    
    Returns:
        updated_state (dict): Modified state after meditation.
        report (dict): Self-diagnostic output.
    """

    logger.info("[Meditation] Triggered. Pausing environment interaction...")

    # Step 1: Check if meditation is actually needed
    if not check_meditation_trigger(agent_state):
        logger.info("[Meditiation] No trigger detected. Skipping.")
        return agent_state, None
    
    # Step 2: Scan memory
    memory_findings = scan_memory(agent_state["memory"])

    # Step 3: Evaluate goal coherence
    goal_status = evaluate_goals(agent_state["goals"])

    # Step 4: Compress and refactor memory
    new_memory = compress_memory(agent_state["memory"], memory_findings)

    # Steps 5: Generate self-reflection report
    report = generate_report(memory_findings, goal_status)

    # Step 6: Update agent state
    agent_state["memory"] = new_memory
    agent_state["last_reflection"] = report

    logger.info("[Meditation] Complete.")
    return agent_state, report