import heapq

def solution(scoville, K):
    answer = 0

    hscov = []
    for s in scoville:
        heapq.heappush(hscov,s)

    while hscov[0] < K:
        try:
            heapq.heappush(hscov,heapq.heappop(hscov) + (heapq.heappop(hscov) * 2))
            answer += 1
        except IndexError:
            return -1
    return answer

print(solution([1,2,3,9,10,12],7))