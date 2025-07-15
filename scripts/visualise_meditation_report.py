# scripts/visualise_meditation_report.py


"""
Visualise Meditation Report

Generates a PNG summary of the latest meditation report.
"""


import json
import os
import glob
import logging
import matplotlib.pyplot as plt
from datetime import datetime


logger = logging.getLogger(__name__)

REPORT_DIR = "logs/meditation_reports"
OUTPUT_FILENAME = "summary_{timestamp}.png"


def find_latest_report():
    files = sorted(
        glob.glob(os.path.join(REPORT_DIR, "report_*.json")),
        key=os.path.getmtime,
        reverse=True,
    )

    if not files:
        print("[Visualisation] No report found.")
        return None

    return files[0] if files else None

def visualise_report(report_path):
    with open(report_path, "r") as f:
        report = json.load(f)

    memory = report["memory"]
    goals = report["goals"]

    # Step 1: Prepare plot
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = {
        "Failures": memory["repeated_failures"],
        "Memory Entries": memory["total_entries"],
        "Priority Conflicts": len(goals["priority_conflicts"]),
        "Duplicate Goals": len(goals["duplicates"]),
        "Drift Score (x10)": goals["drift_score"] * 10,
    }

    labels = list(bars.keys())
    values = list(bars.values())
    ax.bar(labels, values, color="teal")
    ax.set_title("Meditation Summary", fontsize=16)
    ax.set_ylabel("Score")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    # Step 2: Annotate bars
    for i, (label, value) in enumerate(bars.items()):
        ax.text(i, value + 0.2, f"{value:.1f}", ha="center", va="bottom")

    # Step 3: Save image
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    output_path = os.path.join(REPORT_DIR, OUTPUT_FILENAME.format(timestamp=timestamp))
    os.makedirs(REPORT_DIR, exist_ok=True) # Ensure path exists
    plt.tight_layout()
    plt.savefig(output_path)
    logger.info(f"[Visualisation] Saved: {output_path}")
    plt.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    path = find_latest_report()
    if path:
        visualise_report(path)