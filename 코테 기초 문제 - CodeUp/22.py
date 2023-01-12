date = input()
dateList = []
for i in range(0, len(date), 2):
    dateList.append(date[i:i+2])
print(" ".join(dateList))