import numpy as np 

vek = np.arange(1,6) #вектор 5 нат чисел 

m = np.zeros((3,3), dtype=int) # матриця 3х3 з нулів 

mrx = np.random.randint(1,11, size=(5, 5)) # матриця 5х5 з рандом 1-10 

mtrx = np.random.randint(0,2, size=(4, 4)) # 4x4 random 0-1 

array1 = np.random.randint(1,11, size=(5))
array2 = np.random.randint(1,11, size=(5))

plus = array1 + array2 
minus = array1 - array2
multi = array1 * array2

ary1 = np.random.random(size=(7))
ary2 = np.random.random(size=(7))

mul = np.dot(ary1 , ary2) # skalyar 

mrx1 = np.random.random(size=(2,2))
mrx2 = np.random.random(size=(2,3))

multiply = np.dot(mrx1,mrx2)

matrix = np.random.randint(1,11, size=(3,3))

matrix_inv = np.linalg.inv(matrix)

bef = np.random.randint(1,11, size=(4,4))

transp = bef.T

