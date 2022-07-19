#5. Design a code which will find the given number is Palindrome number or not.
# Hint: Use built-in functions of string.

num=int(input("Enter number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")