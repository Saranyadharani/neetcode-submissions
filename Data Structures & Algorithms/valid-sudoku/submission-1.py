class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num == ".":
                    continue
            
                if num in row[r]:
                    return False
                row[r].add(num)

                if num in col[c]:
                    return False
                col[c].add(num)
                
                box_idx=(r//3)*3 + (c//3)
                if num in box[box_idx]:
                    return False
                box[box_idx].add(num)
        return True