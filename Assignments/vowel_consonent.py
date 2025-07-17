'''
Question 5: Take a character from user e.g. a, b, ........ and print whether its a vowel or consonent

'''

char = str(input("Provide a character :"))
# print(char)
# print(type(char))
#
# if char == "a" or "e" or "i" or "o" or "u": # does not work as expected in Python. This is because "e" (a non-empty string) is always truthy, so the condition will always evaluate to True, regardless of char.
#     print("Its a vowel !")
# else:
#     print("Its a consonent ")


# if char.lower() in "aeiou":
#     print("Its a vowel!")
# else:
#     print("Its a consonant")

if char.isalpha():
    print("its an alphabet")
    if char.lower() in "aeiou":
        print("and its a vowel !")
    else:
        print("and its a consonant ")
else:
    print("Its not an alphabet")