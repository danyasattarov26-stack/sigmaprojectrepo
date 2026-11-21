import time
questions = {
    "How many planets exist in the solar system?": "8",
    "What's the capital of france": "Oui Oui Oui, it is paris"
}
score = 0
for q, a in questions.items():
    start_time = time.time()
    user_answer = input(q + " ")
    end_time = time.time()
    if round(end_time - start_time, 1) > 5:
        print("You didnt make it in 5 seconds")
        user_answer = "WRONG"
    print(f"Your time is {round(end_time - start_time, 1)} seconds")
    if user_answer.lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print(f"Your result is: {score} out of {len(questions)}")