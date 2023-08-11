def move(pos, dir, board):

    dirlist = {'up':[0,1],'down':[0,-1],'left':[-1,0],'right':[1,0]}

    for i in range(0,2):
        if -(board[i]//2) <= pos[i]+dirlist.get(dir)[i] <= board[i]//2:
            pos[i] += dirlist.get(dir)[i]

    return pos


def solution(keyinput, board):
    answer = [0,0]

    for ki in keyinput:
        answer = move(answer, ki, board)

    return answer


# print(solution(["left", "right", "up", "right", "right"]	,[11,11]))
print(solution(["down", "down", "up", "up", "up"], [3, 3] ))