"""
env/games/checkers_dummy.py
"""


from env.base import BaseGameEnv


class DummyCheckers(BaseGameEnv):

    def __init__(self):
        self.state = "initial_board"
        self.turns = 0

    def reset(self):
        self.state = "initial_board"
        self.turns = 0

        return self.state
    
    def step(self, action):

        self.turns += 1
        reward = 0
        done = self.turns > 5
        if done:
            reward = 1

        return f"state_{self.turns}", reward, done, {"turns": self.turns}
    
    def legal_actions(self):

        return ["move_a1_b2", "move_c3_d3", "pass"]
    
    def render(self):

        print(f"Current state: {self.state}")