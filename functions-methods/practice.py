import string


def ran_bool(num, low, high):
    return num in range(low, high)


def ran_check(num, low, high):
    if num in range(low, high):
        return 'YES'
    else:
        return 'NO'


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print(f'Upper case letters {d["upper"]}')
    print(f'lower case letters {d["lower"]}')


def unique_list(l):
    x = []
    for n in l:
        if n not in x:
            x.append(n)
    print(sorted(x))


def unique_quick(l):
    print(sorted(set(l)))


def palindrome(s):
    return s == s[::-1]


def ispangram(s):
    alphabets = set(string.ascii_lowercase)
    return alphabets <= set(s.lower())


print(ran_bool(3, 1, 10))
print(ran_check(3, 1, 10))
up_low('Hi, I am doing Great!')
unique_list([11, 44, 22, 66, 99, 5, 5, 5, 1, 1, 3, 3, 5, 5])
unique_quick([11, 44, 22, 66, 99, 5, 5, 5, 1, 1, 3, 3, 5, 5])
print(palindrome('helleh'))
print(ispangram('The quick brown fox jumps over the lazy dog'))
