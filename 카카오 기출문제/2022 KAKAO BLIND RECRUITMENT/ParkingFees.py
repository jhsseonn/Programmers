import math

def solution(fees, records):
    parking_dict = {}
    parking_times = []
    parking_fees = []

    for record in records:
        record = record.split(' ')
        if record[1] in parking_dict.keys():
            parking_dict[record[1]].append(record[0])
        else:
            parking_dict[record[1]] = [record[0]]

    parking_dict = dict(sorted(parking_dict.items()))

    for k, v in parking_dict.items():
        time = 0
        for i in range(0, len(v), 2):
            if (i == len(v)-1):
                time+=calTime(convertTime(v[i]), convertTime("23:59"))
                print(time)
            else:
                time += calTime(convertTime(v[i]), convertTime(v[i+1]))
                print(time)
        parking_times.append(time)
            
    for t in parking_times:
        parking_fees.append(calFees(t, fees[1], fees[0], fees[2], fees[3]))

    return parking_fees

def convertTime(time):
    time_list = time.split(":")
    h = time_list[0]
    m = time_list[1]
    if h[0]==0:
        h = h[1]
    if m[0]==0:
        m = m[1]
    return int(h)*60+int(m)

def calTime(input, output):
    return output-input

def calFees(time, default_fee, default_time, point_time, point_fee):
    result = 0
    result += default_fee
    if time<=default_time:
        return result
    else:
        time -= default_time
        result += int(math.ceil(time/point_time))*point_fee
        return result

fees1 = [180, 5000, 10, 600]
records1 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees1, records1))

#다른 사람 풀이
#클래스를 사용했음... 그러게.. 클래스를 사용하는 방법이 있었네..
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]