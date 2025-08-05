"""
agent/goal_checker.py
"""


import logging
from utils.logger import setup_logger


logger = setup_logger(__name__)


def is_goal_achieved(state, goal: str) -> bool:
    """
    Simple goal checker.
    Example goal: 'reach_turn_5' → returns True if turn >= 5
    """

    logging.debug(f"Checking if goal '{goal}' is achieved in state: {state}")

    if goal.startswith("reach_turn_"):
        try:
            target_turn = int(goal.split("_")[-1])
            current_turn = state.get("turn", 0)
            return current_turn >= target_turn
        except Exception as e:
            logger.warning(f"Goal parse failed: {e}")
            return False
    
    return False