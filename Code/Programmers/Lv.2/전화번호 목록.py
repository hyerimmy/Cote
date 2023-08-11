# def solution(phone_book):
#     hash = []
#     for pb in phone_book:
#         for i in range(1,len(pb)):
#             hash.append(pb[0:i])
#     for pb in phone_book:
#         if pb in hash:
#             return False
#     return True


# def solution(phone_book):
#     for number in phone_book:
#         for other_number in phone_book:
#             if len(number) < len(other_number):
#                 if other_number.startswith(number) and other_number:
#                     return False
#     return True

def solution(phone_book):
    phone_book.sort()
    for index in range(0,len(phone_book)-1):
        if phone_book[index+1].startswith(phone_book[index]):
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12","123","1235","567","88"]))
# print(solution(["1","12"]))