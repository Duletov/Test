import random

M = [[10000000] * 15 for i in range(15)]
N = [[0] * 15 for i in range(15)]

for ji in range(29):
    m = random.randint(1, 15)-1
    n = random.randint(1, 15)-1
    w = random.randint(1, 200)-100
    print(m+1 ,n+1, w)
    M[m][n] = w
    N[m][n] = w
    
for row in M:
    print(' '.join([str(elem) for elem in row]))
print('\n')
for row in N:
    print(' '.join([str(elem) for elem in row]))
