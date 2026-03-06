# 01 - Wordle Guess

This folder contains two implementations inspired by the Codédex Day 1 challenge.

## challenge_solution
Original challenge solution:
Compare two strings and count how many characters match in the same position.

## real_app
A practical quiz evaluator built from the same core logic.

Instead of comparing letters, this version compares:
- correct answers
- user answers

using `zip()` to calculate the final score.

## Files
- `challenge_solution/main.py` → original challenge solution
- `real_app/questions.json` → quiz questions and correct answers
- `real_app/real_app.py` → interactive quiz application

## Concepts practiced
- string comparison
- JSON file handling
- user input validation
- `zip()` for parallel comparison
- modular Python functions
- relative file paths with `os`

## How to run
From the `real_app` folder:

```bash
python real_app.py