# meditation/triggers.py


"""
Trigger Detection

Contains logic to determine when the agent should enter
meditation based on internal performance metrics or conflict signals.
"""


import logging
from meditation.config import STUCK_THRESHOLD


logger = logging.getLogger(__name__)


def check_meditation_trigger(agent_state):
    """
    Decide whether the agent should enter meditation.

    Args:
        agent_state (dict): The agent's internal state.

    Returns:
        bool: True if meditation should be triggered.
    """

    # Placeholder: Trigger if stuck for too many steps
    steps_stuck = agent_state.get("steps_without_progress", 0)
    trigger = steps_stuck >= STUCK_THRESHOLD
    logger.debug("Trigger check: steps_without_progress=%d → %s", steps_stuck, STUCK_THRESHOLD, trigger)

    return trigger