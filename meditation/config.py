# meditation/config.py


"""
Meditation Configuration

Defines thresholds, toggles, and constants for the meditation module.
In the future, these can be modified by Omnis itself via introspection.
"""


# Step 1: Reflextion trigger threshold (e.g. agent fails to progress)
STUCK_THRESHOLD = 6 # Default trigger if no progress for N steps

# Step 2: Enable verbose mode for debugging internal steps
VERBOSE_LOGGING = True

# Step 3: Define logging level
LOG_LEVEL = "DEBUG" # Options: DEBUG, INFO, WARNING, ERROR

# Step 4: Placeholder for future dynamic tuning
ALLOW_SELF_TUNING = False