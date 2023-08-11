def plus_10_minutes(time:str):
    hour = int(time.split(":")[0])
    min = int(time.split(":")[1])
    min += 10
    if min >=60:
        min -= 60
        hour += 1
    hour, min = str(hour), str(min)
    if int(min) < 10:
        min = "0"+min
    if int(hour) < 10:
        hour = "0"+hour
    return (hour+":"+min)

def is_available_time(history, new):
    history = history.split(":")
    new = new.split(":")

    if int(history[0]) < int(new[0]):
        return True
    if int(history[0]) == int(new[0]):
        if int(history[1]) <= int(new[1]):
            return True
    return False

def solution(book_time):
    answer = 0
    time_history_list = []
    book_time.sort()
    # print(book_time)

    for time in book_time:
        is_update = False
        if not time_history_list:
            time_history_list.append(plus_10_minutes(time[1]))
        else:
            for idx in range(0,len(time_history_list)):
                if is_available_time(time_history_list[idx],time[0]):
                    time_history_list[idx] = plus_10_minutes(time[1])
                    is_update = True
                    break
            if not is_update:
                time_history_list.append(plus_10_minutes(time[1]))
        # print(time_history_list)

    return len(time_history_list)

# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution(	[["09:10", "10:10"], ["10:20", "12:20"]]))