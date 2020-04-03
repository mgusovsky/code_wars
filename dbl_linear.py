def dbl_linear(n):
    li = [1,3]
    i, j = 0, 0
    while len(li)-1 < n:
        i_v = 2 * li[i] + 1
        j_v = 3 * li[j] + 1
        if j_v < i_v:
            if j_v != li[-1]:
                li.append(j_v) 
            j += 1
        if j_v >= i_v:
            if i_v != li[-1]:
                li.append(i_v)        
            i += 1
    return li[-1]

print(dbl_linear(10))
print(dbl_linear(20))
print(dbl_linear(30))
print(dbl_linear(50))