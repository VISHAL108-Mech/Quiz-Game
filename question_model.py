""" This module contains the Question class, which represents a question in
 the quiz game."""
class Question:
    """This class represents a question in the quiz game. 
    It has two attributes: text and answer. 
    The text attribute stores the question text, while the answer attribute
    stores the correct answer to the question."""  

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
