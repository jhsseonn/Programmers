col, row = map(int, input().split())
store_count = int(input())
stores = []
result = 0

for i in range(store_count):
    stores.append(list(map(int, input().split())))

x = list(map(int, input().split()))

for store in stores:
    distance=0
    if x[0]==store[0]:
        distance+=max(x[1], store[1])-min(x[1], store[1])
    elif (x[0]==1 and store[0]==2) or (x[0]==2 and store[0]==1):
        distance+=row
        distance+=min(x[1]+store[1], (col-x[1]+col-store[1]))
    elif (x[0]==3 and store[0]==4) or (x[0]==4 and store[0]==3):
        distance+=col
        distance+=min(x[1]+store[1], (row-x[1]+row-store[1]))
    else:
        if x[0]==1:
            if store[0]==3:
                distance+=x[1]+store[1]
            if store[0]==4:
                distance+=col-x[1]+store[1]
        if x[0]==2:
            if store[0]==3:
                distance+=x[1]+row-store[1]
            if store[0]==4:
                distance+=col-x[1]+row-store[1]
        if x[0]==3:
            if store[0]==1:
                distance+=x[1]+store[1]
            if store[0]==2:
                distance+=row-x[1]+store[1]
        if x[0]==4:
            if store[0]==1:
                distance+=col-store[1]+x[1]
            if store[0]==2:
                distance+=row-x[1]+col-store[1]
    result+=distance

print(result)