class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            mid = left + (right-left)//2
            mid_element = matrix[mid//col][mid%col] 
            if(mid_element == target):
                return True
            elif mid_element > target:
                right = mid-1
            elif mid_element < target:
                left = mid +1
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))