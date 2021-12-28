import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
B = np.array([[6,5],
              [4,3],
              [2,1]])

print(A.dot(B)) # Tích vô hướng của A và B (VD: 1*6 + 2*4 + 3*2 = 20)
print(A@B) # cũng là tích vô hướng
print((B.T).dot(A))
print(B.T@A)

##Example
np.random.seed(0)
sales_amount = np.random.randint(0,29,size= (5,3))
print(sales_amount)
#để học thêm pandas
