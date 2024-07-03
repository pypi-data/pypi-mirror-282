from exam_generator.exam import MCQuestion
from types import SimpleNamespace
from questions.utils.puppets import PuppetAgent


#
# class PuppetAgent(Agent):
#     def __init__(self, trainer, actor):
#         self.trainer = trainer
#         self.actor = actor
#
#     def pi(self, s, k, info=None):
#         return self.actor.pi(s, k)
#
#     def train(self, *args, **kwargs):
#         self.trainer.train(*args, **kwargs)
#
#
#     def __getattr__(self, name):
#         a = 234
#         return getattr(self.trainer, name)

class MC_Tabular02(MCQuestion):
    def __init__(self, seed, **kwargs):
        super().__init__(seed, **kwargs)

    def generate(self):
        x = SimpleNamespace()
        # from irlc import train, VideoMonitor
        from irlc.ex09.value_iteration_agent import ValueIterationAgent
        from irlc.ex10.mc_agent import MCAgent
        # from irlc.lectures

        from irlc.gridworld.gridworld_environments import SuttonMazeEnvironment
        x.living = -2

        env = SuttonMazeEnvironment(living_reward=x.living)
        from irlc import train, interactive
        # Note you can access the MDP for a gridworld using env.mdp. The mdp will be an instance of the MDP class we have used for planning so far.
        vagent = ValueIterationAgent(env, mdp=env.mdp)  # Make a ValueIteartion-based agent
        env = SuttonMazeEnvironment(living_reward=x.living)
        # Let's have a cute little animation. Try to leave out the agent_monitor_keys line to see what happens.
        # sagent = SarsaLambdaAgent(env, gamma=.8, epsilon=0.1, alpha=0.5, lamb=0.9)
        import numpy as np
        gammas = (2 + np.random.randint(5) + np.arange(4) ) / 10
        gammas = np.random.permutation(list(gammas) )
        gamma = gammas[0]
        # gamma = 0.9

        # gammas = np.random.permutation(list(gammas))
        # gamma = lambds[0]



        x.answers = gammas

        sagent = MCAgent(env, first_visit=True, gamma=gamma, epsilon=0.1, alpha=0.8)
        pagent = PuppetAgent(sagent, vagent)
        # env = VideoMonitor(env, agent=pagent)
        env, agent = interactive(env, pagent, autoplay=True)
        stats, trajectories = train(env, pagent, num_episodes=1)
        env.reset()
        # env.plot()
        x.fig1 = 'tabular2'
        x.gamma = gamma
        k = -6
        s, a = trajectories[0].state[k], trajectories[0].action[k]
        q_true = sagent.Q[s,a]
        # sagent.Q[s, a] = 0

        # env.display_pygame.annotate_text(state=s, fontsize=120, symbol="?")

        # q_alt = q_true *
        env.plot()
        x.q_true = q_true
        # trajectories[0].states[-3]
        self.savepdf(x.fig1)

        # train(env, agent, num_episodes=1)  # Train for 100 episodes
        # env.savepdf("smallgrid.pdf")  # Take a snapshot of the final configuration
        # env.close()  # Whenever you use a VideoMonitor, call this to avoid a dumb openglwhatever error message on exit
        #
        # x.z = 223
        # x.fig1 = 'stuff'
        # x.answers = ['fish is good', 'chips', 'orange', 'I am muppet']
        env.close()
        return x

