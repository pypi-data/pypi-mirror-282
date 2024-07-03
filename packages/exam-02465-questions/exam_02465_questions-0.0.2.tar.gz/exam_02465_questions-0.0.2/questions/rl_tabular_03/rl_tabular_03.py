from exam_generator.exam import Question
from types import SimpleNamespace
from irlc import Agent

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


grid_bridge_grid2 = [[ '#',-100, -100, -100,   -100, -100, '#'],
                    [   1, ' ',  'S',  ' ',   ' ',  ' ',  2],
                    [ '#',-100, -100, -100,  -100, -100, '#']]
from irlc.gridworld.gridworld_environments import GridworldEnvironment
class BridgeGridEnvironment(GridworldEnvironment):
    def __init__(self, *args, **kwargs):
        super().__init__(grid_bridge_grid2, *args, **kwargs)



class Tabular03(Question):
    # def __init__(self, seed):
    #     super().__init__(seed)

    def generate(self):
        x = SimpleNamespace()
        x.sol = SimpleNamespace()

        # np.random.seed(4+ 0*self.seed)
        # print(np.random.rand())
        # random.seed(4)

        # from irlc.ex09 import rl_agent

        # from irlc.ex11.q_agent import QAgent  # sarsa_agent import SarsaAgent

        # The environment is deterministic.
        from questions.utils.puppets import FixedPuppetAgent
        # from irlc.

        # from irlc.gridworld.gridworld_environments import SuttonCornerGridEnvironment, BookGridEnvironment, BridgeGridEnvironment
        from irlc.ex10.mc_evaluate import MCEvaluationAgent

        bg = BridgeGridEnvironment(living_reward=0, render_mode='human')
        env, agent = interactive(bg, Agent(bg), autoplay=True)
        env.reset()
        env.plot()
        x.fig0 = 'bridge_grid'

        self.savepdf(x.fig0)
        bg.close()
        # alpha = 0.6
        gamma = 0.8
        bg = BridgeGridEnvironment(living_reward=0, render_mode='human')
        actions0 = [3, 1, 1, 1, 1, 1, 0]
        pagent = FixedPuppetAgent(MCEvaluationAgent(env=bg, gamma=gamma, alpha=None, first_visit=True), actions=actions0)

        env, agent = interactive(bg, pagent, autoplay=True)
        train(env, pagent, num_episodes=1)
        s, _ = env.reset()

        x.v_first = pagent.agent.v[s]
        env.reset()
        env.plot()

        x.fig1 = 'mc_first_puppet'
        self.savepdf(x.fig1)

        # agent = MCEvaluationAgent(env=bg, gamma=0.9, alpha=0.6, first_visit=False)
        pagent =FixedPuppetAgent(MCEvaluationAgent(env=bg, gamma=gamma, alpha=None, first_visit=False), actions=actions0)

        env, agent = interactive(env, pagent, autoplay=True)
        train(env, pagent, num_episodes=1)
        env.reset()
        env.plot()
        x.v_every = pagent.agent.v[s]
        x.fig2 = 'mc_every_puppet'
        self.savepdf(x.fig2)
        x.actions = actions0
        # x.alpha = alpha

        x.gamma = gamma
        x.epsilon = 0.9
        x.mdp = bg.mdp
        bg.close()
        return x
