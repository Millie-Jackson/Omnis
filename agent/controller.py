'''
agent/controller.py
'''


from env.wrapper import make_env
import random
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class AgentController:

    def __init__(self, env_name="checkers"):
        
        self.env = make_env(env_name)
        self.state = None
        self.done = False

    def select_action(self, legal_actions):
        """Stub action selection — random for now."""

        return random.choice(legal_actions)
    
    def run(self):
        """Main loop — runs one episode."""

        self.state = self.env.reset()
        self.done = False
        logger.info(f"Game started. Initial state: {self.state}")

        while not self.done:
            legal = self.env.legal_actions()
            action = self.select_action(legal)
            logger.info(f"Agent action: {action}")

            self.state, reward, self.done, info = self.env.step(action)
            logger.info(f"New state: {self.state} | Reward: {reward} | Done: {self.done} | Info: {info}")
            self.env.render()

        logger.info("Game over.")    