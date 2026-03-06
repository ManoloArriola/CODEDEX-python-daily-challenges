def wordle_guess(secret, guess):
    """
    Counts how many characters match in the exact same position.
    Both inputs are expected to have the same length (5 in the challenge).
    """
    count = 0

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            count += 1

    return count


if __name__ == "__main__":
    secret = input("Secret word (5 letters): ").strip().upper()
    guess = input("Your guess (5 letters): ").strip().upper()

    # Basic validation (optional, but helpful)
    if len(secret) != len(guess):
        print("Error: secret and guess must be the same length.")
    else:
        result = wordle_guess(secret, guess)
        print(f"Matches in the same position: {result}")
