# Problem: Is it possible to place n queens on an n x n chessborad such that no two queens attack each other?

import itertools as it

# check that are two cells on same diagonal?
def is_solution(perm):
    '''如果是對角線的話, 點1跟點2相離水平跟垂直距離會相等, 不管點1是否在 i == j 的位置上'''
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True

number = int(input("Enter size of chessborad?"))

perm_tmep = []

for perm in it.permutations(range(number)):
    if is_solution(perm):
        perm_temp = perm
        print(perm)
        break
        # exit()

temp = [['.' for i in range(number)] for j in range(number)]

count = 0
for perm in perm_temp:
    temp[count][perm] = 'Q'
    count = count+1

for i in range(number):
    print(temp[i])

