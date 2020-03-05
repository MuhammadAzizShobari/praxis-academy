listData = [3,4,100,90,70]
iterasi = 0

for x in range (0,len(listData)-1):
    minIndex = x
    for y in range (x+1,len(listData)):
        iterasi += 1
        if listData[y] < listData[minIndex]:
            minIndex = y
    listData[x],listData[minIndex] = listData[minIndex],listData[x]
    print(listData)

    print(iterasi)