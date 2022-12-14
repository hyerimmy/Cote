from _datetime import datetime as dt


def solution(m, musicinfos):
    answer = '(None)'

    time = [0]
    title = []
    melody = ''

    mlist = []
    for mk in range(0,len(m)):
        if m[mk] == '#':
            mlist.append(mlist.pop()+m[mk])
        else:
            mlist.append(m[mk])

    for mif in musicinfos:
        mif_time = (dt.strptime(mif.split(',')[1], '%H:%M')
                    - dt.strptime(mif.split(',')[0], '%H:%M')).seconds // 60
        time.append(time[-1]+mif_time)

        title.append(mif.split(',')[2])

        mif_melody = mif.split(',')[3]
        for mi in range(0,mif_time):
            melody += mif_melody[mi % len(mif_melody)]

    melodylist = []
    for mk in range(0, len(melody)):
        if melody[mk] == '#':
            melodylist.append(melodylist.pop() + melody[mk])
        else:
            melodylist.append(melody[mk])


    i = 0
    start = -1
    end = -1

    print("~~~~~~~~~~~~~~~~~~~~")
    print(mlist)
    print(melodylist)
    print("~~~~~~~~~~~~~~~~~~~~")

    for mldi in range(0,len(melodylist)):
        if mlist[i] == melodylist[mldi]:
            i += 1
            if i == 1:
                start = mldi
            if i == len(mlist):
                end = mldi
                break
        else:
            start = -1

    print("********start",start)
    print("********end",end)

    if start == -1 or end == -1:
        return answer

    print(time)

    print("<<<<<<<<<>>>>>>>>>>>>")
    answertime = 0
    for ti in range(1,len(time)):
        print("time[ti]",time[ti])
        print("time[ti]-time[ti-1]",time[ti]-time[ti-1])
        if start < time[ti] and end < time[ti]:
            if answertime < time[ti]-time[ti-1]:
                answer = title[ti-1]
                print("answer",answer)
                answertime = time[ti]-time[ti-1]

    return answer

# print(solution("ABC",
#                ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABCCCCCCC",
#                ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

print(solution("ABC",
               ["12:00,12:14,HELLO,ABAB", "13:00,13:05,WORLD,CDE"]))
