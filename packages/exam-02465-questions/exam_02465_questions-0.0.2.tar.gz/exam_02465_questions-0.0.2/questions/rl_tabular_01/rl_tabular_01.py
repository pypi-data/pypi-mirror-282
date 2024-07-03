from exam_generator.exam import Question
from types import SimpleNamespace
from irlc import Agent
from matplotlib import pyplot as plt
import numpy as np
import irlc

from irlc.ex11.q_agent import QAgent  # sarsa_agent import SarsaAgent
from irlc.ex12.sarsa_lambda_agent import SarsaLambdaAgent
from irlc.ex10.mc_agent import MCAgent

from irlc.gridworld.gridworld_environments import SuttonCornerGridEnvironment, BookGridEnvironment

from irlc import train, interactive

#
# class PuppetAgent(Agent):
#     def __init__(self, trainer, actor):
#         self.trainer = trainer
#         self.actor = actor
#
#     def pi(self, s, k=None):
#         return self.actor.pi(s, k)
#
#     def train(self, *args, **kwargs):
#         self.trainer.train(*args, **kwargs)
#
#
#     def __getattr__(self, name):
#         a = 234
#         return getattr(self.trainer, name)
#         # return self.agent1.__getattr__(name)
#         # pass


class Tabular01(Question):
    # def __init__(self, seed):
    #     super().__init__(seed)

    def generate(self):
        seed = 3
        np.random.seed(seed)
        x = SimpleNamespace()
        x.alpha = np.round(0.5 + 0.5 * np.random.rand(), decimals=1)
        x.R_possible = [-10, -1, 0, 1, 2]
        x.gamma = np.round(0.5 + 0.5 * np.random.rand(), decimals=1)
        x.answer = 1/(1-x.gamma) * max(x.R_possible)
        # env = SuttonCornerGridEnvironment(living_reward=0)
        seed = seed + 2
        env = BookGridEnvironment(living_reward=0, seed=seed)

        # irlc.ex09.value_iteration_agent
        # import ValueIterationAgent
        # Note you can access the MDP for a gridworld using env.mdp. The mdp will be an instance of the MDP class we have used for planning so far.
        # vagent = ValueIterationAgent(env, mdp=env.mdp)  # Make a ValueIteartion-based agent
        # env = OpenGridEnvironment(living_reward=0)
        # Let's have a cute little animation. Try to leave out the agent_monitor_keys line to see what happens.
        # sagent = SarsaLambdaAgent(env, gamma=.8, epsilon=0.1, alpha=0.5, lamb=0.9)
        # lambds = (2 + np.random.randint(5) + np.arange(4)) / 10
        # lambds = np.random.permutation(list(lambds))
        # gamma = lambds[0]
        # x.answers = lambds
        epsilon = 0.1
        alpha = x.alpha
        gamma = x.gamma

        sagent = QAgent(env, gamma=gamma, epsilon=.7, alpha=alpha)
        train(env, sagent, num_episodes=10, seed=seed)
        sagent.epsilon = epsilon

        env, agent = interactive(env, sagent, autoplay=True)
        train(env, sagent, max_steps=2, num_episodes=1, seed=seed)
        env.display_pygame.annotate_text(state=env.state, dx=+0.2, symbol='?', color=(200, 200, 50), bold=False)
        env.display_pygame.annotate_text(state=(2,0), dy=-0.2, symbol='x', color=(200, 50, 50), bold=False)
        env.plot()
        x.fig1 = 'rl1'
        self.savepdf(x.fig1)



        # env.display_pygame.annotate_text(state=env.state, dx=-0.2, symbol='o', color=(50, 200, 50), bold=False)
        # env.display_pygame.annotate_text(state=(0,0), dy=-0.25, symbol='n', color=(50, 50, 200), bold=False)
        # env.display_pygame.annotate_text(state=(0,0), dx=0.2, symbol='e', color=(50, 50, 200), bold=False)


        env.mdp.A(env.state)
        from irlc.gridworld.gridworld_mdp import GridworldMDP
        a = GridworldMDP.EAST

        # NORTH = 0  # These are the four available actions.
        # EAST = 1
        # SOUTH = 2
        # WEST = 3

        s = env.state
        mdp = env.mdp

        dd = dict(mdp.Psr(s, a))
        sp, r = max(dd, key=dd.get)

        actions, qs = sagent.Q.get_Qs(sp)
        qs = np.around(qs, 2)
        Qsa = np.around(sagent.Q[s,a], 2)

        q_new = Qsa + alpha * (r + gamma * max(qs) - Qsa )

        print("Change in Q: ", q_new - Qsa)
        x.action_label = 'east'
        env.close()
        x.sol = SimpleNamespace()
        x.sol.Qnew = q_new
        x.epsilon = epsilon

        x.sol.Qmax = max(qs)

        a = 234
        # env.savepdf(x.fig1)
        # a = 234

        # pagent = PuppetAgent(sagent, vagent)
        # env = VideoMonitor(env, agent=pagent)
        # env, agent = interactive(env, pagent, autoplay=True)
        # train(env, pagent, num_episodes=1)
        # env.reset()
        # env.plot()
        # x.fig1 = 'pagent'
        # x.gamma = gamma



        return x

