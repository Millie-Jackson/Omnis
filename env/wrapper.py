"""
env/wrapper.py
"""


from env.games.checkers_dummy import DummyCheckers

def make_env(name: str):

    if name == "checkers":
        return DummyCheckers()
    else:
        raise ValueError(f"Unkown environment: {name}")


class BaseGameEnv:

    def reset(self):
        """
        Resets the game to initial state.
        Returns initial observation
        """

        raise NotImplementedError
    
    def step(self, action):
        """
        Takes an action and returns:
        - observation: new game state
        - reward: numeric value (win = 1, lose = -1, else = 0)
        - done: whether the game is over
        - info: optional debug info (dict)
        """

        raise NotImplementedError
    
    def legal_actions(self):
        """Returns a list of legal actions in the current state."""

        raise NotImplementedError
    
    def render(self):
        """(Optional) Prints or visualises current state."""

        pass