def accum(st):
    return "-".join([st[i].upper() + st[i].lower()*i for i in range(len(st))])

