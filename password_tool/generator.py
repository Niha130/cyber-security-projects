def generate_wordlist(name, dob, pet):
    words = []

    base = [name, dob, pet]

    for item in base:
        words.append(item)
        words.append(item + "123")
        words.append(item + "@2024")
        words.append(item.capitalize())

    return list(set(words))
