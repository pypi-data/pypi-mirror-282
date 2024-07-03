from exam_generator.exam import MCQuestion
from types import SimpleNamespace
import numpy as np

class MCPid(MCQuestion):
    def __init__(self, seed):
        super().__init__(seed)
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

        pid1 = [ [1, 0, 0], [2, 0, 0], [3, 0, 0]  ]
        pid1 = np.random.permutation(pid1)
        dt = 0.5
        N = 6

        X = np.zeros( (len(pid1), N+1) )
        U = np.zeros( (len(pid1), N) )
        xstar = 0

        for s, (p, i, d) in enumerate(pid1):
            xs = [6]
            us = []

            pid = PID(dt, Kp=p, Ki=i, Kd=d, target=xstar)
            for k in range(N):
                # dt = 0.5
                us.append( pid.pi(xs[-1]) )
                xs.append(xs[-1] + 0.5 * dt * us[-1])
            X[s, :] = np.asarray(xs)
            U[s, :] = np.asarray(us)

        x.x0 = X[0,0]
        x.u0 = U[0,0]
        plt.plot(X[0,:], 'ko-', markersize=10, mfc='blue', label='$x_k$')
        plt.plot(U[0,:], 'ks-', markersize=10, mfc='red', label='$u_k$')
        plt.xlabel('$k$')
        plt.legend()
        plt.grid()
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

