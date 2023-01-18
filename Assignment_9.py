# Assignment_9
# python


# 1.	Perform all Inbuilt commands using numpy library: dtype, zero, random, empty, full, repeat, tile
import numpy as np
print("using command zeros")
# zeros(shape, dtype=float)
print(np.zeros((3,5),dtype=float))
print()
print("using command full")
# full(shape, fill_value, dtype=None)
print(np.full((2,3),6,dtype=float))
print()
print("using command empty")
# numpy.empty(shape, dtype=float, order='C', *, like=None)
print(np.empty((2,2),dtype=int))
print()
print("using command random.rand")
# random.rand(d0, d1, ..., dn) 
# Create an array no. in range [0,1)
print(np.random.rand(2,3)) 
print()
print("using command repeat")
# numpy.repeat(A: array_like, repeats: ArrayLike, axis=None)
x = np.array([[1,2],[3,4]])
print(np.repeat(x,[1, 5],axis = 1))
# tile(A: ArrayLike, reps: ArrayLike)
print()
print("using command tile")
a = np.array([[2,3],[4,5],[6,7]])
print(np.tile(a,[2,3]))


# 2.	Write a python program to perform all arithmetic operations on vector using numpy.
import numpy as np
v1 = input("Enter vector V1 like (x1,x2,...  ,xn) : ")
v2 = input("Enter vector V2 like (y1,y2,...  ,yn) : ")
a1,a2 = v1.strip("()").split(",") , v2.strip("()").split(",")
b1,b2 = list(map(float,a1)) , list(map(float,a2))
c1,c2 = np.array(b1) , np.array(b2)
print("V1 + V2",c1+c2,"V1 - V2",c1-c2,"V1 / V2",c1/c2,"V1 * V2",c1*c2,sep="\n")


# 3.	Write a python program to perform all arithmetic operations on matrix using numpy.
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,2,3],[0,1,4],[5,6,0]])
print("matrix addtion")
print(a+b)
print()
print("matrix subtraction")
print(a-b)
print()
print("matrix multiplication")
def mul(x,y):
    r = np.zeros((len(x),len(y[0])),dtype=float)
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(b)):
                r[i][j] += x[i][k] * y[k][j]
    return r
print(mul(a,b))
print()
print("matrix divison")
# find determinant of a matrix b
d = b[0][0]*(b[1][1]*b[2][2]-b[1][2]*b[2][1])-b[0][1]*(b[1][0]*b[2][2]-b[2][0]*b[1][2])+b[0][2]*(b[1][0]*b[2][1]-b[1][1]*b[2][0])
# find cofactor of a matrix
c1 = b[1][1]*b[2][2]-b[1][2]*b[2][1]
c2 = b[1][0]*b[2][2]-b[2][0]*b[1][2]
c3 = b[1][0]*b[2][1]-b[1][1]*b[2][0]
c4 = b[0][1]*b[2][2]-b[0][2]*b[2][1]
c5 = b[0][0]*b[2][2]-b[0][2]*b[2][0]
c6 = b[0][0]*b[2][1]-b[0][1]*b[2][0]
c7 = b[0][1]*b[1][2]-b[0][2]*b[1][1]
c8 = b[0][0]*b[1][2]-b[1][0]*b[0][2]
c9 = b[0][0]*b[1][1]-b[1][0]*b[0][1]
C = np.array([[c1,c2,c3],[c4,c5,c6],[c7,c8,c9]]) 
# find adj. of b
p = C.transpose()
q = np.array([[1,-1,1],[-1,1,-1],[1,-1,1]])
adj_b = p*q # adj. of b
inv_b = (1/d)*adj_b # matrix inverse
div = mul(a,inv_b) # matrix divison
print(div)


# 4.	Write a python program to read one csv file using pandas.
import pandas as pd
# pandas.read_csv('filepath/filename.csv')
a = pd.read_csv('C:/Users/bhumi/Desktop/username-or-email.csv')
print(type(a))


# 5.	Write a python program to create pandas series from a list
import pandas as pd
#  pandas.Series(data: DatetimeIndex, index: Axes | None = ..., dtype: ... = ...)
dictionary = {'a' : 1, 'b' : 2, 'c' : 3, 'd': 4,'e': 5}
print(pd.Series(dictionary))


# 6.	Write a python program to create pandas DataFrame. 
import pandas as pd
import numpy as np
dictionary ={'studentA' : [76, 82, 63, 94],'studentB' : [94, 53, 62, 71],'studentC' : [75, 66, 82, 74]}
a = np.array(['maths','physics','chemistry','english'])
print(pd.DataFrame(dictionary, index=a))


# 7.	Write a python program to check the number of maximum returned rows.
import numpy as np
a = np.array([[1,2],[3,9],[4,5]])
print(np.max(a,axis=0))


# 8.	Write a python program to print first 5 row and last 5 row from the DataFrame.
import pandas as pd
import numpy as np
a = pd.DataFrame({'A':np.random.randn(15),'B':np.random.randn(15),'C':np.random.randn(15)})
print("first 5 row from the DataFrame")
print(a.head(5))
print()
print("last 5 row from the DataFrame")
print(a.tail(5))