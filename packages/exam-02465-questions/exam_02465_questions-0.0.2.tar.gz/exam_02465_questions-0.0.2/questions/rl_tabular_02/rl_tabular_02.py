from exam_generator.exam import Question
from types import SimpleNamespace

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


class Tabular02(Question):
    # def __init__(self, seed):
    #     super().__init__(seed)

    def generate(self):
        import numpy as np

        # np.random.seed(4+ 0*self.seed)
        print(np.random.rand())
        # random.seed(4)
        from irlc.ex11.q_agent import QAgent

        # from irlc.ex09 import rl_agent

        # from irlc.ex11.q_agent import QAgent  # sarsa_agent import SarsaAgent

        # The environment is deterministic.


        from irlc.gridworld.gridworld_environments import BookGridEnvironment


        # print(random.random())

        # assert False
        x = SimpleNamespace()
        x.sol = SimpleNamespace()
        x.alpha = np.round(0.5 + 0.5 * np.random.rand(), decimals=1)
        x.R_possible = [-10, -1, 0, 1, 2]
        x.gamma = np.round(0.5 + 0.5 * np.random.rand(), decimals=1)
        x.gamma = 1
        # x.answer = 1/(1-x.gamma) * max(x.R_possible)
        # env = SuttonCornerGridEnvironment(living_reward=0)
        env = BookGridEnvironment(living_reward=0)
        x.mdp= env.mdp

        a = 34
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
        alpha = 0.9
        gamma = 0.9

        sagent = QAgent(env, gamma=gamma, epsilon=.7, alpha=alpha)

        # for _ in range(10):
        #     print(sagent.pi_eps(env.reset(seed=43), info=dict(seed=34)))

        # print(np.random.rand())
        # assert False
        seed = 1
        train(env, sagent, num_episodes=9, seed=seed)
        sagent.epsilon = epsilon


        env, agent = interactive(env, sagent, autoplay=True)
        train(env, sagent, max_steps=16, num_episodes=1)
        # env.state

        env.display_pygame.annotate_text(state=env.state, dy=-0.25, symbol='x', bold=False)
        env.display_pygame.annotate_text(state=env.state, dx=-0.2, symbol='o', color=(50, 200, 50), bold=False)

        env.display_pygame.annotate_text(state=(0,0), dy=-0.25, symbol='n', color=(50, 50, 200), bold=False)
        env.display_pygame.annotate_text(state=(0,0), dx=0.2, symbol='e', color=(50, 50, 200), bold=False)

        # from irlc.gridworld.gridworld_mdp


        env.plot()
        x.fig1 = 'rl1'
        self.savepdf(x.fig1)
        # env.mdp.A(env.state)
        ## PART A: Move north and east.
        from irlc.gridworld.gridworld_mdp import GridworldMDP
        x.a_action1 = GridworldMDP.NORTH
        # a2 = GridworldMDP.EAST


        dd = dict(env.mdp.Psr(env.state, x.a_action1))
        sp, r = max(dd, key=dd.get)
        values = set( [round(q, ndigits=2) * gamma for q in sagent.Q.get_Qs(sp)[1]] )
        x.sol.a_vals = list(values)

        ## SOLUTION TO PART C
        from irlc.gridworld.demo_agents.hidden_agents import ValueIterationAgent3
        env.close()
        env = BookGridEnvironment(render_mode='human')
        env, agent = interactive(env, ValueIterationAgent3(env, epsilon=0.1, gamma=0.95), autoplay=True)
        train(env, agent, num_episodes=2)
        x.fig2 = 'rl2'
        env.plot()
        self.savepdf(x.fig2)
        env.close()
        return x

