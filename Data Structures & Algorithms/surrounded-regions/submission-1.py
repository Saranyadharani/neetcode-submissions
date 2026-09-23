from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #if there is no board return nothing
        if not board:
            return
        # define the rows and cols
        rows=len(board)
        cols=len(board[0])
        # define the bfs which takes the (r,c) mark them as S
        def bfs(r,c):
            queue=deque([(r,c)])
            board[r][c]='S'
            while queue:
                r,c=queue.popleft()# pop out the left most element
# explore in the 4 dir of the popped out element and find its neighbours and valid its bound
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols :
                        if board[nr][nc]=='O':
                            board[nr][nc]='S'
                            queue.append((nr,nc))
        # using Row wise loop flipping the Boundary O to S
        for r in range(rows):
            if board[r][0]=='O':
                bfs(r,0)
            if board[r][cols-1]=='O':
                bfs(r,cols-1)
        for c in range(cols):
            if board[0][c]=='O':
                bfs(0,c)
            if board[rows-1][c]=='O':
                bfs(rows-1,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='S':
                    board[r][c]='O'


