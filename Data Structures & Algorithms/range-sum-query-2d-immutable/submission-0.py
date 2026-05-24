# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                sum += self.matrix[row][col]
        return sum

"""
- Given a 2D matrix and you have to handle multiple queries.
- Calculate the sum of the elements of the matrix inside the rectangle defined
by upper left corner (row1, col1) and lower right corner (row2, col2).
- Row 1 is index 0, and Col 1 is also index 0.
"""