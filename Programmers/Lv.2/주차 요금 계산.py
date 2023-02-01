from datetime import datetime
import math
def timediffer(starttime, endtime):
    time_object1 = datetime.strptime(starttime, '%H:%M')
    time_object2 = datetime.strptime(endtime, '%H:%M')
    return(((time_object2 - time_object1).seconds) // 60)

def solution(fees, records):
    answer = []
    rdictprocess = dict()
    rdict = dict()

    for r in records:
        rlist = r.split()
        if rlist[2] == "IN":
            rdictprocess[rlist[1]] = rlist[0]
        elif rlist[2] == "OUT":
            if rlist[1] not in rdict.keys():
                rdict[rlist[1]] \
                    = timediffer(rdictprocess[rlist[1]], rlist[0])
            else:
                rdict[rlist[1]] \
                    += timediffer(rdictprocess[rlist[1]], rlist[0])

            rdictprocess[rlist[1]] = ""

    for rdpk in rdictprocess.keys():
        if rdictprocess[rdpk] != "":
            if rdpk not in rdict.keys():
                rdict[rdpk] \
                    = timediffer(rdictprocess[rdpk], "23:59")
            else:
                rdict[rdpk] \
                    += timediffer(rdictprocess[rdpk], "23:59")

    carnum = sorted(list(rdict.keys()))
    for cn in carnum:
        if rdict[cn] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] +
                          math.ceil((rdict[cn]-fees[0])/fees[2])*fees[3])

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
