from exam_generator.exam import Question, ProgrammingQuestion
from types import SimpleNamespace

class ProgramLQR01(ProgrammingQuestion):
    program_file = "question_lqr.py"
    # def __init__(self, seed):
    #     super().__init__(seed)
    def generate(self):
        x = SimpleNamespace()

        # from irlc.exam.exam2023spring.question_inventory import InventoryDPModelB
        # model = InventoryDPModelB()

        # pw = model.Pw(0, 0, 0)
        # x.pw = pw

        from irlc.exam.exam2023spring.question_lqr import getAB
        A, B, d = getAB(33)
        # print(A)

        return x

