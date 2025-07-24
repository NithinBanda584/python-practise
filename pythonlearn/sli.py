a=int(input("enter a number:"))
last=a%10
first=a
while first>=10:
    first//=10
print(first+last)