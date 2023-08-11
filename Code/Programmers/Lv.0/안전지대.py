def solution(board):
    answer = 0

    danger = [[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1],[0,-1],[0,1]]

    for y in range(0,len(board)):
        for x in range(0,len(board[y])):
            if board[y][x] == 1:

                for d in danger:
                    if 0<=y+d[0]<len(board) and 0<=x+d[1]<len(board):
                        if board[y+d[0]][x+d[1]] != 1:
                            board[y+d[0]][x+d[1]] = 2

    for b in board:
        for bb in b:
            if bb == 0:
                answer += 1
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))