# def sumnum(x):
#     a = 0
#     num = int(x)
#     if num<10 : return num
#     for d in x :
#         a = a + int(d)
#         # print(a)
#     return a
# x = "23999996"
# s = sumnum(x)
# while s > 1 :
#     s = sumnum(str(s))
#     print(s)

# ab = open('reading.txt')
# count = 0
# for line in ab: 
#     count = count + 1
# print('line count: ', count)

# ab = open('reading.txt')
# c = ab.read() 
# print(c)
# print(len(c))
# print(c[:100])

# ab = open('reading.txt')
# for line in ab :
#     if line.startswith('G:-') :
#         print(line)

# x, y, *z = input(" Enter any 3 numbers:- ").split()
# print(x)
# print (y)
# print(z)

x = 5
y = 3
print(x,y)
# z = x 
# x=y
# y = z
[x, y] = [y, x]

print(x,y)