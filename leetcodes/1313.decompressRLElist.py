class Solution:
    def decompressRLElist(self, nums):
        out = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            for i in range(0, freq):
                out.append(val)
        return out


s = Solution()
print(s.decompressRLElist([1, 2, 3, 4, 6, 7, 1, 3, 3, 1]))
