import sys
import numpy as np
from graph_gen import *

def has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not

    return False

def main():
    sets1=[]
    for n in range (4):
        sets1.append([0]*4)
    sets1[0][1]=1
    sets1[0][2]=-1
    sets1[1][0]=1
    sets1[1][1]=-1
    sets1[2][2]=1
    sets1[2][0]=-1
    sets1[3][3]=1
    sets1[3][1]=-1
    if has_cycle(sets1):
        print('Yes')
    else:
        print('No')
    sets2=[]
    for n in range (4):
        sets2.append([0]*4)
    sets2[0][2]=1
    sets2[0][0]=-1
    sets2[1][0]=1
    sets2[1][1]=-1
    sets2[2][1]=1
    sets2[2][2]=-1
    sets2[3][1]=1
    sets2[3][3]=-1
    if has_cycle(sets2):
        print('Yes')
    else:
        print('No')
    sets3=[]
    for n in range (4):
        sets3.append([0]*4)
    sets3[0][2]=1
    sets3[0][0]=-1
    sets3[1][3]=1
    sets3[1][2]=-1
    sets3[2][1]=1
    sets3[2][3]=-1
    sets3[3][1]=1
    sets3[3][2]=-1
    if has_cycle(sets2):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
