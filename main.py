questions = {
    "How many planets exist in the solar system?": "8",
    "What's the capital of france": "Oui Oui Oui, it is paris"
}
score = 0
for q, a in questions.items():
    user_answer = input(q + " ")
    if user_answer.lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print(f"Your result is: {score} out of {len(questions)}")