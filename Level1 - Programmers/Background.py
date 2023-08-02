def solution(wallpaper):
    answer = []
    indexes = []
    lux, luy, rdx, rdy = 0, 0, 0, 0

    for i, row in enumerate(wallpaper):
        for idx, r in enumerate(row):
            if r=="#":
                indexes.append(str(i)+","+str(idx))

    for index, s in enumerate(indexes):
        if index==0:
            lux, luy = int(list(s.split(","))[0]), int(list(s.split(","))[1])
            rdx, rdy = int(list(s.split(","))[0]), int(list(s.split(","))[1])
        x, y = int(list(s.split(","))[0]), int(list(s.split(","))[1])
        if x<lux:
            lux = x
        if y<luy:
            luy = y
        if x>rdx:
            rdx = x
        if y>rdy:
            rdy = y
        
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx+1)
    answer.append(rdy+1)

    return answer


wlist = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]	
print(solution(wlist))

#다른 사람 풀이
#난.... 파이썬을 쓴단 소리는 하고 다니면 안 될 듯
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]