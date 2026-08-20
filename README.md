# 🧠 Quiz Game — Python

A modular **Python Quiz Game** that presents a series of questions to the user, evaluates their answers, tracks the score, and displays the final result. The project uses **Object-Oriented Programming (OOP)** and custom Python modules to keep the code organized, reusable, and maintainable.

---

## 📌 Project Overview

This project is a command-line quiz application built using Python. Questions and answers are stored separately in a data module, converted into `Question` objects, and passed to the `QuizBrain` class, which manages the quiz flow and score tracking.

The project focuses on applying **OOP, modular programming, data structures, loops, functions, and conditional logic** to build a complete interactive application.

---

## ✨ Features

* 🧠 Multiple-choice/True-False style quiz questions
* 📚 Question bank created from structured data
* 🎯 Object-oriented quiz management
* 📊 Real-time score tracking
* 🔄 Automatically moves through remaining questions
* ✅ Evaluates user answers
* 🏁 Displays the final score after completing the quiz
* 🧩 Separates data, question models, and game logic into different modules
* 💻 Simple command-line interface

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Programming Paradigm:** Object-Oriented Programming (OOP)
* **IDE:** Visual Studio Code
* **Interface:** Command Line / Terminal

### Python Modules

* Custom `question_model` module
* Custom `quiz_brain` module
* Custom `data` module

No external libraries are required.

---

## 🧠 Python Concepts Demonstrated

### 🏗️ Object-Oriented Programming

* Classes
* Objects
* Constructors
* Object attributes
* Object methods
* Encapsulation
* Creating and managing objects

The project uses a `Question` class to represent individual questions and a `QuizBrain` class to manage the quiz.

---

### 📦 Modular Programming

The project separates different responsibilities into independent Python files:

* `question_model.py` → Defines the `Question` class
* `data.py` → Stores the quiz question data
* `quiz_brain.py` → Contains the main quiz logic
* `quiz_game.py` → Main program that connects everything together

This makes the application easier to understand, maintain, and extend.

---

### 📚 Data Structures

* Lists
* Dictionaries
* List of dictionaries
* Objects stored inside lists

The question data is converted into `Question` objects and stored inside a `question_bank` list.

---

### 🔄 Control Flow

* `for` loops
* `while` loops
* Conditional statements
* Boolean expressions
* Comparison operators

The quiz continues running while questions remain unanswered.

```python
while quiz.question_remaining():
    quiz.next_question()
```

---

### 🧩 Functions & Methods

* Defining functions
* Calling methods
* Passing arguments
* Returning values
* Reusable program logic

---

### ⌨️ User Interaction

* User input
* Answer evaluation
* Dynamic score updates
* Final score calculation

---

### 📊 Score Management

The `QuizBrain` object keeps track of:

* Current question number
* Total questions
* User's score
* Remaining questions

The final score is displayed after all questions have been answered.

---

## 🔧 How It Works

The application follows this workflow:

```text
Question Data
     ↓
data.py
     ↓
Create Question Objects
     ↓
question_model.py
     ↓
Question Bank
     ↓
QuizBrain
     ↓
Display Questions
     ↓
Get User Answer
     ↓
Check Answer
     ↓
Update Score
     ↓
Next Question
     ↓
Final Score
```

---

## 📂 Project Structure

```text
Quiz Game/
│
├── data.py
├── question_model.py
├── quiz_brain.py
├── quiz_game.py
├── README.md
└── __pycache__/
```

### File Responsibilities

| File                | Purpose                                             |
| ------------------- | --------------------------------------------------- |
| `data.py`           | Contains the quiz questions and correct answers     |
| `question_model.py` | Defines the `Question` class                        |
| `quiz_brain.py`     | Handles quiz logic, questions, answers, and scoring |
| `quiz_game.py`      | Main entry point that initializes and runs the quiz |
| `README.md`         | Project documentation                               |

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/VISHAL108-Mech/Quiz-Game.git
```

### 2. Navigate to the project directory

```bash
cd quiz-game
```

### 3. Run the game

```bash
python quiz_game.py
```

The quiz will start in the terminal.

---

## 🎯 Learning Outcomes

Building this project helped me strengthen my understanding of:

* Object-Oriented Programming in Python
* Creating and using custom classes
* Working with objects
* Modular programming
* Separating data from application logic
* Lists and dictionaries
* Loops and conditional statements
* Functions and methods
* User input handling
* Score tracking
* Building reusable and maintainable code

---

## 💼 Portfolio Highlights

This project demonstrates practical experience with:

* 🐍 **Python Programming**
* 🏗️ **Object-Oriented Programming**
* 🧩 **Modular Programming**
* 📚 **Data Structures**
* 🔄 **Control Flow**
* 🎯 **Game Logic**
* 📊 **State & Score Management**
* 🧠 **Problem Solving**
* 🧹 **Code Organization**
* 💻 **Command-Line Applications**

The project also demonstrates an understanding of how to break a larger application into **separate classes and modules**, rather than keeping all functionality inside a single Python file.

---

## 🔮 Future Improvements

* Add multiple-choice answer options
* Add different quiz categories
* Add difficulty levels
* Add a timer for each question
* Store high scores using files or a database
* Add a graphical user interface using Tkinter
* Add randomized question order
* Add question difficulty tracking
* Add detailed performance statistics
* Add unit tests for the quiz logic

---

## 📬 Contact

**Developer:** Vishal Yadav

**GitHub:**  https://github.com/VISHAL108-Mech

**LinkedIn:**  www.linkedin.com/in/vishal-yadav-2a91a7428

**Email:** vy4122000@gmail.com

---

## ⭐ Project Purpose

This project was built as part of my journey toward developing stronger **Python programming, Object-Oriented Programming, and software development skills** through practical, hands-on projects.

---

## 📸 Screenshot

### 🎮 Quiz Gameplay

<img width="1010" height="449" alt="Screenshot 2026-08-20 182205" src="https://github.com/user-attachments/assets/32be5082-f602-4cf5-bbe1-b6742964ca46" />


---

### 🏷️ Topics

`#Python` `#PythonProject` `#OOP` `#ObjectOrientedProgramming` `#PythonProgramming` `#Programming` `#QuizGame` `#GameDevelopment` `#Functions` `#Classes` `#Objects` `#DataStructures` `#GitHub` `#Portfolio` `#ProblemSolving`
