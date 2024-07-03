from exam_generator.exam import Question, ProgrammingQuestion
from types import SimpleNamespace
import numpy as np
import sympy as sym
from sympy import latex

class ProgramControl01(ProgrammingQuestion):
    program_file = "question_control.py"
    # def __init__(self, seed):
    #     super().__init__(seed)
    def generate(self):
        x = SimpleNamespace()
        from irlc.exam.exam2024spring.question_control import Simulation

        xx = sym.Symbol('x')
        uu = sym.Symbol('u')
        m = Simulation()
        y = m.sym_f([xx], [uu], sym.Symbol('t'))
        f = latex(y[0])
        x.f = f
        x.x0 = 0

        # from irlc.exam.exam2023spring.question_inventory import InventoryDPModelB
        # model = InventoryDPModelB(p_burglary=None)

        # pw = model.Pw(0, 0, 0)
        # x.pw = pw
        #
        # from irlc.exam.exam2023spring.question_lqr import getAB
        # A, B, d = getAB(33)
        # print(A)
        # x.file = ''
        return x

