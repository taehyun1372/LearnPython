def nb_year(p0, percent, aug, p):
    count = 0
    current = p0
    while(True):
        count+=1
        if current * (1 + percent*0.01) + aug >= p:
            break
        else:
            current = current * (1 + percent*0.01) + aug > p
    return count

nb_year(1500, 5, 100, 5000)