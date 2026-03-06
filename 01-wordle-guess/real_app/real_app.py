import json
import os

def load_questions(filename):
    """
    Load questions from a JSON file.

    Parameters:
        filename (str): Path to the JSON file.

    Returns:
        list: A list of question dictionaries.
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def ask_questions(questions):
    """Ask each question to the user and collect their answers."""
    user_answers = []

    for i, item in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {item['question']}")

        for key, value in item["options"].items():
            print(f"  {key}) {value}")

        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in item["options"]:
                user_answers.append(answer)
                break
            else:
                print("Invalid option. Please enter a, b, or c.")

    return user_answers


def evaluate_answers(questions, user_answers):
    """Compare user answers with correct answers and calculate score."""
    correct_answers = [item["correct"] for item in questions]
    score = sum(correct == user for correct, user in zip(correct_answers, user_answers))
    return score


def show_results(questions, user_answers, score):
    """Display the final score and a review of each question."""
    total = len(questions)
    percentage = (score / total) * 100

    print("\n--- Results ---")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")

    print("\n--- Review ---")
    for i, (item, user) in enumerate(zip(questions, user_answers), start=1):
        correct = item["correct"]
        if user == correct:
            print(f"Question {i}: Correct")
        else:
            print(f"Question {i}: Incorrect | Your answer: {user} | Correct answer: {correct}")


def main():
    """Main program flow."""
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "questions.json")

    questions = load_questions(file_path)
    user_answers = ask_questions(questions)
    score = evaluate_answers(questions, user_answers)
    show_results(questions, user_answers, score)


if __name__ == "__main__":
    main()