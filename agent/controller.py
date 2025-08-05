'''
agent/controller.py
'''


from env.wrapper import make_env
from agent.perception import Perception
from agent.planning import Planner
from agent.goal_checker import is_goal_achieved
from agent.memory import Memory
import random
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class AgentController:

    def __init__(self, env_name="checkers"):
        
        self.env = make_env(env_name)
        self.state = None
        self.done = False
        self.perception = Perception()
        self.planner = Planner()
        self.memory = Memory()
        self.goal = "reach_turn_5"

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

            # Always parse state after last env.step()
            parsed_state = self.perception.parse(self.state)

            if is_goal_achieved(parsed_state, self.goal):
                logger.info(f"Goal '{self.goal}' achieved! Ending episode.")
                break

            action = self.planner.choose_action(parsed_state, legal)
            logger.info(f"Agent action: {action}")

            self.state, reward, self.done, info = self.env.step(action)
            logger.info(f"New state: {self.state} | Reward: {reward} | Done: {self.done} | Info: {info}")

            self.memory.record(self.state, action, reward, info)

            parsed_state = self.perception.parse(self.state)
            logger.info(f"Perceived state: {parsed_state}")

            self.env.render()

        logger.info("Game over.")  
        logger.info(f"Full episode memory ({len(self.memory.get_episode())} steps):")
        for step in self.memory.get_episode():
            logger.info(step)  
        self.memory.save_to_file()