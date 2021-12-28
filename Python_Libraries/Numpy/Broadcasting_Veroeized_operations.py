import numpy as np

a = np.arange(3)
print(a)
print(a+5)
b = np.ones([3,3])
print(b)
print(a.shape)
print(b.shape)
print(a+b)# Nếu kích thước mảng k đồng nhất sẽ tự động được làm đồng nhất bằng cách thêm số hàng hoặc cột tương tự
#nhưng chỉ có thế là 1 hàng hoặc 1 cột
c = np.arange(3).reshape([3,1])
print(a+c)
x = np.array([[1,4],
             [2,5],
             [3,6]])
y = np.array([[1,2,3],
             [4,5,6]])
# print(x+y)#Error
#Comparing :
list_number = [1,2,3]
ll = np.array(list_number)
print(ll)
print(sum(ll)) #Python sum()
print(np.sum(ll))#Numpy sum() -> dung numpy sẽ nhanh hơn
# Create a massive Numoy array
massive_array = np.random.random(10000)
print(massive_array[:5])
print(massive_array.shape)
i = (sum(massive_array))
print(i)
j = (np.sum(massive_array))
print(j)
print(np.min(massive_array))
print(np.mean(massive_array)) # tính giá trị trung bình
print(np.max(massive_array))