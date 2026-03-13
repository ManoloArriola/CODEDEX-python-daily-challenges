```markdown
# Data Symmetry Analyzer

This tool analyzes text entries and determines whether they form palindromes.

It expands the original palindrome challenge into a practical data-processing utility.

---

## Features

- Loads multiple entries from a dataset
- Normalizes text
- Detects palindromes
- Generates a classification report

---

## Example Dataset


racecar
level
manolo
taco cat
12321
hello


Output:


racecar → palindrome
level → palindrome
manolo → not palindrome
taco cat → palindrome
12321 → palindrome
hello → not palindrome

---

## Example Implementation

```python
def check_palindrome(sequence):
    cleaned = sequence.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def analyze_dataset(words):

    results = {}

    for word in words:
        results[word] = check_palindrome(word)

    return results
