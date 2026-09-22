total = float(input("niit une"))

if total > 100000:
    discount = 0.10
elif total >= 50000:
    discount = 0.05
else:
    discount = 0.0

pay = total * (1 - discount)
print("hungulult:", discount*100, "%")
print("tuluh:", pay)