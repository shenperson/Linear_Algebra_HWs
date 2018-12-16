import sys
import numpy as np
import pandas as pd
import re


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
    # TODO
    a = []
    for i in range(len(g.T)):
        zero = np.zeros(len(g.T[i]))
        temp = np.where(g.T[i] == 1)
        # print(len(temp[0]))
        zero[temp] = 1./len(temp[0])
        # print(zero)
        # a.append(zero)
        a.append(zero)
        # print(a[i])
    # print(np.array(a))
    return np.array(a).T


def cal_rank(t, d=0.85, max_iterations=1000, alpha=0.001):
    # TODO
    R = np.ones(len(t)).T/len(t)
    d_arr = R*(1-d)
    R_prev = np.zeros(len(t)).T
    # print(d_arr)
    for _ in range(max_iterations):
        R = d_arr+np.dot(t, R)*d
        if(dist(R_prev, R) <= alpha):
            break
        R_prev = np.array(R)
        # print(R)

    return R


def cal_rank2(i, t, d=0.85, max_iterations=1000, alpha=0.001):
    # TODO
    R = np.ones(len(t)).T/len(t)
    d_arr = R*(1-d)
    R_prev = np.zeros(len(t)).T
    R2 = np.zeros(len(t))
    R2[i] = 1
    R = R2
    # print(d_arr)
    for _ in range(max_iterations):
        R = d_arr+np.dot(t, R)*d
        if(dist(R_prev, R) <= alpha):
            break
        R_prev = np.array(R)
        # print(R)

    return R


def save(t, r):
    # TODO
    np.savetxt('./1.txt', t)
    np.savetxt('./2.txt', r)

    return


def dist(a, b):
    return np.sum(np.abs(a-b))


def main():
    try:
        graph = load(sys.argv[1])
    except:
        graph = load('graph.txt')
    # print(graph)
    transition_matrix = get_tran(graph)
    # print(transition_matrix)
    rank = cal_rank(transition_matrix)
    # print(rank)
    save(transition_matrix, rank)


def test():
    try:
        graph = load(sys.argv[1])
    except:
        graph = load('graph.txt')
    # print(graph)
    transition_matrix = get_tran(graph)
    # print(transition_matrix)
    rank = cal_rank(transition_matrix)
    rank2 = cal_rank2(998, transition_matrix)
    # print(rank)
    print(dist(rank, rank2))
    # save(transition_matrix, rank2)


if __name__ == '__main__':
    main()
    # test()
