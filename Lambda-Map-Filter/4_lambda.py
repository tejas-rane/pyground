
my_nums = [1, 2, 3, 4, 5, 6]

# Lambda way to square
print(list(map(lambda num: num ** 2, my_nums)))

my_nums = [0, 1, 2, 3, 4, 5, 6]
# Lambda way to check_even
print(list(filter(lambda num: num % 2 == 0, my_nums)))


names = ['Andy', 'Eve', 'Sallly']
# Lambda way to slice
print(list(map(lambda name: 'EVEN' if len(name) % 2 == 0 else name[0], names)))
