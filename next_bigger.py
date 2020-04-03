from itertools import permutations
import random
import time
start_time = time.time()

def next_bigger(n):
    digits = [i for i in str(n)]
    x = len(digits)-2
    for i in range(x, -1, -1):
        if digits[i] >= digits[i+1]:
            continue
        d_const = digits[:i]
        d_var = digits[i:]
        test = int(''.join(d_var))
        perm = list(permutations([j for j in d_var]))
        perm = list(dict.fromkeys(perm)) # deletes duplicates
        perm = sorted([int(''.join(x)) for x in perm]) # list of ints
        for j in range(0, len(perm)):
            if test < perm[j]:
                ans_var = [k for k in str(perm[j])]
                ans = int(''.join((d_const + ans_var)))
                return ans
        print('not in the last {} digits!'.format(x-i))
    return -1

print(next_bigger(211111111))
# print(next_bigger(21111111111111))
# for y in range(0, 1500):
#     print(next_bigger(random.randrange(0, 10**10)))
print("--- %s seconds ---" % (time.time() - start_time))
