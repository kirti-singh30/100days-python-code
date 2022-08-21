def maxprofit(price,start,end):
    if end<= start:
        return 0

    for i in range(start, end+1):
        for j in range(i+1,end+1):
            