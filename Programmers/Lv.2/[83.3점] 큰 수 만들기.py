def solution(number, k):
    t = len(number) - k  # 최종 결과값 길이
    candidate_pool = [number]
    for i in range(t):
        new_candidate_pool = []
        for candidate in candidate_pool:
            k = len(candidate)-t
            new_candidate_pool.extend([candidate[:i]+candidate[i+idx:] for idx, n in enumerate(candidate[i:i+k+1]) if n == max(candidate[i:i+k+1])])
        candidate_pool = [number for number in new_candidate_pool if number[:i] == max([number[:i] for number in new_candidate_pool])]
        print(candidate_pool)
        if len(candidate_pool) == 1 and len(candidate_pool[0]) == t:
            return candidate_pool[0]


# print(solution("1924",2))
print(solution("1331234", 3))
# print(solution("4177252841",4))
