from exam_generator.exam import MCQuestion
from types import SimpleNamespace
import numpy as np

class MCBandit02(MCQuestion):
    def __init__(self, seed, **kwargs):
        super().__init__(seed, **kwargs)
        # select random elements from the bank.

    def generate(self):
        x = SimpleNamespace()
        x.sol = SimpleNamespace()
        K = 4
        # K = np.random.randint(3,5)

        x.c = 1 + np.random.randint(2)
        dbest = 0.1

        def mdiff(Ns):
            return (np.abs(Ns - Ns[:, np.newaxis]) + np.eye(4) * 4).min().min()

        while True:

            Ns = np.random.randint(3, 16, size=(K,))

            # Must be greater than 1.





            UB = 4

            Qt = UB * 0.9
            t = np.sum(Ns)+1 # I guess?
            # qm = 1/( ( (UB - Qt )/x.c )**2 / np.log(t) )

            SS = np.round( (UB - x.c * np.sqrt( np.log(t) / Ns))*Ns )
            x.sol.arm = np.random.randint(K)
            SS[x.sol.arm] += 3
            x.SS = SS
            x.K = K

            x.xlabels = [f'Arm $a={k}$' for k in range(x.K)]
            x.ylabels = [f'$N_t(a)$', 'Total reward $S_t(a)$']
            x.X = np.stack( [Ns, x.SS])
            x.t = t

            x.tbl1 = 'tablebandit2'
            x.sol.ucb = x.SS / Ns + x.c * np.sqrt( np.log(t) / Ns)

            x.sol.qvals = x.SS / Ns
            x.sol.bounds = np.sqrt( np.log(t) / Ns)

            if x.sol.qvals.argmin() != x.sol.arm and x.sol.bounds.argmax() != x.sol.arm and mdiff(Ns) >= 3 and mdiff(x.sol.qvals) >= 0.2:

                break
            else:
                # print("Bad...")
                pass
        x.answers = [x.sol.arm] + [a for a in range(K) if a != x.sol.arm]
        return x


