def anagram(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    print(sorted(s1) == sorted(s2))


def anagram2(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    if len(s1) != len(s2):
        return False

    # counting dictionary algorithm
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


anagram('clint eastwood', 'old west action')

anagram('clint eastwood', 'ofd west action')

print(anagram2('clint eastwood', 'old west action'))

print(anagram2('clint eastwood', 'ofd west action'))
