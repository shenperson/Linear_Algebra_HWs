import sys
import numpy as np
from graph_gen import *


def has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    for i in sets:
        for j in sets:
            if i < j:
                for k in range(len(i)):
                    if i[k]*j[k] == -1:
                        temp = []
                        for q in range(len(i)):
                            temp.append(i[q]+j[q])
                        sets.append(temp)
        if (not (-1 in i)) and (not (1 in i)):
            return True

    return False


def main():
    p1_list = list()
    if len(sys.argv) <= 1:
        p1_list = get_p1('r07')
    else:
        p1_list = get_p1(sys.argv[1])

    # return
    for sets in p1_list:
        '''
          HINT: You can `print(sets)` to show what the matrix looks like
            If we have a directed graph with 2 -> 3 4 -> 1 3 -> 5 5 -> 2 0 -> 1
                   0  1  2  3  4  5
                0  0  0 -1  1  0  0
                1  0  1  0  0 -1  0
                2  0  0  0 -1  0  1
                3  0  0  1  0  0 -1
                4 -1  1  0  0  0  0
            The size of the matrix is (5,6)
        '''
        if has_cycle(sets):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
