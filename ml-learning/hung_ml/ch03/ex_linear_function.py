"""y = 3x - 18：一次函數的計算與圖形"""

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 3 * x - 18


# 截距：x = 0 時的 y（y 截距）、y = 0 時的 x（x 截距，即方程式 3x - 18 = 0 的解）
y_intercept = f(0)
x_intercept = 18 / 3
print(f"斜率 = 3，y 截距 = {y_intercept}，x 截距 = {x_intercept}")

for x in [0, 2, 6, 10]:
    print(f"f({x}) = {f(x)}")

# 畫圖：NumPy 陣列一次算出所有點的 y
x = np.linspace(-2, 12, 100)
y = f(x)

plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # macOS 中文字型
plt.plot(x, y, label="y = 3x − 18")
plt.scatter([0, x_intercept], [y_intercept, 0], color="red", zorder=3)
plt.annotate(f"(0, {y_intercept})", (0, y_intercept), textcoords="offset points", xytext=(8, -4))
plt.annotate(f"({x_intercept:g}, 0)", (x_intercept, 0), textcoords="offset points", xytext=(8, -12))
plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.title("一次函數 y = 3x − 18")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
