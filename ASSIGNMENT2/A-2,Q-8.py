import random as r

num = r.random()
print(num)

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Random choice from list:", r.choice(lst))
print("Random choice from another list:", r.choice([1, 2, 3, 4, 5, 6, 7]))

print("Random number using randrange:", r.randrange(10, 50, 3))

print("Another random number:", r.random())
 
r.seed(5)
print("After seed:", r.random())
