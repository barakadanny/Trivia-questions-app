from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

# =========== API =========== #
parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean"
}

response = requests.get(question_data, params=parameters)
data = response.json()

question_bank = []
for question in data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
