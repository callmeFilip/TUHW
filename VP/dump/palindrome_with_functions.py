# funkciq proverqvashta dali vuvedanata ot potrebitel informaciq (text/chislo)
# e palindrom, ako e palindrom vrushta suobshtenie

def isPalindrome(text):
    palindrome = True
    for i in range(len(text)):
        if text[i] != text[-(i + 1)]:
            palindrome = False

    return 'Is palindrome' if palindrome else 'Is not palindrome'


msg = input('Input information: ')

print(isPalindrome(msg))
