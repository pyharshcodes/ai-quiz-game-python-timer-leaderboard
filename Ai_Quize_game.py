import time
import random

#Sample question
questions=[
    {
        "question":"What is the capital of France?",
        "options":["A. Berlin", "B. Paris" , "C. Rome", "D.Madrid"],
        "answer": "B"
    },
    {
        "question": "What is the output of 3*1**3?",
        "options": ["A. 27", "B. 3", "C. 1", "D. 4"],
        "answer": "B"
    },
    {
        "question": "Which language you use in web page?",
        "options": ["A. Python", "B. JavaScript", "C. Java", "D. All"],
        "answer": "D"
    },
    {
        "question": "Who developed python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    }
]

score_file="score.txt"

def show_menu():
    print("Welcome to AI Quize Game")
    print("1. Start Quiz")
    print("2. View Leaderboard")
    print("3. Exit")

def start_quiz(username):
    score=0
    random.shuffle(questions)
    for q in questions:
        print(f"\n{q['question']}")
        for opt in q['options']:
            print(opt)
        
        start_time = time.time()
        answer = input("\n Your answer (A/B/C/D): ").strip().upper()
        elapsed_time=time.time()-start_time
        
        if elapsed_time > 10:
            print("Time is up! No point add.")
        elif answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")

    print(f"\n{username}, your final score: {score}/{len(questions)}")
    save_score(username,score)

def save_score(username, score):
    with open(score_file, "a") as f:
        f.write(f"{username} - {score}\n")
    print("Score saved to leaderboard!")

def view_leaderboard():
    print("\n Leaderboard:")
    try:
        with open(score_file, "r") as f:
            scores = f.readlines()
        scores = sorted(scores, key=lambda x:int(x.split("-")[-1].strip()),reverse=True)
        for line in scores[:5]:
            print(line.strip())
    except FileNotFoundError:
        print("No scores found yet.")

while True:
    show_menu()
    choice=input("\nEnter your choice (1/2/3): ").strip()
    if choice=='1':
        name=input("\nEnter your name:")
        start_quiz(name)
    elif choice=='2':
        view_leaderboard()
    elif choice=='3':
        print("\n Thanks for playing! Bye.")
        break
    else:
        print("Invalid choice. Please try again.")
