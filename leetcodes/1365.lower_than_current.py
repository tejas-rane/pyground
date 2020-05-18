def smallerNumbersThanCurrent(nums):
    out = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        out.append(count)
    return out


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
