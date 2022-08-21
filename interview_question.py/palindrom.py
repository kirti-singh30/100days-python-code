def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input("what you want to check?")
#s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print(f"Yes,{s} is palindrom")
else:
    print(f"No,{s} is not palindrom")