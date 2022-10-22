text = input()

sym_count = 0
word_count = 0


for symbol in text:
    if symbol == ' ':
        if sym_count == 5:   # if sixth symbol is ' '
            word_count += 1  # add one to word counter

        sym_count = 0        # then reset word counter
    else:
        sym_count += 1


print(word_count)
