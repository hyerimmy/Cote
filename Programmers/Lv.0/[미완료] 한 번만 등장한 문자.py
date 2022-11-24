from collections import Counter

def solution(s):
    counter = Counter(s)
    print(counter)
    print(list(counter))
    answer = ''
    return answer

print(solution("abcabcadc"))