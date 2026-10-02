import sys
import numpy as np

# print("Python 版本：", sys.version)
# print("Python 路徑：", sys.executable)
# print("NumPy 計算結果：", np.array([1, 2, 3]) * 2)

def Circle(radius):
     # area = "%.1f" % (radius * radius * 3.14)

     area = f"{(radius * radius * 3.14):.1f}"
     
     length = "%.1f" % (2 * radius * 3.14)
     
     return area, length

area1, length1 = Circle(5)

print(f"area:{area1} length:{length1}")
