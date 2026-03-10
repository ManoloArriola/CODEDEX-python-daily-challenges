import string
def find_unique_words(transcript):
    transcript = transcript.lower()

    for p in string.punctuation:
      transcript = transcript.replace(p, "")

    words = transcript.split()

    unique_words = set(words)

    return len(unique_words)
