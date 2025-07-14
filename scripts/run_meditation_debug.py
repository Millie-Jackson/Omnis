# scripts/run_meditation_debug.py


"""
Meditation Module Debug Launcher

Initialises logging, imports dummy agent, and runs the meditation loop.
Outputs results to console and file.
"""


import logging
import os
import json
from datetime import datetime
from meditation.config import LOG_LEVEL
from meditation.meditation_module import run_meditation
from meditation.examples.dummy_agent_test import create_dummy_agent_state


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("logs/meditation.log"),
        logging.StreamHandler()
    ]
)



def main():
    logger.info("Starting meditation test with dummy agent.")

    agent = create_dummy_agent_state()
    updated_agent, report = run_meditation(agent)

    if report:
        timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        report_path = f"logs/meditation_reports/report_{timestamp}.json"

        with open(report_path, "w") as f:
            json.dump(report, f, indent=4)

        logger.info("Meditation report saved to %s", report_path)
    else:
        logger.info("No meditation occurred.")


if __name__ == "__main__":
    main()