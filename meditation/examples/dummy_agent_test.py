# meditation/examples/dummy_agent_test.py


"""
Dummy Agent for Meditation Module Testing

Simulates an Omnis-like agent with:
- Fake memory
- Simple goal stack
- Artificial stagnation
"""


def create_dummy_agent_state():
    return {
        "steps_without_progress": 15, # Trigger threshold = 10
        "memory": [
            {"step": 1, "action": "go", "result": "fail"},
            {"step": 2, "action": "go", "result": "fail"},
            {"step": 3, "action": "go", "result": "fail"},
            {"step": 4, "action": "wait", "result": "pass"},
            {"step": 5, "action": "go", "result": "fail"},
            {"step": 6, "action": "go", "result": "fail"},
        ],
        "goals": [
            {"id": "reach_exit", "priority": 1},
            {"id": "collect_items", "priority": 2},
            {"id": "reach_exit", "priority": 3},
        ],
        "last_reflection": None,
    }