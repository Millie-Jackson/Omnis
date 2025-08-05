"""
agent/planning.py
"""


import logging
from utils.logger import setup_logger


logger = setup_logger(__name__)


class Planner:

    def __init__(self):
        pass

    def choose_action(self, state, legal_actions):
        """
        Given the parsed state and legal actions, pick one.
        For now: choose first valid action.
        """

        logger.debug(f"Planning action for state: {state}")

        if not legal_actions:
            return None
        
        return legal_actions[0]