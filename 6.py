"""
根据普查员和女士对话，推测孩子的年龄
"""
import numpy as np
from collections import Counter

age_l = []  # age_l用于存储3人年龄乘积为36的情况
age_set = []  # age_set用于存储满足要求的3人年龄的集合（无序）。以防止重复存储年龄一样、顺序不同的情况
for age1 in range(1, 18):
    for age2 in range(1, 18):
        for age3 in range(1, 18):
            if age1 * age2 * age3 == 36:
                if {age1, age2, age3} not in age_set:  # 若满足条件的年龄未存储过，则存储
                    age_set.append({age1, age2, age3})
                    age_l.append([age1, age2, age3])

age_array = np.array(age_l)
age_sum = np.sum(age_array, axis=1)  # 求所有情况的年龄和

m = Counter(age_sum)  # 数出每种和的个数。由题，知道年龄和还不足以判断年龄，所以一定存在多个和与正确情况相同
key_l = []  # 记录有多个结果相同的和
for key, value in m.items():
    if value > 1:
        key_l.append(key)

ans = []
for key in key_l:  # 对于这些可能的和，找出其对应的年龄存储到ans中
    for i in range(age_array.shape[0]):
        if age_sum[i] == key:
            ans.append(age_array[i])

for elem in ans:  # 由题，有一个年龄最大的孩子，找出最大值唯一的情况，打印。即得到结果
    maxi = np.max(elem)
    if np.sum(elem == maxi) == 1:
        print(elem)
