"""
agent/memory.py
"""


import logging
import json
from pathlib import Path
from datetime import datetime
from utils.logger import setup_logger


logger = setup_logger(__name__)


def timestamped_filename(prefix="episode", ext="json"):

    now = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    
    return f"{prefix}_{now}.{ext}"


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

    def save_to_file(self, folder="logs/episodes", prefix="episode"):
        Path(folder).mkdir(parents=True, exist_ok=True)
        filename = timestamped_filename(prefix)
        filepath = Path(folder) / filename
        with open(filepath, "w") as f:
            json.dump(self.episode, f, indent=2)
        logger.info(f"Episode memory saved to {filepath}")