class Solution:
    def minSetSize(self, arr):
        half_size = len(arr)/2
        out = []
        dict = {}
        total = 0
        for num in arr:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
        for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True):
            if total >= half_size:
                return len(out)
            else:
                total += value
                out.append(value)
        return 1

s = Solution()
print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(s.minSetSize([7,7,7,7,7,7]))
print(s.minSetSize([1,2,3,4,5,6,7,8,9,10]))