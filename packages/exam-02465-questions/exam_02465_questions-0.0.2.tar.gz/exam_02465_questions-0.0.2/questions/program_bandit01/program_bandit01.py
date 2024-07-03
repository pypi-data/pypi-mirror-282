from exam_generator.exam import Question, ProgrammingQuestion
from types import SimpleNamespace

class ProgramBandit01(ProgrammingQuestion):
    program_file = "question_bandit.py"
    def __init__(self, seed):
        super().__init__(seed)
    def generate(self):
        x = SimpleNamespace()

        x.file = ''
        return x
