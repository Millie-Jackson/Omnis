"""
agent/perception.py
"""


import logging
from utils.logger import setup_logger


logger = setup_logger(__name__)


class Perception:

    def __init__(self):
        pass

    def parse(self, raw_state):
        """
        Convert raw game state into structured format.
        For now: wrap it as a dict, to simulate real processing.
        """

        logger.debug(f"Parsing state: {raw_state}")

        structured = {
            "raw": raw_state,
            "turn": self.extract_turn(raw_state),
            "board": None
        }

        return structured
    
    def extract_turn(self, raw_state):
        """Stub logic to get turn number from dummy state."""

        if isinstance(raw_state, str) and "state_" in raw_state:
            try:
                return int(raw_state.split("_")[1])
            except (IndexError, ValueError):
                return None
        
        return None