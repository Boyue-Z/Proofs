def generating_permutations(perm, n):
    if len(perm) == n:
        print(perm)
        return
    
    for k in range(n):
        if k not in perm:
            perm.append(k)
            generating_permutations(perm, n)
            perm.pop()

generating_permutations(perm = [], n = 4)

