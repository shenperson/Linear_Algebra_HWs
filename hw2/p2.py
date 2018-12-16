from util import *
import numpy as np

'''find key'''
cipher1 = 'POWRDPTF.'
plain1 = 'ARE_YOU_F'
cp1 = np.array([to_number(cipher1[i]) for i in range(len(cipher1))])
pl1 = np.array([to_number(plain1[i]) for i in range(len(plain1))])
cp1_mtx = np.reshape(cp1, (3, int(len(cp1)/3)))
pl1_mtx = np.reshape(pl1, (3, int(len(pl1)/3)))

# print(cp1_mtx)
# print(pl1_mtx)
inv_pl1_mtx = inv_key(pl1_mtx)
key_mtx = np.dot(cp1_mtx, inv_pl1_mtx) % 31
key = key_mtx.flatten()
for i in key:
    print(i, end=' ')
print()


'''input'''
msg = 'ESHMXH,M?'
input = np.array([to_number(msg[i]) for i in range(len(msg))])
# print(len(input))
input_mtx = np.reshape(input, (3, int(len(input)/3)))
# print(input_mtx)

'''inverse of key'''
inv_key_mtx = inv_key(key_mtx)


'''output'''
# output_mtx = np.dot(key_mtx, input_mtx) % 31
output_mtx = np.dot(inv_key_mtx, input_mtx) % 31
# print(output_mtx)

output = [to_char(i) for i in output_mtx.flatten()]
print(''.join(output))
