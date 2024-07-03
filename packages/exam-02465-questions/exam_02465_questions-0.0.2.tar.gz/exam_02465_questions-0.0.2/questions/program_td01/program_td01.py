from exam_generator.exam import Question, ProgrammingQuestion
from types import SimpleNamespace

class ProgramTD01(ProgrammingQuestion):
    program_file = "question_td0.py"
    def __init__(self, seed, **kwargs):
        super().__init__(seed, **kwargs)
    def generate(self):
        x = SimpleNamespace()
        x.file = ''
        return x
