# Assignment_7
# python

# figure(num=None, figsize=None, dpi=None, *, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)[source]
# plt.plot(x, y, color='g', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
# subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
# ax.bar(x, height, width, bottom, align)


# Plotting one graph in one figure window:
# a. y = x2 in the interval [−2,2].
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2,2,0.05)
y = x**2
fig = plt.figure(figsize=(7,6),dpi=125,edgecolor='red')
ax = fig.add_subplot()
ax.plot(x,y,'r*',label="y=x^2")
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.legend(loc='upper right')
ax.set_title('Graph of parabola')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
plt.show()


# b. y = x3 − 4x − 9 in the interval [-2,3].
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2,3,0.05)
y = (x**3)-4*x-9
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x,y,'k_')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.legend(["y=x^3-4*x-9"],loc='upper left')
ax.set_title('Graph of y=x^3-4*x-9')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
plt.show()

# Plotting two graphs in two figure windows:(Using plt.figure command)
# a. y = sin(x) and z = cos(x) in the interval [−2π, 2π].
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2*np.pi,2*np.pi,0.05)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x,y,'b|',label="y=sinX")
ax.legend(loc='upper right')
ax.set_title('Graphs of y=sinX and y=cosX')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
y1 = np.cos(x)
ax1 = fig.add_subplot(212)
ax1.plot(x,y1,'y_',label="y=cosX")
ax1.legend(loc='lower right')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
plt.show()


# b. y = sin−1(x) and z = cos−1 (x) in the interval [−1,1].
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-1,1,0.005)
y = np.arcsin(x)
fig = plt.figure()
ax = fig.add_subplot(121)
ax.plot(x,y,'k|',label="y=sin^(-1)X")
ax.legend(loc='upper left')
ax.set_title('Graph of y=sin^(-1)X')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
y1 = np.arccos(x)
ax1 = fig.add_subplot(122)
ax1.plot(x,y1,'k-',label="y=cos^(-1)X")
ax1.legend(loc='upper right')
ax1.set_title('Graph of y=cos^(-1)X')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
plt.show()


# c. Write a Python code to plot graph of log(x) and e^x in one graph and in same figure window using appropriate commands and scale
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,5,0.05)
y = np.log(x)
y1 = np.exp(x)
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x,y,'k+',label="y=log(x)")
ax.legend(loc='upper left')
ax.set_title('Graphs of y=log(x) and y=e^x')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax1 = fig.add_subplot(212)
ax1.plot(x,y1,'k*',label="y=e^x")
ax1.legend(loc='upper left')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
plt.show()


# Write a Python code to plot graphs of x^2, √𝑥, e^x and log(x) by givingappropriate range to all using subplot command.
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,5,0.05)
y = x**2
y1 = x**0.5
y2 = np.exp(x)
y3 = np.log(x)
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(221)
ax1 = fig.add_subplot(222)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(224)
ax.plot(x,y,'k',label="y=x^2",linewidth=1)
ax.legend(loc='upper left')
ax.set_title('Graph of y=x^2',loc='left',size=10)
ax.set_ylabel('y-axis')
ax1.plot(x,y1,'k',label="y=x^(1/2)",linewidth=2)
ax1.legend(loc='upper left')
ax1.set_title('Graph of y=x^(1/2)',loc='left',size=10)
ax2.plot(x,y2,'k',label="y=e^x",linewidth=3)
ax2.legend(loc='upper left')
ax2.set_title('Graph of y=e^x',loc='left',size=10)
ax2.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')
ax3.plot(x,y3,'k',label="y=log(x)",linewidth=4)
ax3.legend(loc='lower right')
ax3.set_title('Graph of y=log(x)',loc='left',size=10)
ax3.set_xlabel('x-axis')
plt.show()


# 1. : Write a Python code to plot a bar graph of following data:
# Languages C C++ JAVA Python MATLAB
# Students 23 17  35   29     12
import matplotlib.pyplot as plt
langs = ['C', 'C++', 'Java', 'Python', 'Matlab']
students = [23,17,35,29,12]
plt.bar(langs,students,label="Language",color='k')
plt.legend(loc='upper right')
plt.title('BAR PLOT')
plt.xlabel('Languages')
plt.ylabel('Number of Students')
plt.show()


