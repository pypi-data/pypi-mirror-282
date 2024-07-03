from exam_generator.exam import Question
from types import SimpleNamespace

from questions.utils.puppets import PuppetAgent


class SarsaLambda01(Question):
    def __init__(self, seed):
        super().__init__(seed)

    def generate(self):
        x = SimpleNamespace()
        # from irlc import train, VideoMonitor
        from irlc.ex09.value_iteration_agent import ValueIterationAgent
        from irlc.ex12.sarsa_lambda_agent import SarsaLambdaAgent
        from irlc.gridworld.gridworld_environments import OpenGridEnvironment
        env = OpenGridEnvironment(living_reward=-1)
        from irlc import train, interactive
        # Note you can access the MDP for a gridworld using env.mdp. The mdp will be an instance of the MDP class we have used for planning so far.
        vagent = ValueIterationAgent(env, mdp=env.mdp)  # Make a ValueIteartion-based agent
        env = OpenGridEnvironment(living_reward=0)
        # Let's have a cute little animation. Try to leave out the agent_monitor_keys line to see what happens.
        sagent = SarsaLambdaAgent(env, gamma=1, epsilon=0.1, alpha=0.5, lamb=0.9)

        pagent = PuppetAgent(sagent, vagent)
        # env = VideoMonitor(env, agent=pagent)
        env, agent = interactive(env, pagent, autoplay=True)
        train(env, pagent, num_episodes=1)
        env.reset()
        env.plot()
        x.fig1 = 'pagent'
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

