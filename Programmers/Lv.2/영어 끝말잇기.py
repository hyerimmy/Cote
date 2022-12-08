def solution(n, words):
    result = [0,0]
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0]\
                or words[0:i-1].count(words[i]) > 0:
            if (i + 1) % n == 0:
                result[0] = n
            else:
                result[0] = ((i + 1) % (n))

            if (i + 1) % n == 0:
                result[1] = ((i + 1) // n)
            else:
                result[1] = ((i + 1) // n + 1)
            break
    return result


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
