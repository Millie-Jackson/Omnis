"""
env/wrapper.py
"""


from env.games.checkers_dummy import DummyCheckers

def make_env(name: str):

    if name == "checkers":
        return DummyCheckers()
    else:
        raise ValueError(f"Unkown environment: {name}")
