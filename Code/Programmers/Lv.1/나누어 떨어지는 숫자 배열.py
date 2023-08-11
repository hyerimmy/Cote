def solution(arr, divisor):
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if not answer:
        return [-1]
    return sorted(answer)

def solution2(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
