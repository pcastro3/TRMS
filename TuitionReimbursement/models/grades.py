class Grades:

    def __init__(self, grade='', letter='', pass_fail=''):
        self.grade = grade
        self.letter = letter
        self.pass_fail = pass_fail

    def __repr__(self):
        return str({
            'grade': self.grade,
            'letter': self.letter,
            'pass_fail': self.pass_fail
        })

    def json(self):
        return {
            'grade': self.grade,
            'letter': self.letter,
            'passFail': self.pass_fail
        }

