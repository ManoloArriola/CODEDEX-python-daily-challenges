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
