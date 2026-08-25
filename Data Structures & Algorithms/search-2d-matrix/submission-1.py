class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        TARGET_ROW = -1

        for row in range(ROW):
            if (matrix[row][0] <= target and matrix[row][COL - 1] >= target):
                TARGET_ROW = row
                break;
        else:
            return False
        
        left = 0
        right = COL - 1
        while (left <= right):
            mid = (left + right) // 2
            if (matrix[TARGET_ROW][mid] == target):
                return True
            elif (matrix[TARGET_ROW][mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return False