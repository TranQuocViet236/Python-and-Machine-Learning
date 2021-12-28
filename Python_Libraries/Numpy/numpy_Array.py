#Numpy(Numerical Python)
#syntax: import numpy as np
#create a array
import  numpy as np
x = np.array([1,2,3,4])
y= np.array([[1,2,3],
            [4.5,7,7.5]],dtype="float32")
print(y)
print(x.dtype) #Kiểu dữ liệu của các phần tử trong x
print(type(x)) # Kiểu dữ liệu của x
print(type(y))
print(y.shape) # out ra số hàng và số cột của y
print(y.ndim) # out ra số chiều của y
print(y.size) # out ra số lượng phần tử của y

#Các hàm có sẵn
#Hàm zero :
print(np.zeros([2,4],dtype=float))
#Hàm one:
print(np.ones([3,5],dtype=int))
#Hàm arange:
print(np.arange(0,20,2))
#Hàm full
print(np.full([2,4],8))
#Hàm linspace
print(np.linspace(1,10,5))