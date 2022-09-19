def isPalindrome(s):
    return s== s[::-1]
string = input()
only_alpha=""
for char in string:
    if char.isalpha():
        only_alpha+=char
ans=isPalindrome(only_alpha.lower())

if ans:
    print("Yes")
else:
    print("No")
