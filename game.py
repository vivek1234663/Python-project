import time

quiz_questions = [
    {
        "question": "1.What is the capital of india?",
        "options": ["A. Lucknow", "B. London", "C. New Delhi", "D. Dehradun"],
        "answer": "C"
    },
    {
        "question": "2.Which animal is bird?",
        "options": ["A. Tiger", "B. peacock", "C. Lion" ,"D. Monkey"],
        "answer": "B"
    },
    {
        "question": "3.Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "4.What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Shark"],
        "answer": "B"
    },
    {
        "question": "5.Which country recently hosted the 2024 Summer Olympics?",
        "options": ["A. Paris","B. Bijing","C. Rio de janerio","D. Tokyo"],
        "answer": "A"
    },
    {
        "question": "6.What is the national animal of india?",
        "options": ["A. Horse","B. Elephant","C. Monkey","D. Tiger"],
        "answer": "D"
    },
    {
        "question": "7.What is the national currency of india?",
        "options": ["A. inr","B. Yen","C. dollar","D. euro"],
        "answer": "A"
    },
    {
        "question": "8.Which festival is the colors of Lights?",
        "options": ["A. Sankranti","B. Holi","C. Diwali","D. Pongal"],
        "answer": "C"
    },
]

def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

def get_user_answer():
    while True:
        user_answer = input("your answer is(A/B/C/D): ").strip().upper()
        if user_answer in ["A","B","C","D"]:        
            return user_answer
        else:
            print("Invalid input. Please enter A,B,C or D.")

def run_quiz():
    score = 0
    total_questions = len(quiz_questions)

    print("Welcome to the Quiz Game!")
    print(f"You will be asked {total_questions} questions. Let's begin!\n")
    time.sleep(2)

    for question in quiz_questions:
        display_question(question)
        user_answer = get_user_answer()
        correct_answer = question["answer"]

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")
        time.sleep(1)

    print("Quiz ended!")
    print(f"Your final score is {score}/{total_questions}.")

    if score == total_questions:
        print("Congratulations! You got all questions right!") 
    elif score >= total_questions / 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    run_quiz()