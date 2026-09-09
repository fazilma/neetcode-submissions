class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                
                if num=='.':
                    continue
                boxid = int(row/3) *3+ int(col/3)
                if num in rowset[row] or num in colset[col] or num in box[boxid]:
                    return False
                else:
                    rowset[row].add(num)
                    colset[col].add(num)
                    box[boxid].add(num)
        return True