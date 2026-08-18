""" This module contains the QuizBrain class, which manages the quiz questions
 and tracks the player's score."""

class QuizBrain:
    """This class represents the quiz brain, which manages the quiz questions
      and tracks the player's score."""

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def question_remaining(self):
        """This method checks if there are any remaining questions in the quiz.
        It returns True if there are more questions, and False otherwise."""

        return self.question_number < len(self.question_list)


    def next_question(self):
        """This method retrieves the next question from the question list, 
        prompts the user for an answer, and checks if the answer is correct. 
        It also updates the score and question number accordingly."""

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        """This method checks if the user's answer is correct. 
        It compares the user's answer with the correct answer, updates the score
        if the answer is correct, and provides feedback to the user."""
          
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")
