from exam_generator.exam import Question
from types import SimpleNamespace
from irlc import Agent
from matplotlib import pyplot as plt
import numpy as np
from irlc.ex11.q_agent import QAgent  # sarsa_agent import SarsaAgent
from irlc.ex12.sarsa_lambda_agent import SarsaLambdaAgent
from irlc.ex10.mc_agent import MCAgent

from irlc.gridworld.gridworld_environments import SuttonCornerGridEnvironment, BookGridEnvironment

from irlc import train, interactive

class Bellman02(Question):
    # def __init__(self, seed):
    #     super().__init__(seed)

    def generate(self):
        np.random.seed(3)
        x = SimpleNamespace()
        x.sol = SimpleNamespace()
        x.fig1 = 'mdpfig'
        x.gamma = 2/3
        v1, v2 = (2 + x.gamma ) / (4-4*x.gamma),  (4 - x.gamma ) / (4-4*x.gamma)
        x.v2 = v2
        print(v1, v2)
        x.sol.a = (1 + x.gamma * x.v2) / (2 -x.gamma)
        print(x.sol.a)

        return x

