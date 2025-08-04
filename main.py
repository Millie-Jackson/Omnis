"""
main.py
"""


from agent.controller import AgentController

if __name__ == "__main__":

    agent = AgentController(env_name="checkers")
    agent.run()    