def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5, 6]

for item in map(square, my_nums):
    print(item)

# more pythonic way
print(list(map(square, my_nums)))
