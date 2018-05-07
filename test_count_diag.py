def count_diag(perm):
    count_diag = 0
    for i in perm:
        if i == 1 or i == 2:
            count_diag = count_diag + 1
    return count_diag

perm = [1, 1, 1, -1, -1] * 5
print(count_diag(perm))
print(perm) 