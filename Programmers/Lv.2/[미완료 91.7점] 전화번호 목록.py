def solution(phone_book):
    hash = []
    for pb in phone_book:
        for i in range(1,len(pb)):
            hash.append(pb[0:i])
    print(hash)
    for pb in phone_book:
        if pb in hash:
            return False
    return True

# print(solution(["119", "97674223", "1195524421"]	))
print(solution(["123", "456", "789"]))
# print(solution(["12","123","1235","567","88"]))
# print(solution(["1","12"]))