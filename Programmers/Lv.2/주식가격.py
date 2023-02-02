def solution(prices):
    answer = []

    for i in range(0,len(prices)):
        ans = 0
        for k in range(i+1,len(prices)):
            ans += 1
            if prices[i] > prices[k]:
                break
        answer.append(ans)

    return answer

print(solution([1, 2, 3, 2, 3]	))