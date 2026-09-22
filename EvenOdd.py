def is_even(n):
    return n % 2 == 0

n = int(input("Тоог оруулна уу: "))

if is_even(n):
    print(f"{n} нь тэгш тоо байна.")
else:
    print(f"{n} нь сондгой тоо байна.")
