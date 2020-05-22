
def kidsWithCandies(candies, extraCandies):
    out = []
    max_count = max(candies)
    for num in candies:
        if num + extraCandies >= max_count:
            out.append(True)
        else:
            out.append(False)
    return out


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
