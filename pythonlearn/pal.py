a=str(input())
if a==a[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
print("palindrome" if (a:=input())==a[::-1] else "not a palindrome")