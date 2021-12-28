#Standard Deviation and Variance : Độ lệch chuẩn và phương sai
#Standard Deviation: is a measure of how spread out of numbers are:
#Thước đo độ phân tán dữ liệu
#Variance: Trung bình của tổng bình phương(squared) sự sai khác giữa bản thân nó và giá trị trung bình
# Độ lệch chuẩn = căn bậc 2 (square root) của phương sai
import numpy as np

dog_height = [600,470,170,430,300]
dog_height = np.array(dog_height)
print(np.var(dog_height))
std = np.sqrt(np.var(dog_height))
print(std)