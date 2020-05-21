class Solution:
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for num in row[::-1]:
                if num < 0:
                    count += 1
                else:
                    break
        return count

s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))