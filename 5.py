"""
运用Monte Carno 方法计算圆周率的近似值。
"""
import random

count = 0  # 用于计数落在单位圆内点的个数
times = 100000  # 设定模拟次数
for i in range(times):
    x = random.random()  # 随机生成两个0~1之间的数，作为点的坐标(x, y)
    y = random.random()
    if x ** 2 + y ** 2 < 1:  # 计数落在单位圆内的点
        count = count + 1
print('pi = ' + str(4 * count / times))  # 单位圆内点的个数与总点数之比约等于圆面积与正方形面积之比，从而算出圆周率
