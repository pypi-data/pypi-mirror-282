from exam_generator.exam import Question, ProgrammingQuestion
from types import SimpleNamespace


class ProgramDP02(ProgrammingQuestion):
    program_file = "question_inventory.py"
    # def __init__(self, seed):
    #     super().__init__(seed)
    def generate(self):
        x = SimpleNamespace()
        import irlc
        import time
        # print(irlc.__path__)
        # print("Hello there.")
        time.sleep(1)
        from irlc.exam.exam2023spring.question_inventory import InventoryDPModelB
        model = InventoryDPModelB()
        pw = model.Pw(0, 0, 0)
        x.pw = pw
        # x.file = ''
        return x

