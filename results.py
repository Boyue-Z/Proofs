def conv_symbol(row):
    result = []
    for ele in row:
        if ele == 1:
            result.append('//')
        elif ele == -1:
            result.append('\\')
        elif ele == 0:
            result.append('..')
    return result

def draw_solution(perm):
    s = []

    for i in range(5):
        s.append(perm[5 * i: 5 * i + 5])
        # print(s)
    s.reverse()

    for row in s:
        print(conv_symbol(row))

perm = [1, 1, 1, 1, 1,
 1, 0, 0, 0, 0,
 1, 0, -1, -1, 0,
 0, -1, -1 , 0, 1,
 -1, -1, 0, 1, 1]

print(draw_solution(perm))