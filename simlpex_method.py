# # Simplex method for nth coefficients & nth constraints
# # also print a tables of iterations
import numpy as np
import pandas as pd
# input_data
a = input("enter your problem is maximiz(for enter max) or minimiz(for enter min): ")
b = int(input("how much constraints you have :"))  # No. of constraints
print("enter the coefficients of objective function(Z) separate by coma")
str1 = input("= ")
str1 = str1.strip(" ").split(",")
cj = list(map(lambda x:float(x),str1))
if a == 'min':
    cj = list(map(lambda x:-x ,cj))
sym=[]
for i in range(len(cj)):
    sym.append('x'+str(i+1))
l1 = []
xB = []
cB = []
B = []
l2 = []
for i in range(1,1+b):
    print("enter the coefficients of constraint",i)
    str2 = input("= ")
    str2 = str2.strip(" ").split(",")
    coc = list(map(lambda x:float(x),str2))
    l1.append(coc)
    print("d",i,end="",sep="")
    d = float(input(' = '))
    xB.append(d)
    cj.append(0) # enter value of slack variable in list of cj
    cB.append(0)
    B.append("s"+str(i))
    s = []
    for j in range(1,1+b):
        if i==j:
            s.append(1)
        else :
            s.append(0)
    l2.append(s)
l0 = list(np.array(l1).transpose())
l0 = list(map(lambda x : list(x),l0))
sym = sym + B
l3 = l0 + l2 

def print_table(cj,cB,B,xB,l3,zj_cj):
    D = {"cB":cB,'B':B,"xB":xB}
    D1 = {}
    for i in range(len(sym)):
        D[sym[i]]= l3[i]
    D3 = {**D,**D1}
    print("       Cj =",end="")
    for i in cj:
        print(i,end='   ')
    print()
    print(pd.DataFrame(D3))
    print("    Zj_Cj =",end="")
    for i in zj_cj:
        print(i,end='   ')
    print()
    print("\n---------------------------------------------------------------------------\n")

r = []
for i in range(b):
    r1 = l1[i]+l2[i]
    r.append(r1)   # r[i], i = 1,2,3...n  r is numpay array matrix
r = np.array(r)

while True:
    zj_cj = list(np.sum(cB*r.transpose(), axis=1) - cj)
    print_table(cj,cB,B,xB,l3,zj_cj)
    u = len(list(filter(lambda x: (x < 0), zj_cj)))
    if u==0:
        break
    keyj = zj_cj.index(min(zj_cj))
    key_column = list(r[:,keyj])
    l4 = [] # xB/key_column
    for i in range(len(xB)):
        if key_column[i] != 0:
            c = xB[i]/key_column[i]
        else:
            c = 10000000
        l4.append(c)
    keyi = l4.index(min(l4))
    key = r[keyi][keyj]
    a1 = r[keyi]/key
    l5 = []
    for i in range(len(xB)):
        if i!=keyi:
            x = xB[i] - (xB[keyi]/key)*key_column[i]
        else:
            x = xB[keyi]/key
        l5.append(x)
    xB = l5
    l6 = []     
    for i in range(len(key_column)):
        if key_column[i]>=0 and i!=keyi:
            a2 = r-key_column[i]*a1
            a2 = a2[i]
        else :
            a2 = a1
            B[i] = sym[keyj]
            cB[i] = cj[i]
        l6.append(a2)
    r = np.array(l6)
    l3 = r.transpose()

xB, cB = np.array(xB), np.array(cB)
sol = np.sum(xB*cB)
print("The solution is optimum\n",a,"z =",sol)