class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [0]* 9
        colset = [0] * 9
        box = [0] * 9
        for i in range(9):
            rowset[i] = set()
            colset[i] = set()
            box[i] = set()
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                boxid = int(row/3) *3+ int(col/3)
                if num=='.':
                    continue
                if num in rowset[row] or num in colset[col] or num in box[boxid]:
                    return False
                else:
                    rowset[row].add(num)
                    colset[col].add(num)
                    box[boxid].add(num)
        return True