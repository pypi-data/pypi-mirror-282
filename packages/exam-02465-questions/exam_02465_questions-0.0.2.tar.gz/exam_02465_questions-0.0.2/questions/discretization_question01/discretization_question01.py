from exam_generator.exam import Question
from types import SimpleNamespace
from irlc import Agent
from irlc.ex03.control_model import ControlModel
from irlc.ex04.discrete_control_model import DiscreteControlModel
from irlc.ex03.control_cost import SymbolicQRCost
import gymnasium
from gymnasium.spaces import Box
import numpy as np
import sympy as sym

class VeryBasicControl(ControlModel):
    n = 2
    d = 1
    def __init__(self, *args, **kwargs):
        self.observation_space = Box(-np.inf, np.inf, shape=(self.n,))
        self.action_space = Box(-np.inf, np.inf, shape=(self.d,))
        # bounds = dict(x_low=[-np.inf]*self.n, x_high=[np.inf]*self.n,
        #                    u_low=[-np.inf] * self.d, u_high=[np.inf] * self.d,
        #                    )
        # cost = SymbolicQRCost.zero(self.observation_space.shape[0],self.action_space.shape[0])
        super().__init__()

    def sym_f(self, x, u, t=None):
        return [x[1], sym.cos(x[0] + u[0])]

    def get_cost(self) -> SymbolicQRCost:
        return SymbolicQRCost.zero(self.n, self.d)

class Discretization01(Question):
    def __init__(self, seed):
        super().__init__(seed)
    def generate(self):
        x = SimpleNamespace()
        bmodel = VeryBasicControl()
        dt = 0.2
        dmodel = DiscreteControlModel(bmodel, dt=0.04)
        # xs = symv('x', 2)
        # us = symv('u', 1)
        xs = sym.symbols(f"x0:2")
        us = sym.symbols('u0:1')

        fd = dmodel._f_discrete_sym(xs, us, dt=dt)
        w = sym.symbols("w")
        u = sym.symbols("u")


        fd[1].subs(xs[0], w)
        fd[1].subs(us[0], u)
        sym.latex(fd)
        u0 = np.zeros( (dmodel.action_size,))
        xp = dmodel.f( np.zeros((dmodel.state_size,)), u0)
        xpp = dmodel.f(xp, u0)
        x.u0 = u0
        x.dt = dt
        w_ddot = bmodel.sym_f([w, xs[1]], [u])
        x.f_tex = sym.latex(w_ddot[1])
        return x

