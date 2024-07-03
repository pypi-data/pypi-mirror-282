from exam_generator.exam import MCQuestion
from types import SimpleNamespace
import numpy as np

class MCBandit01(MCQuestion):
    def __init__(self, seed, **kwargs):
        super().__init__(seed, **kwargs)
        # select random elements from the bank.

    def generate(self):
        x = SimpleNamespace()
        K = np.random.randint(3,5)
        x.qs = np.around(np.random.randn(K)*2,1)
        x.eps = 0.1
        x.sigma = np.around(np.random.rand()*2+0.5,1)
        x.K = K

        kopt = x.qs.argmax()
        kalt = np.random.randint(K)
        x.kalt = kalt
        x.kopt = kopt
        x.answers = [x.qs[kopt] * (1 - x.eps) + x.qs[kalt]*x.eps,
                   x.qs[kopt] * (1 - x.eps) - x.qs[kalt] * x.eps,
                   x.qs[kopt] * x.eps + (1-x.eps)*x.qs[kalt],
                   (x.qs[kopt] +x.qs[kalt] * x.eps)/2
                   ]

        return x

        x.NSN = 2
        x.NS0 = 1
        x.NSk = 10
        x.NA = 4
        x.NW = 2
        x.N = 10

        x.answers = [x.NS0 * x.NW * x.NA + (x.N-1) * x.NSk * x.NW * x.NA,
                     x.NS0 * x.NW * x.NA + (x.N - 1) * x.NSk * x.NW * x.NA + x.NSN,
                     x.NSN * x.NW * x.NA + (x.N - 1) * x.NSk * x.NW * x.NA ,
                     (x.NS0 + x.NSN) * x.NW * x.NA + (x.N - 1) * x.NSk * x.NW * x.NA,
                     ]
        return x
        # Make a figure.
        import matplotlib.pyplot as plt
        from irlc.ex04.pid import PID

        pid1 = [ [1, 0, 0], [2, 0, 0], [3, 0, 0]  ]
        pid1 = np.random.permutation(pid1)
        dt = 0.5
        N = 6

        X = np.zeros( (len(pid1), N+1) )
        U = np.zeros( (len(pid1), N) )
        xstar = 4

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

        # plt.show()
        return x

