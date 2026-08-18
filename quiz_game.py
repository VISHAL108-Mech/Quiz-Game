"""This is the main script for the quiz game. It imports the necessary
classes and data, creates a list of Question objects, initializes the
QuizBrain class, and runs the quiz game loop until all questions have been
answered. Finally, it prints the final score."""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question = data["question"]
    answer = data["correct_answer"]
    questions = Question(question, answer)
    question_bank.append(questions)

quiz = QuizBrain(question_bank)

while quiz.question_remaining():
    quiz.next_question()

print("Quiz Completed.")
print(f"Final Score: {quiz.score}/{quiz.question_number}")
