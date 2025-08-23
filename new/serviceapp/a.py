# print("hello")
# a="bbba"
# if a==a[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
def isPalindrome(s):
    return s == s[::-1]

s="bbba"
ans=isPalindrome(s)
print(ans)



a= int(input("enter a number"))
b= int(input("enter a number")) 
c= int(input("enter a number"))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")