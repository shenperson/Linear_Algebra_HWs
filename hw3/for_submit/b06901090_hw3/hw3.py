import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
from math import cos, sin, pi


def plot_wave(x, path='./wave'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path+'.png')


def plot_ak(a, path='./freq'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path+'_freq.png')


def get_x(filename='./test'):
    """get index and x array"""
    with open((filename+'.txt'), 'r', encoding='utf-8') as file:
        index, x = [], []
        for i, j in enumerate(file):
            index.append(i)
            x.append(float(j))
        return np.array(index), np.array(x)


def plot_txt(filename='./test', output='./wave2'):
    """plot the waveform from txt file"""
    with open((filename+'.txt'), 'r', encoding='utf-8') as file:
        x, y = get_x(filename)
        plt.plot(y)
        plt.savefig(output+'.png')


def CosineTrans(x, B):
    # TODO
    # implement cosine transform
    return np.dot(np.linalg.inv(B), x)


def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform
    return np.dot(B, a)


def gen_basis(N):
    # TODO
    X = np.array([[((2**(0.5)*cos((n+0.5)*k*pi/N)) if k > 0 else 1)*(N**(-0.5))
                   for n in range(N)] for k in range(N)])
    return X.T


def find_freq(x):
    mean = sum(x)*1./len(x)
    max_ = max(x)
    freq = []
    temp = 0
    for i in range(len(x)):
        if x[i] > 5:
            freq.append(index[i])
        temp = x[i]
    return np.array(freq)


def mask(N, index, freq):
    idx_list = []
    temp_list = []
    zero = np.zeros(N, dtype=bool)
    temp = freq[0]
    for i in range(len(freq)):

        if(freq[i]-temp) < 10:
            temp_list.append(freq[i])
        else:
            idx_list.append(temp_list)
            temp_list = []
            temp_list.append(freq[i])
            temp = freq[i]
        if i == len(freq)-1:
            idx_list.append(temp_list)
            temp_list = []
    _mask = []
    for i in idx_list:
        zero[i] = True
        _mask.append(zero)

        zero = np.zeros(N, dtype=bool)
    return _mask


def output_ans(i, N, B, freq, _mask, filename='b06901090'):
    freq1 = np.array(freq)
    freq1[~_mask[i-1]] = 0
    np.savetxt('./'+filename+'_f'+str(i)+'.txt',
               InvCosineTrans(B, freq1))
    return InvCosineTrans(B, freq1)


if __name__ == '__main__':
    """ deal with input information """
    try:
        signal_path = sys.argv[1]
    except:
        signal_path = 'b06901090.txt'
    filename = re.sub('.txt', '', signal_path)
    index, x = get_x(filename)

    """ generate basis 'B' """
    N = len(index)
    B = gen_basis(N)

    """ cosine transform """
    Output = CosineTrans(x, B)
    plot_ak(Output, filename)

    """ find peak frequency and generate mask """
    freq = find_freq(Output)
    all_freq = np.zeros(N)
    all_freq[freq] = 1
    _mask = mask(N, index, freq)

    """ inverse consine transform (and plot the waveform) """
    o1 = output_ans(1, N, B, all_freq, _mask, filename)
    plot_wave(o1, './wave1')
    o3 = output_ans(3, N, B, all_freq, _mask, filename)
    plot_wave(o3, './wave3')
