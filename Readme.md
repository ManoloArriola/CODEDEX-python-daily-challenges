# 01 - Wordle Guess

This folder contains two parts:

## challenge_solution
Original Codédex challenge solution:
Compare two strings and count how many characters match in the same position.

## real_app
A practical quiz evaluator built from the same comparison logic.

### Real-world idea
Instead of comparing letters, this app compares:
- correct answers
- user answers

using `zip()` to calculate the final score.

### Files
- `questions.json` → stores the quiz questions and correct answers
- `main.py` → runs the quiz app

### Run the app
```bash
python main.py
