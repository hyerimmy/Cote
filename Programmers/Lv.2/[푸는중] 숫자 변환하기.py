
def calculate_func(x, y, n, answer):
    print(answer)
    for number in answer:
        new_number = [number * 2, number * 3, number + n]
        print(new_number)
        for nn in new_number:
            print(nn)
            if nn < y:
                answer[nn] = answer[number]+1
            elif nn == y:
                return answer[number]+1
        calculate_func(x,y,n,answer)

def solution(x, y, n):
    new_number = [x * 2, x * 3, x + n]
    answer = {
        x * 2 : 0,
        x * 3: 0,
        x + n: 0,
    }

    return calculate_func(x,y,n,answer)




print(solution(10,40,5))