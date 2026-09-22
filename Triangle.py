
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("NOT A TRIANGLE")
else:
    if a == b == c:
        print("EQUILATERAL")
    elif a == b or a == c or b == c:
        print("ISOSCELES")
    else:
        print("SCALENE")