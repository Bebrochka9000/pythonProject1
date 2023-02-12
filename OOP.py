# class Emploe:
#     '''какие-то комменты'''
#     def __init__(self, f,i,o):
#         self.f = f
#         self.i = i
#         self.o = o
#
#     def __repor__(self):
#         return self.f, self.i[0], self.o[0]
#
#
# emploes = [
#     Emploe("Тимофеевна", "Влада", "Сергеевна"),
#     Emploe("Кулакова", "Евгения", "Романовна"),
#     Emploe("Вольнов", "Александр", "Семёнов")
#
# ]
# for i in range(len(emploes)):
#     print(' '.join(emploes[i].__repor__()))


class Question():
    def __init__(self, question_text, question_diff, question_answer):
        self.question_text = question_text
        self.question_diff = question_diff
        self.question_answer = question_answer

        self.is_asked = False
        self.user_answer = None
        self.points = int(self.question_diff) * 10

    def get_point(self):
        return self.points

    def is_correct(self):
        if self.question_answer == self.user_answer:
            return True
        else:
            return False

    def build_question(self):
        return "Вопрос", self.question_text, "\n Сложность", self.question_diff, '/5'

    def positive_feedback(self):
        return "Ответ верный, вы получаете", self.points, "баллов"

    def negative_feedback(self):
        return "Ответ неверный, верный ответ", self.question_answer


data = {
    "q": "How many days do we have in the week",
    "d": "1",
    "a": "9"
}




def draw_table(question):
    for categori_name, categori_question in question.items():
        print(categori_name.ljust(15), end="")
        for price, question_data in categori_question.items():
            ask = question_data['asked']
            if not ask:
                print(price, " ", end="")
            else:
                print(" ", end="    ")
        print()