import itertools
def solution(word):
    answer = []

    for i in range(1,6):
        for c in itertools.product(['A','E','I','O','U'],repeat=i):
            answer.append(''.join(list(c)))
    answer.sort()
    return answer.index(word)+1


for c in itertools.product(['A', 'E', 'I', 'O', 'U'], repeat=2):
    print(c)
    print(''.join(list(c)))