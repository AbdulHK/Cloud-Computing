def isPalindrome():
    string1 = input('Enter a string: ')
    string2 = string[::-1]
    if string1 == string2:
        return 'It is a palindrome'
    return 'It is not a palindrome'

isPalindrome()