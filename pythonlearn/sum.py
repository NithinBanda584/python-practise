a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>=b and a>=c:
    print(f"large digit is:",a)
elif b>=a and b>=c:
    print(f"large digit is:",b)
elif c>=a and c>=b:
    print(f"large digit is:",c)
