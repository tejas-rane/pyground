class Solution:
    def findDuplicates(self, nums):
        sorted_nums = sorted(nums)
        out = []
        for i in range(0,len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                out.append(sorted_nums[i])
        return out                   
        # dict = {}
        # out = []
        
        # for num in nums:
        #     if num in dict:
        #         dict[num] += 1
        #     else:
        #         dict[num] = 1
        # for num in dict:
        #     if dict[num] >1:
        #         out.append(num)
        # return out

s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))