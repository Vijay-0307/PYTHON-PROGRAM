def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
s =input("ENnter a String:")
ans = isPalindrome(s)
if (ans):
    print("Palindrome")
else:
    print("Not a Palindrome")