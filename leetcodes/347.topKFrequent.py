def topKFrequent(nums, k):
    dict = {}
    list_dict = []
    for i in nums:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    for key, value in sorted(dict.items(), key=lambda x: x[1]):
        list_dict.append(key)

    return list_dict[-k:]


print(topKFrequent([1, 1, 1, 2, 2, 3, 4, 5, 6,
                    7, 4, 3, 2, 4, 5, 6, 3, 2, 3, 4, 5, 6], 3))
print(topKFrequent([1], 1))
