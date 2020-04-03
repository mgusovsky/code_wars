def snail(snail_map):
    print(snail_map)
    a = rec(snail_map, len(snail_map), 0, list())
    print(a)
    return a

def rec(smap, n, i, temp= list()):
    m = n-1
    if smap == [[]]:
        return temp
    if (n - 2*i) < 1:
        return temp
    if (n - 2*i) == 1:
        temp.append(smap[i][i])
        return temp
    for x in range(i, n-i):
        temp.append(smap[i][x])
    for y in range(i+1, n-i):
        temp.append(smap[y][m-i])
    for x in range(m-(i+1), i, -1):
        temp.append(smap[m-i][x])
    for y in range(n-(i+1), i, -1):
        temp.append(smap[y][i])
    return rec(smap, n, i+1, temp)
        
array = list()

print(snail(array))
