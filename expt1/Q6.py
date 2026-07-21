def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is Not a Prime Number")
