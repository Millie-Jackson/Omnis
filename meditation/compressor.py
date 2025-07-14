# meditation/compressor.py


"""
Memory Compressor

Reduces memory size and noise by pruning redundant or outdated entries.
Helps reset focus and streamline reasoning.
"""


import logging


logger = logging.getLogger(__name__)


def compress_memory(memory, findings, keep_last_n=5):
    """
    Compresses memory by:
    - Keeping only the N most recent events
    - Ensuring key events (e.g., repeated failures) are retained

    Args:
        memory (list of dict): Agent memory (assumed ordered by time)
        findings (dict): Results from memory scan (e.g., failure_loop_detected)

    Returns:
        list of dict: Compressed memory
    """

    # Step 1: Keep last N entries
    recent_memory = memory[-keep_last_n:]

    # Step 2: Add failure envents if found outside that window
    if findings.get("failure_loop_detected"):
        failure_entries = [m for m in memory if m.get("result") == "fail"]
        for entry in failure_entries:
            if entry not in recent_memory:
                recent_memory.append(entry)
    
    # Step 3: Remove duplicates while preserving order
    seen = set()
    compressed = []
    for m in recent_memory:
        key = (m.get("step"), m.get("action"), m.get("result"))
        if key not in seen:
            seen.add(key)
            compressed.append(m)

    logger.debug("Compressed memory size: %d → %d", len(memory), len(compressed))
    return compressed