def check_even(num):
    return num % 2 == 0

my_nums = [0, 1, 2, 3, 4, 5, 6]

print(list(filter(check_even,my_nums)))