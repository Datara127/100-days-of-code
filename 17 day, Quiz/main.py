from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)
for i in range(len(question_bank)):
    quiz.question_next()

print(f"Your final score was: {quiz.score}/{quiz.question_number}")

