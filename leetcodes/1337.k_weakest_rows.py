class Solution:
    def kWeakestRows(self, mat,k):
        dict = {}
        out = []
        row_index = 0
        for row in mat:
            soldiers = 0
            for i in row:
                soldiers += i
            dict[row_index] = soldiers
            row_index += 1
        for key, value in sorted(dict.items(), key=lambda x : x[1] ):
            out.append(key)
        return out[:k]

s = Solution()
print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))