import sys
import numpy as np
import pandas as pd


def load(fname):
    f = open(fname, 'r').readlines()
    n = len(f)
    ret = {}
    for l in f:
        l = l.split('\n')[0].split(',')
        i = int(l[0])
        ret[i] = {}
        for j in range(n):
            if str(j) in l[1:]:
                ret[i][j] = 1
            else:
                ret[i][j] = 0
    ret = pd.DataFrame(ret).values
    return ret


def get_tran(g):
    g = np.array(g, dtype=np.float)
    shape = g.shape
    for j in range(shape[1]):
        c = 0
        for i in range(shape[0]):
            if g[i, j] != 0:
                c += 1
        if c != 0:
            g[:, j] /= c
    return g


def cal_rank(t, d=0.85, max_iterations=1000, alpha=0.001):
    pbbt = np.ones(shape=(len(t), 1))/len(t)
    mat = d*t + (1-d)*np.ones(shape=t.shape)/len(t)
    for _ in range(int(np.log2(max_iterations))+1):
        mat = mat @ mat
    return mat @ pbbt


def save(t, r):
    np.savetxt(fname='_1.txt', X=t)
    np.savetxt(fname='_2.txt' , X=r)


def dist(a, b):
    return np.sum(np.abs(a-b))


def main():
    graph = load(sys.argv[1])
    transition_matrix = get_tran(graph)
    rank = cal_rank(transition_matrix)
    save(transition_matrix, rank)


if __name__ == '__main__':
    main()
