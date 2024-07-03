from exam_generator.exam import Question
from types import SimpleNamespace
from irlc.ex04.discrete_control_model import DiscreteControlModel
import sympy as sym

from questions.discretization_question01.discretization_question01 import VeryBasicControl

class BC(VeryBasicControl):
    n = 1
    d = 1
    a = 4
    c = 0

    def sym_f(self, x, u, t=None):
        return [(self.a * x[0] * u[0])]

def line(f, xs, us, xb, ub):
    sub = dict(zip(xs + us, xb + ub))
    return sym.Matrix([f]).jacobian(xs).subs(sub) @ (sym.Matrix(xs) - sym.Matrix(xb)) + \
    sym.Matrix([f]).jacobian(us).subs(sub) @ (sym.Matrix(us) - sym.Matrix(ub)) + sym.Matrix([f]).subs(sub)


class Discretization02(Question):
    # def __init__(self, seed):
    #     super().__init__(seed)
    def generate(self):
        x = SimpleNamespace()
        x.sol = SimpleNamespace()

        bmodel = BC()
        dt = 0.5
        x.dt = dt
        dmodel = DiscreteControlModel(bmodel, dt=dt)

        xs = (sym.symbols('x'),) #symv('x',         bmodel.n)
        us = (sym.symbols('u'),) #symv('u',         bmodel.d)
        # xx = sym.symbols('x')

        f = bmodel.sym_f(xs, us)[0]
        x.f_tex = sym.latex(f)

        # ub = sym.symbols('\\bar{u}_1:3')
        # xb = sym.symbols('xb1:2')

        # sub = dict(zip(xs+us, xb+ub))
        # f_lin = sym.Matrix([f]).jacobian(xs).subs(sub) @ (sym.Matrix(xs) - sym.Matrix(xb) )   + \
        #             sym.Matrix([f]).jacobian(us).subs(sub)  @ (sym.Matrix(us) - sym.Matrix(ub) ) + sym.Matrix([f]).subs(sub)

        # x0 = (2,)
        # u0 = (1,1)

        xks = (sym.Symbol('x_k'),)
        # uks =  (sym.Symbol('u_{k,1}'), sym.Symbol('u_{k,2}') )

        uks = (sym.Symbol('u_k'),)

        f_euler =  self.fixf( (dt * f + xs[0]) )
        f_euler_k = f_euler.subs( zip(xs+us, xks + uks) )
        x.sol.f_euler_k = f_euler_k
        sym.latex(f_euler_k)

        # ub = sym.symbols('\\bar{u}_1:3')
        ub = sym.symbols('\\bar{u}'),
        xb = (sym.symbols('\\bar{x}'),)
        x.ub_val = (1,)

        # s0 = dict(zip(uks, x.ub_val))

        f_euler_lin = line(f_euler_k, xks, uks, xb, ub)
        f_euler_lin_val = f_euler_lin.subs( dict(zip(ub, x.ub_val)))
        x.sol.f_euler_lin_val = f_euler_lin_val[0]
        x.sol.f_euler_lin = f_euler_lin[0]

        x.sol.A = f_euler_lin_val.jacobian(xks)
        x.sol.B = f_euler_lin_val.jacobian(uks)
        x.sol.d = f_euler_lin_val.subs( dict(zip(xks+ uks, (0,0) ) ))

        f_lin = line(f, xs, us, xb, ub)
        x.f_lin_val = f_lin.subs(dict(zip(ub, x.ub_val)))
        # x.f_lin = x.f_lin_val[0]
        # sym.Symbol('x(t)')
        x.Ap = x.f_lin_val.jacobian(xs)
        x.Bp = x.f_lin_val.jacobian(us)
        x.dp = x.f_lin_val.subs( dict(zip(xs+ us, (0,0) ) ))

        eAdt = sym.exp( self.fixf(x.Ap * dt) )
        v = eAdt * sym.Matrix(xks) + 1/self.fixf(x.Ap)[0] * ( eAdt[0] - 1 ) * (x.Bp @ sym.Matrix(uks) + sym.Matrix(x.dp) )
        # v[0]
        sym.latex(v)
        x.f_lin_EI = v[0].simplify()
        if len(x.ub_val) == 1:
            x.ub_val = x.ub_val[0]
        a = 234
        return x

    def fixf(self, eq):
        from sympy import Dummy

        # def flint(eq):
        """convert floats that are ints to ints"""
        reps = {}
        e = eq.replace(lambda x: x.is_Float and x == int(x), lambda x: reps.setdefault(x, Dummy()))
        return e.xreplace({v: int(k) for k, v in reps.items()})


