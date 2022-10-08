def count_letters(text):
    count = 0

    for letter in text:
        if letter.isalpha():
            count += 1
    return count


text = input()

print(count_letters(text))
