hours = int(input("Enter worked hours"))
rate = int(input("Enter hours rate"))
if hours < 0 or rate < 0:
    print("Invalid Input")
else:
    if hours <= 40:
        salary = hours * rate
    else:
        salary = 40 * rate + (hours - 40) * rate * 1.5
    print("salary=",salary)