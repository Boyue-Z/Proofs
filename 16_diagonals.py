signs = [1, -1, 0]

def can_be_extended_to_solution(perm):
    current = len(perm) - 1

    last = current - 1
    down = current - 5
    diag_l = down - 1
    diag_r = down + 1

    if current % 5 == 0:
        last = -1
        diag_l = -1    
    
    if (current + 1) % 5 == 0:
        diag_r = - 1

    # print("current, last, down, diag_l, diag_r:", current, last, down, diag_l, diag_r)
    # print("perm:", perm)
   
    # pass if perm[current] is empty
    if perm[current] == 0:
        return True

    # check last, must be same
    if (last >= 0) and perm[last] != 0 and (perm[current] - perm[last] != 0):
        # print("Last error,last, current: ", perm[last], perm[current])
        # print("\n")
        return False
    
    # check down, must be same
    if (down >= 0) and perm[down] != 0 and (perm[current] - perm[down] != 0):
        # print("Down error, down, current:", perm[down], perm[current])
        # print("\n")
        return False

    # check diag_L
    if (diag_l >= 0) and perm[diag_l] != 0:
        if perm[current] == 1 and (perm[current] - perm[diag_l] == 0):
            return False
            

    # check diag_R
    if (diag_r >= 0) and perm[diag_r] != 0:
        if perm[current] == -1 and (perm[current] - perm[diag_r] == 0):
            return False

    print("current, last, down, diag_l, diag_r:", current, last, down, diag_l, diag_r)
    print("perm:", perm)
    print("\n")

    return True

def count_diag(perm):
    count_diag = 0
    for i in perm:
        if i != 0:
            count_diag = count_diag + 1
    return count_diag 

def count_zero(perm):
    count = 0
    for i in perm:
        if i == 0:
            count = count + 1
    return count

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

count = 0
def extend(perm, n):
    global count
    count = count + 1

    if len(perm) == 25:
        if count_diag(perm) < 16:
            draw_solution(perm)
            print("\n")
            return
        
        print("Find solution:")
        print(perm)
        draw_solution(perm)
        exit()
    
    for sign in signs:
        if count_zero(perm) <= 10:
            perm.append(sign)
            if can_be_extended_to_solution(perm):
                extend(perm, n)
            perm.pop()

extend(perm = [], n = 5)
print(count)