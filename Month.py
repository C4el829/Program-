month= int(input("month(1-12)="))
if month in (12,1,2):
    print("Uvul")
elif month in (3,4,5):
    print("Havar")
elif month in (6,7,8):
    print("Zun")
elif month in (9,10,11):
    print("Namar")
else:
    print("Invalid")