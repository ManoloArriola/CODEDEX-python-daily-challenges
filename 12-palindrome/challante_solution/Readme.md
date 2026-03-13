# Palindrome Checker

This challenge focuses on detecting whether a sequence reads the same forwards and backwards.

A **palindrome** is a word, phrase, or number that remains the same when reversed.

Examples:

racecar  
level  
2002  
Was it a car or a cat I saw

Spaces and capitalization should be ignored.

---

## Problem

Given a string, determine whether it is a palindrome.

Rules:

- Ignore spaces
- Ignore capitalization
- Assume the input contains only letters and numbers

Return:

- `True` if the sequence is a palindrome
- `False` otherwise

---

## Example

Input: Was it a car or a cat I saw


Output:


True


---

## Python Solution

```python
def check_palindrome(sequence):

    cleaned = sequence.lower().replace(" ", "")

    return cleaned == cleaned[::-1]