# 2. Write a Python code to plot a multiple bar graph of the following data:
# 2015 20 40 30
# 2016 25 23 22
# 2017 50 51 45
# 2018 20 17 19
import numpy as np
import matplotlib.pyplot as plt
X = np.arange(4)
Y = [[20, 25, 50, 20],[40, 23, 51, 17],[30, 22, 45, 19]]
plt.bar(X, Y[0], color = 'y', width = 0.25,edgecolor='red')
plt.bar(X + 0.25, Y[1], color = 'b', width = 0.25,edgecolor='red')
plt.bar(X + 0.50, Y[2], color = 'r', width = 0.25,edgecolor='red')
plt.xticks(X + 0.25,["2015","2016","2017","2018"])
plt.title('MULTIPLE BAR PLOT')
plt.xlabel('Number of Years')
plt.ylabel('Data')
plt.legend(labels=['1','2','3'])
plt.show()


# 3. Write a Python code to plot stack bar graph of the following data:
# Sr. No. 0  1  2  3  4
# Men     20 35 30 35 27
# Means 
# Woman   25 32 34 20 25
# Means 
import numpy as np
import matplotlib.pyplot as plt
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
x = np.arange(5)
plt.bar(x, menMeans, width=0.40, color='r')
plt.bar(x, womenMeans, width=0.40,bottom=menMeans, color='k')
plt.ylabel('Scores by group')
plt.xlabel('Groups')
plt.title("Men's group vs Women's group")
plt.legend(labels=['Men', 'Women'])
plt.xticks(x,['G1', 'G2', 'G3', 'G4', 'G5'])
plt.show()


# 4. Write a Python code to plot histogram of the following data:
# 22,87,5,43,56,73,55,54,11,20,51,5,79,31,27.
import numpy as np
import matplotlib.pyplot as plt
a = [22, 87, 5, 43, 56,73, 55, 54, 11,20, 51, 5, 79, 31,27]
bins = np.arange(0,100,10)
plt.title("HISTOGRAM PLOT")
plt.ylabel('number of age-data in subinterval')
plt.xlabel("people's ages criteria")
plt.hist(a,bins,color='k')
plt.legend(labels=['age-data'])
plt.xticks(bins)
plt.show()


# Q.2 Python Programme related to While loop
# 1. Write a while loop that adds all the numbers up to 100 (inclusive).
sum = 0
i = 1
while i<=100:
    sum+=i
    i+=1
print("sum of 1 to 100 is",sum)

# 2. Write a program to display the first 7 multiples of 7.
a = 7
i = 1
while i<=7:
    print(a,end=",")
    a+=7
    i+=1

# 3. Write a program to find sum of first n-natural numbers for given n.
n = int(input("enter number: "))
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print("sum of 1 to",n,"is",sum)

# 4. Write a programme to print Fibonacci Series till n number (Accept n from user).
n = int(input("enter required terms of Fibonacci series: "))
i = 1
a = 1
b = 1
while i<=n:
    print(a,end=",")
    c=a+b
    a=b
    b=c
    i+=1


# 5. Find HCF of two numbers entered from user.
o = int(input("enter number 1: "))
p = int(input("enter number 2: "))
if o<p:
    a = o
    o = p
    p = a
a = None
i = p
while i>0:
    if o%i==0 and p%i==0:
        a=i
        break
    i-=1
print("HCF of",o,"&",p,"is",a)

# 6. Write programme to print only odd numbers from the given list L=[23,45,32,25,46,33,71,90].
L=[23,45,32,25,46,33,71,90]
i = 0
n = len(L)
while i<n:
    if L[i]%2!=0:
        print(L[i],end=",")
    i+=1

# 7. Write a programme to print all the vowels characters in the string ‘PYTHON’.
a = "PYTHON"
i = 0 
while i<len(a):
    if a[i] in ["A","E","I","O","U"]:
        print(a[i],end=",")
    i+=1








# n = int(input("enter required terms of Fibonacci series: "))
# a = 1
# b = 1
# i = 2 
# if n==1 :
#     print(a)
# elif n==2 :
#     print(a,",",b,sep="")
# else :
#     print(a,",",b,sep="",end="")
#     while i<=n:
#         c = a + b
#         a = b
#         b = c
#         print (c,end=",")
#         i+=1


