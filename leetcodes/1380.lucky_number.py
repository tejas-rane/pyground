class Solution:
    def luckyNumbers (self, matrix):
        minimum = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current_col = [row[j] for row in matrix]
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(current_col):
                    minimum.append(matrix[i][j])
                    break
        return minimum
s= Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))