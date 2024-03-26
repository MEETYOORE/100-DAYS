class QuizzBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}){cur_question.text} True/False: ")
        self.check_answer(user_answer, cur_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def check_answer(self, user, correct):
        if user.lower() == correct.lower():
            print(f"You got it Right🥳! \nThe correct answer was {correct}")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
            print()

        else:
            print(f"You got it Wrong😔! \nThe correct answer was {correct}")
            print(f"Your current score is {self.score}/{self.question_number}")
            print()
