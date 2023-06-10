# def solution(elements):
#     result = list()
#     for size in range(1,len(elements)):
#         for i in range(len(elements)):
#             if (i + size) <= len(elements):
#                 result_number = sum(elements[i:i+size])
#             else:
#                 result_number = sum(elements[i:len(elements)] + elements[0:i + size - len(elements)])
#
#             if result_number not in result:
#                 result.append(result_number)
#
#     return len(result)+1

def solution(elements):
    result = set()
    for size in range(1,len(elements)):
        for i in range(len(elements)):
            if (i + size) <= len(elements):
                result_number = sum(elements[i:i+size])
            else:
                result_number = sum(elements[i:len(elements)] + elements[0:i + size - len(elements)])
            result.add(result_number)
    return len(result)+1

print(solution([7,9,1,1,4]))