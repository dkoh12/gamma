# from collections import deque

from pprint import pprint

def getboard(n):
    return [[0] * n for i in range(n)]

# if this square is valid, place queen
def checkvalid(board, row, col):
    # check no queen in current row
    for i in range(col):
        if (board[row][i]):
            return False

    # check upper diagonal on left
    i=row
    j=col
    while(i>=0 and j>=0):
        if(board[i][j]):
            return False
        i-=1
        j-=1

    # check lower diagonal on left
    i=row
    j=col
    while(i<len(board) and j>=0):
        if(board[i][j]):
            return False
        i+=1
        j-=1

    return True

def solveNQueens(board, col, n):
    if(col == n):
        return True

    # for a given row
    for i in range(n):
        if checkvalid(board, i, col):
            board[i][col] = 1;

            if(solveNQueens(board, col+1, n)):
                return True

            board[i][col] = 0;

    return False


def nqueens(n):
    board = getboard(n)
    
    if(not solveNQueens(board, 0, n)):
        print("Solution does not exist")
        return;

    pprint(board);
    return;


if __name__=="__main__":
    nqueens(8)







# # find all squares in following row marked false
# def getchildren(board, i):
#     lst = []
#     if i < len(board):
#         for j in range(len(board)):
#             if not board[i+1][j]:
#                 lst.append((i+1, j))
#     return lst


    # # dfs
    # queens = []
    
    # queue = deque([(0, 0)])
    # #numqueens = 0
    
    # #i = 0 # row
    
    # failedstate = []
    
    # while len(queens) < n:
    
    #     #forward pass
    #     # will exit when either it has found all n queens or found a failed row
    #     while not queue.empty():
    #         q = queue.pop()
    #         i, j = q
    #         if (checkvalid(board, i, j)):
    #             queens.append((i, j))
    #             fillboard(board, i, j)
    #             children = getchildren(board, i)  # [(2, 2), (2, 3)]
    #             queue.extend(children)
            
    #     #backtracking
    #     if len(queens) < n:
    #         q = queens.pop()
    #         i, j = q
    #         failedstate.append((i, j)) # (2, 2)
    #         unfillboard(board, i, j)
    #         children = [k for k in getchildren(board, i-1) if k not in failedstate] #we don't repeat
    #         queue.extend(children)
            
    #  return queens
            
        