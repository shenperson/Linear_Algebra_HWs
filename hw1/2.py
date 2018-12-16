import numpy as np
sets = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
temp = sets
# print(np.dot(A, A))
for i in range(len(sets)+1):
    for k in range(len(sets)):
        if temp[k][k] >= 1:
            print('True')
    temp = np.dot(temp, sets)
    print(temp, ' ')
