def transltor(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation = "D"
            else:
                translation = translation + "d"
        else:
            translation = translation + letter
    return translation


print(transltor(input("Enter Phrase: ")))
