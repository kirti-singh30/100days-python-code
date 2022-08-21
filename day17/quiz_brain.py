class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_question(self):
        final = self.question_number < len(self.question_list)
        return final

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
         
        user_input = input(f"Q.{self.question_number} {question.txt} (True/False)?:").lower()
        self.check_answer(user_input,question.ans)

    def check_answer(self,user_input, correct_ans):
        if user_input == correct_ans.lower():
            self.score += 1
            print(f"you got this right.your score is {self.score} ")
        else:
            print(f"your answer is wrong.your score is {self.score} ")

        print(f"the right answer is {correct_ans}")
        print(f"your current score is {self.score}/{self.question_number} ")

