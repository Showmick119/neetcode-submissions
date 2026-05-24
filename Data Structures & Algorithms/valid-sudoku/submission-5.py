class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            check = [0] * 10 # so we get index 1 to 9 (and not get cut off at 8)
            for col in range(cols):
                curr = board[row][col]
                if not curr.isdigit():
                    continue
                else:
                    curr = int(curr)
                check[curr] += 1
                if check[curr] > 1:
                    return False
        
        for col in range(cols):
            check = [0] * 10 # so we get index 1 to 9 (and not get cut off at 8)
            for row in range(rows):
                curr = board[row][col]
                if not curr.isdigit():
                    continue
                else:
                    curr = int(curr)
                check[curr] += 1
                if check[curr] > 1:
                    return False
        
        # [row1, col1, row2, col2]
        starts = [
            [0, 0, 2, 2], [0, 3, 2, 5], [0, 6, 2, 8],
            [3, 0, 5, 2], [3, 3, 5, 5], [3, 6, 5, 8],
            [6, 0, 8, 2], [6, 3, 8, 5], [6, 6, 8, 8]
        ]

        for start in starts:
            row1, col1 = start[0], start[1]
            row2, col2 = start[2], start[3]
            check = [0] * 10
            for row in range(row1, row2 + 1):
                for col in range(col1, col2 + 1):
                    curr = board[row][col]
                    if not curr.isdigit():
                        continue
                    else:
                        curr = int(curr)
                    check[curr] += 1
                    if check[curr] > 1:
                        return False

"""
- We are working with a matrix essentially.
- For each row, process all its columns, meaning all its elements.
- Must contain digits 1 to 9 with no duplicates. Keep track of what's been
seen so far, if seen again, then terminate, as it's not valid.
- Check each row and each column seperately. As row validity does not indicate
column validity, and vice-versa.
- It doesn't have to contain all the values from 1-9, just can't contain duplicates,
and whatever value it does have, must come from 1 to 9.
- There can be empty entries too. The board does not need to be full or be solvable
to be valid.
"""