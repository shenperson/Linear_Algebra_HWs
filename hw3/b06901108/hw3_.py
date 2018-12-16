import sys
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy.linalg import inv
import math

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # TODO
    # implement cosine transform
    B_inv=inv(np.mat(B))
    x_T=np.mat(x).T
    ak_list=B_inv*np.mat(x_T)
    return ak_list

def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform
    return B*a

def gen_basis(N):
    # TODO
    size=len(N)
    row=[]
    for_matrix=[]
    for i in range(0,size):#row
        for j in range(0,size):#column
            if i==0:
                row.append(1/math.sqrt(size))
            else:
                t=math.sqrt(2)
                s=math.sqrt(size)
                c0=t/s
                thita=((j+0.5)*i*(math.pi))/size
                row.append((c0)*math.cos(thita))
        for_matrix.append(row)
        row=[]
    matrix=np.mat(for_matrix)
    
    return matrix.T

def set_mask(Min,Max,lb,ub):
    mask=[]
    for i in range(Min,Max):
        if i>lb and i<ub:
            mask.append(1)
        else:
            mask.append(0)
    return mask

def get_mask(ak,order):
    global debug
    order_copy=order
    in_peak=0
    find_list=[]
    lb=0
    for i in range (0,len(ak)):
         if ak[i]>14 and peak==0:
             peak=1
             order=order-1
         if ak[i]<14:
             peak=0
             if lb!=0:
                 ub=i
                 if debug==1:
                     print ('lb=',lb,'ub=',ub)
                 return set_mask(0,len(ak),lb-50,ub+50)
         if order==0 and peak==1:
             lb=i
             peak=2
    

def filt(origin,mask):
    for i in range(0,len(mask)):
        if mask[i]!=0:
            origin[i]=origin[i]*mask[i]
        else :
            origin[i]=[0]
    return origin

def write_in(name,word):
    f=open(name,'w')
    for i in range(0,len(word)):
        push=float(word[i])
        push=str(push)+"\n"
        f.writelines(push)
    f.close()

if __name__ == '__main__':

    signal_path = sys.argv[1]
    global debug
    debug=0
    if len(sys.argv)>2:
        debug=1
        print ('in ',sys.argv[2],'mode ...')
    f=open(signal_path,'r')
    y_list=[]
    for i in range(0,1000):
        a=float(f.readline())
        y_list.append(a)
    if debug==1:
        plot_wave(y_list,'orgin')
    Basis=gen_basis(y_list)
    ak_list=CosineTrans(y_list,Basis)
    b=InvCosineTrans(ak_list,Basis)
    #mask1=set_mask(0,1000,-1,2)#100)
    #mask2=set_mask(0,1000,350,550)
    if debug==1:
        plot_wave(InvCosineTrans(ak_list,Basis),'return')
    mask1=get_mask(ak_list,1)
    index=3
    if sys.argv[1]=='test.txt':
        index=2
    mask2=get_mask(ak_list,index)
    plot_ak(ak_list,'b06901108_freq')
    ak_list_copy=ak_list.copy()
    f1=InvCosineTrans(filt(ak_list,mask1),Basis)
    f3=InvCosineTrans(filt(ak_list_copy,mask2),Basis)
    str1='b06901108_f1.txt'
    str2='b06901108_f3.txt'
    if debug==1:
        str1=str1+'.debug'
        str2=str2+'.debug'
    write_in(str1,f1)#InvCosineTrans(filt(ak_list,mask1),Basis))
    write_in(str2,f3)#InvCosineTrans(filt(ak_list_copy,mask2),Basis))
    if debug==1:
        plot_ak(filt(ak_list,mask1),'freq_f1')
        plot_ak(filt(ak_list_copy,mask2),'freq_f3')
        plot_wave(f1,'f1')#InvCosineTrans(ak_list,Basis),'f1')
        plot_wave(f3,'f3')#InvCosineTrans(ak_list_copy,Basis),'f3')
