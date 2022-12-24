def solution(phone_book):
    answer = True

    phone_book.sort(key=len)

    for pb in range(0,len(phone_book)):
        for npb in range(pb+1, len(phone_book)):
            # if phone_book[npb] != phone_book[pb] \
            #         and len(phone_book[npb]) >= len(phone_book[pb]):
                # print("phone_book[pb]",phone_book[pb])
                # print("npb",npb)
                #
                # print("phone_book[pb][0:3]",phone_book[pb][0:len(phone_book[pb])])
                # print("npb[0:3]",npb[0:len(phone_book[pb])])
                #
                # print(phone_book[pb][0:len(phone_book[pb])] == npb[0:len(phone_book[pb])])
                answer = phone_book[pb][0:len(phone_book[pb])] != phone_book[npb][0:len(phone_book[pb])]
                if not answer:
                    return answer
    return True

print(solution(["119", "97674223", "1195524421"]	))
print(solution(["123", "456", "789"]))
print(solution(["12","123","1235","567","88"]))