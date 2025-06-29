def make_abbreviation(phrase):
    words = phrase.split()
    abbreviation = ''.join(word[0] for word in words if word[0].isalpha())
    return abbreviation.upper()

user_input = input("Введите фразу: ")
result = make_abbreviation(user_input)
print("Аббревиатура:", result)
