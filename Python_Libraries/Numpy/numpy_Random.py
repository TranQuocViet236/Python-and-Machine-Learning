import numpy as np
#seed
# np.random.seed(0) # có seed để gọi hàm rand luôn tạo ra 1 giá trị
# print(np.random.random([4,4]))
# print(np.random.normal(0,1,(3,3)))
# print(np.random.randint(1,10,[4,5]))
# print(np.random.rand(4,4))
x1 = np.random.randint(20,size  =6)
print(x1)
# print(x1[0],x1[-1],x1[4])
x2= np.random.randint(10,size = [3,4])
print(x2)
# print(x2[-1,-1])
# #slicing
# # x[start:stop:step]
# print(x1[0:3])
# print(x1[::2])
# print(x2[:2,:3])
# print(x2[:,:3])
# #Reshaping and transpose:
# grid = np.arange(1,10)
# print(grid)
# print(grid.shape)
# print(grid.reshape((3,3)))
# print(grid.reshape(9,1))
# #Transpose
# print(x2.T)
#Array concatenation andsplitting
#
# x = np.array([1,2,3])
# y = np.array([4,5,6])
# print(np.concatenate((x,y)))
# grid = np.array([[1,2,3],
#                  [4,5,6]])
# print(grid)
# print(np.concatenate((grid,grid))) # axis =0 by default
# print(np.concatenate((grid,grid),axis=1))
# #vertical stack
# x = np.array([1,2,3],
#              [4,5,6])
# print(np.vstack([x,grid]))
# #horizontally stack the arrays : hstack
# print(np.hstack([x,grid]))

x = np.array([1,2,3,99,69,3,2,1])
# print(np.split(x,[3,5]))
x1,x2,x3=np.split(x,[3,5])
print(x1)
print(x2)
print(x3)