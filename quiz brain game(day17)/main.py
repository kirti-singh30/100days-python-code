from quention_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q1 = item["text"]
    a1 = item["answer"]
    old_q = Question(q1,a1)
    question_bank.append(old_q)

quiz = QuizBrain(question_bank)
end = True
while end:
    #questions = quiz.still_has_question()
    if quiz.still_has_question():
        quiz.next_question()
    else:
        end = False
print("you have completed the quiz")
print(f"your final score was {quiz.score}/{quiz.question_number}")