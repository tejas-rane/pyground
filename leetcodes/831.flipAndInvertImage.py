class Solution:
    def flipAndInvertImage(self, A):
        for l in A:
            l.reverse()
            for i in range(0,len(l)):
                l[i] ^= 1
        return A

s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))