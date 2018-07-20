import gym
from gym import wrappers
import configparser


class rl_agent:
    def __init__(self,config_file:str=None):
        self.parse_config(config_file)

    def parse_config(self,config_file:str=None):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(config_file)
        self.environment = config['DEFAULT']['environment']
        self.max_episodes = config.getint('DEFAULT','max_episodes')

    def update(self):
        env = gym.make(self.environment)
        env.reset()
        for _ in range(self.max_episodes):
            env.render()
            env.step(env.action_space.sample())

if __name__ == '__main__':
    gym_agent = rl_agent('/home/naraya01/github_projects/RL_ctrl/config/ctrl_algos_config.ini')
    gym_agent.update()