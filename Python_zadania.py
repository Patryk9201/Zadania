
numbers = [1, 5, 2, 3, 1, 4, 5, 1, 2, 50, 42, 3, 4, 5, 6, 7, 8, 9, 2, 4, 65, 23, 5, 5]

numbers_sum = sum(numbers[5:15])
print("Sum of first ten elements starting from element five: ", numbers_sum)


pot = []
power_of_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in power_of_two:
    pot.append(2**i)
print(pot)

#List Comprehension
pot_two = [2**i for i in power_of_two]
print(pot_two)


users = [
    {"name": "Kamil","country": "Poland"},
    {"name": "John","country": "USA"},
    {"name": "Yeti"}
]

lst = [user for user in users if user.get("country") == "Poland"]
print(lst)

