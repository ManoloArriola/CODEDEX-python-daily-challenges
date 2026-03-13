def check_palindrome(sequence):
    cleaned = sequence.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def analyze_dataset(words):

    results = {}

    for word in words:
        results[word] = check_palindrome(word)

    return results
