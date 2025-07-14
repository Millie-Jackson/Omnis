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
            {"steps": 1, "action": "move_forward", "result": "fail"},
            {"steps": 2, "action": "move_forward", "result": "fail"},
            {"steps": 3, "action": "move_forward", "result": "fail"},
        ],
        "goals": [
            {"id": "reach_exit", "priority": 1},
            {"id": "collect_items", "priority": 2},
            {"id": "reach_exit", "priority": 3},
        ],
        "last_reflection": None,
    }