"""
agent/memory.py
"""


import logging
from utils.logger import setup_logger


logger = setup_logger(__name__)


class Memory:

    def __init__(self):

        self.episode = []

    def record(self, state, action, reward, info=None):
        """Store a step in memory."""

        entry = {
            "state": state,
            "action": action,
            "reward": reward,
            "info": info or {}
        }
        logger.debug(f"Recording memory: {entry}")
        self.episode.append(entry)

    def get_episode(self):

        return self.episode
    
    def clear(self):

        self.episode = []