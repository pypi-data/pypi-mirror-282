from exam_generator.exam import MCQuestion
from types import SimpleNamespace
import numpy as np

class MCPid(MCQuestion):
    def __init__(self, seed, answer_permutation=None):
        super().__init__(seed, answer_permutation=answer_permutation)
        # select random elements from the bank.

    def generate(self):
        x = SimpleNamespace()
        x.z = 223
        x.fig1 = 'stuff'
        from irlc.ex04.pid_locomotive_agent import PIDLocomotiveAgent
        x.answers = ['fish is good', 'chips', 'orange', 'I am muppet']
        # Make a figure.

        import matplotlib.pyplot as plt
        from irlc.ex04.pid import PID
        plt.close()
        pid1 = [ [2, 0, 0], [1, 0, 0], [0.2, 0, 0], [0.5, 0, 0] ]

        x.u_true = np.random.randint(4)

        pid1 = np.random.permutation(pid1)
        dt = 0.5
        N = 5

        X = np.zeros( (len(pid1), N+1) )
        U = np.zeros( (len(pid1), N) )
        xstar = np.random.randint(1,4)*2

        for s, (p, i, d) in enumerate(pid1):
            xs = [10]
            us = []
            pid = PID(dt, Kp=p, Ki=i, Kd=d, target=xstar)
            for k in range(N):
                # dt = 0.5
                us.append( pid.pi(xs[-1]) )
                xs.append(xs[-1] + 0.4 * dt * us[-1])
            X[s, :] = np.asarray(xs)
            U[s, :] = np.asarray(us)

        x.x0 = X[x.u_true,0]
        x.u0 = U[x.u_true,0]
        plt.figure(figsize=(8,5))

        plt.plot(X[0,:], 'ko-', markersize=10, mfc='black', label='$x_k$')
        lts = ['ks-', 'k^-', 'kd-', 'k>-']

        colors = ['red', 'blue', 'green', 'yellow']
        for k in range(4):
            plt.plot(U[k,:], lts[k], markersize=10, mfc=colors[k], label='$u^{(%i)}_k$'%(k+1,))
        plt.plot([0, X.shape[1]-1], [xstar, xstar], '--', label="$x^*$", linewidth=3)

        x.Kp, x.Ki, x.Kd = pid1[x.u_true]

        x.e = xstar - x.x0

        plt.xlabel('$k$')
        plt.legend()
        plt.grid()
        # plt.show()
        # plt.show()
        # plt.plot(np.sin(np.linspace(0, 1)))
        x.fig1 = 'pid1'
        x.figsol = 'pid1sol'

        x.dt = dt
        x.xstar = xstar

        self.savepdf(x.fig1)
        plt.close()

        plt.plot(X[0, :], 'ko-', markersize=10, mfc='blue', label='$x_k$')
        plt.plot(U[:, :].T, 'ks-', markersize=10, mfc='red', label='$u_k$')

        self.savepdf(x.figsol)
        x.pid = pid1
        plt.close()

        # plt.show()
        return x

