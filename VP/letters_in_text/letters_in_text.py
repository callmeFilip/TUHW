FIRST_LETTER_CAPITAL = ord('A')
FIRST_LETTER_LOWERCASE = ord('a')
LAST_LETTER_CAPITAL = ord('Z')
LAST_LETTER_LOWERCASE = ord('z')


def count_letters(text):
    counter = 0
    for i in text:
        numeric_representation = ord(i)
        if (numeric_representation > FIRST_LETTER_CAPITAL and numeric_representation < LAST_LETTER_CAPITAL) or (numeric_representation > FIRST_LETTER_LOWERCASE and numeric_representation < LAST_LETTER_LOWERCASE):
            counter += 1

    return counter


text = str(input())

print(count_letters(text))
