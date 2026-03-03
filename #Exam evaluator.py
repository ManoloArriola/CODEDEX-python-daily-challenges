correct_answers = ["a", "a", "b", "c", "a"]

questions = [
    "1. Question: a) option a, b) option b, c) option c: ",
    "2. Question: a) option a, b) option b, c) option c: ",
    "3. Question: a) option a, b) option b, c) option c: ",
    "4. Question: a) option a, b) option b, c) option c: ",
    "5. Question: a) option a, b) option b, c) option c: "
]

user_answers = []

for question in questions:
    while True:
        answer = input(question).lower()
        if answer in ["a", "b", "c"]:
            user_answers.append(answer)
            break
        else:
            print("Invalid option. Please enter a, b, or c.")

def evaluate_exam(correct, user):
    score = sum(c == u for c, u in zip(correct, user))
    return score

score = evaluate_exam(correct_answers, user_answers)
percentage = (score / len(correct_answers)) * 100

print("\n--- Results ---")
print(f"Score: {score}/{len(correct_answers)}")
print(f"Percentage: {percentage:.2f}%")

print("\nReview:")
for i, (c, u) in enumerate(zip(correct_answers, user_answers), start=1):
    if c != u:
        print(f"Question {i}: Correct answer was '{c}', you answered '{u}'")