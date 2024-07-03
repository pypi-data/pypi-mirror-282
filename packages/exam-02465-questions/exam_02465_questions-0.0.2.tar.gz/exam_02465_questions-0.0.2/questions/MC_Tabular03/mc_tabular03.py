from exam_generator.exam import MCQuestion
from types import SimpleNamespace
import numpy as np
import random
from irlc.ex11.q_agent import QAgent
from irlc.gridworld.gridworld_environments import SuttonCornerGridEnvironment, BookGridEnvironment
from irlc import train, interactive

class MC_Tabular03(MCQuestion):
    def __init__(self, seed, **kwargs):
        super().__init__(seed, **kwargs)

    def generate(self):
        seed = 3
        random.seed(seed)
        np.random.seed(seed)
        x = SimpleNamespace()
        x.alpha = np.round(0.5 + 0.5 * np.random.rand(), decimals=1)
        x.R_possible = [-10, -1, 0, 1, 2]
        x.gamma = np.round(0.5 + 0.5 * np.random.rand(), decimals=1)
        # x.answer = 1 / (1 - x.gamma) * max(x.R_possible)
        # env = SuttonCornerGridEnvironment(living_reward=0)
        seed = seed + 2
        x.living_reward = 1
        env = SuttonCornerGridEnvironment(living_reward=x.living_reward, seed=seed)
        # epsilon = 0.1
        alpha = x.alpha
        gamma = x.gamma

        sagent = QAgent(env, gamma=gamma, epsilon=1., alpha=alpha)
        train(env, sagent, num_episodes=20, seed=seed)
        # sagent.epsilon = epsilon
        for s in sagent.Q.q_:
            for a in sagent.Q.q_[s]:
                sagent.Q.q_[s][a] = np.random.randn()

        env = SuttonCornerGridEnvironment(living_reward=x.living_reward, seed=seed, render_mode='human')
        env, agent = interactive(env, sagent, autoplay=True)
        s0, info = env.reset()
        sagent.epsilon = 1
        x.a0 = sagent.pi_eps(s0, info)

        # train(env, sagent, max_steps=2, num_episodes=1, seed=seed)
        env.display_pygame.annotate_text(state=env.state, action=x.a0, symbol='?', color=(100, 100, 220), bold=False)
        # env.display_pygame.annotate_text(state=(2, 0), dy=-0.2, symbol='x', color=(200, 50, 50), bold=False)
        env.plot()
        x.fig1 = 'rl3'
        self.savepdf(x.fig1)
        sp, r, term, trunc, info = env.step(x.a0)
        x.q_old = sagent.Q[s0, x.a0]
        x.q_next_best = sagent.Q[sp, sagent.Q.get_optimal_action(sp, info)]
        sagent.train(s0, x.a0, r, sp, term, None,None)
        env.close()
        x.mdp = env.mdp

        x.q_new = sagent.Q[s0,x.a0]

        qq = x.q_old + alpha * (x.living_reward + gamma *  x.q_next_best - x.q_old)

        x.q2 =  alpha * (x.living_reward + gamma *  x.q_next_best - x.q_old)
        x.q3 = x.q_old + alpha * (x.living_reward + gamma *  x.q_next_best )
        x.q4 = x.q_old +  (x.living_reward + gamma * x.q_next_best - x.q_old)
        x.q5 = x.q_old + alpha * (x.living_reward + x.q_next_best - x.q_old)
        x.q6 = x.q_old + alpha * (gamma * x.living_reward +  gamma * x.q_next_best - x.q_old)
        # print(f"{x.q2=}")
        # print(f"{alpha=}")
        assert x.q_new == qq
        qs = [x.q2, x.q3, x.q4,x.q5,x.q6]
        np.random.shuffle(qs)
        x.answers = [x.q_new] + list(qs)
        x.answers = x.answers[:4]
        # print(f"{x.answers=}")
        return x
