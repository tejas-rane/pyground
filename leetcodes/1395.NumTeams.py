class Solution:
    def numTeams(self, rating):
        count = 0
        size = len(rating)
        for i in range(0, size-2):
            for j in range(i+1,size-1):
                for k in range(j+1,size):
                    if(rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        count +=1
        return count

s = Solution()

print(s.numTeams([2,5,3,4,1]))
print(s.numTeams([1,2,3,4]))