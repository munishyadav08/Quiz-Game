print("Welcome to Quiz Game")
playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay Nice! Let's Play :)")

score = 0

questions = [
    {"question": "String is a data type?", "answer": "yes"},
    {"question": "Is Python a statically-typed language?", "answer": "no"},
    {"question": "Does Python support object-oriented programming?", "answer": "yes"},
    {"question": "Can you use the break statement in a for loop in Python?", "answer": "yes"},
    {"question": "Is Python a compiled language?", "answer": "no"}
]

for question in questions:
    answer = input(question["question"] + " yes or no ")
    if answer.strip().lower() == question["answer"]:
        print('CORRECT!')
        score += 1
    else:
        print('INCORRECT! ')

print("Your score is", score)
print("Your score is", (score / len(questions)) * 100, "%")
