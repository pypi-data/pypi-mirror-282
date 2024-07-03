from exam_generator.exam import Question, ProgrammingQuestion
from types import SimpleNamespace
import sympy as sym

class ProgramDP01(ProgrammingQuestion):
    program_file = "question_dp.py"
    # def __init__(self, seed):
    #     super().__init__(seed)
    def generate(self):
        x = SimpleNamespace()
        x.file = ''
        return x
        # bmodel = VeryBasicControl()
        dt = 0.2
        dmodel = DiscretizedModel(bmodel, dt=0.04)
        xs = symv('x', 2)
        us = symv('u', 1)
        # t = sym.symbols('t')
        fd = dmodel.f_discrete_sym(xs, us, dt=dt)
        sym.latex(fd)

        u0 = dmodel.action_space.sample() * 0 + 1
        xp = dmodel.f(dmodel.observation_space.sample() * 0, u0)
        xpp = dmodel.f(xp, u0)

        x.u0 = u0
        x.dt = dt
        x.f_tex = sym.latex(bmodel.sym_f(xs, us)[1])

        return x

        x, u = sym.symbols('x u')
        sym.diff(sym.cos(x), x, x)


        # from irlc import train, VideoMonitor
        from irlc.ex09.value_iteration_agent import ValueIterationAgent
        from irlc.ex12.sarsa_lambda_agent import SarsaLambdaAgent
        from irlc.gridworld.gridworld_environments import SuttonCornerGridEnvironment, OpenGridEnvironment
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
        self.savepdf(x.fig1 +".pdf")

        # train(env, agent, num_episodes=1)  # Train for 100 episodes
        # env.savepdf("smallgrid.pdf")  # Take a snapshot of the final configuration
        # env.close()  # Whenever you use a VideoMonitor, call this to avoid a dumb openglwhatever error message on exit
        #
        # x.z = 223
        # x.fig1 = 'stuff'
        # x.answers = ['fish is good', 'chips', 'orange', 'I am muppet']
        env.close()
        return x

