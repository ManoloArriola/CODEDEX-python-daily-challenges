import json
import os


def check_url(address):
    if address.startswith("http://"):
        domain = address[7:]
    elif address.startswith("https://"):
        domain = address[8:]
    else:
        return "invalid"

    if "." not in domain:
        return "invalid"

    for char in domain:
        if not (char.isalnum() or char == "-" or char == "."):
            return "invalid"

    return "valid"


def load_urls(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def classify_urls(urls):
    valid_urls = []
    invalid_urls = []

    for url in urls:
        if check_url(url) == "valid":
            valid_urls.append(url)
        else:
            invalid_urls.append(url)

    return valid_urls, invalid_urls


def main():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "urls.json")

    urls = load_urls(file_path)
    valid_urls, invalid_urls = classify_urls(urls)

    print("=== URL Validation Report ===")
    print(f"Total URLs: {len(urls)}")
    print(f"Valid URLs: {len(valid_urls)}")
    print(f"Invalid URLs: {len(invalid_urls)}\n")

    print("Valid:")
    for url in valid_urls:
        print(f"- {url}")

    print("\nInvalid:")
    for url in invalid_urls:
        print(f"- {url}")


if __name__ == "__main__":
    main()
