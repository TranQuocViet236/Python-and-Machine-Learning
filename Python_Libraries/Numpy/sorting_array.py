import numpy as np

x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))
print(np.argsort(x)) # return về index của mảng sau khi sắp xếp
np.random.seed(42)
MatA = np.random.randint(0,10,size= (4,6))
print(MatA)
print(np.sort(MatA,axis=0)) # Sắp xếp theo cột
print(np.sort(MatA,axis=1))