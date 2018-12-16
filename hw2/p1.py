from util import *
import numpy as np

'''input'''
# msg = 'IS_THAT_W'
# msg = 'THIS_IS_AN_APPLE..'
msg = 'VJWUV,EDI'
# msg = 'KXTUFXMRHJ,WTMT'
input = np.array([to_number(msg[i]) for i in range(len(msg))])
# print(len(input))
input_mtx = np.reshape(input, (3, int(len(input)/3)))
# print(input_mtx)

'''key'''
# key_ = '4 3 24 29 14 1 9 9 22'
key_ = '25 8 25 9 9 16 28 21 18'
key = np.array(list(map(int, key_.split(' '))))
key_mtx = np.reshape(key, (3, int(len(key)/3)))
# print(key_mtx)

'''inverse of key'''
inv_key_mtx = inv_key(key_mtx)


'''output'''
# output_mtx = np.dot(key_mtx, input_mtx) % 31
output_mtx = np.dot(inv_key_mtx, input_mtx) % 31
# print(output_mtx)

output = [to_char(i) for i in output_mtx.flatten()]
print(''.join(output))
