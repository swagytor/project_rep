class Question:
    POINTS_PER_ANSWER = 10

    def __init__(self, question, difficult, answer):
        self.question = question
        self.difficult = int(difficult)
        self.answer = str(answer)
        self.is_asked = False
        self.user_answer = None
        self.score_amount = self.difficult * Question.POINTS_PER_ANSWER

    def get_points(self):
        return self.score_amount

    def is_correct(self, user_answer):
        return self.answer == user_answer

    def build_question(self):
        return f'Вопрос: {self.question}\nСложность: {self.difficult}/5'

    def build_positive_feedback(self):
        return f'Ответ верный, получено {self.score_amount} баллов'

    def build_negative_feedback(self):
        return f'Ответ неверный, верный ответ {self.answer}'
