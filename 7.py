from itertools import combinations
import numpy as np


def f(a, b):
    """
通过交换a,b中的元素，使序列a元素的和与序列b元素的和之间的差最小
    :param a: 输入序列1
    :param b: 输入序列2
    :return: 交换后的序列1，交换后的序列2，两序列最终和的差
    """
    total = a + b  # total为两个序列的拼接结果

    count = 0
    # 用组合的方式找出a的所有可能结果，依次遍历
    for a_new in combinations(total, len(a)):
        a_new = list(a_new)
        b_new = total.copy()
        for e in a_new:
            b_new.remove(e)  # 计算此时与a_new对应的b_new

        d = abs(np.sum(a_new) - np.sum(b_new))  # 计算此时两个序列的和 的差 的绝对值
        if count == 0:  # 若是第一个循环，则直接保存结果。delta为两序列和的最小差值、a_ans和b_ans为最佳结果
            delta = d
            a_ans = a_new.copy()
            b_ans = b_new.copy()
        elif d < delta:  # 若当前差值小于最小差值，则更新结果
            delta = d
            a_ans = a_new.copy()
            b_ans = b_new.copy()

        count = count + 1

    return a_ans, b_ans, delta


# 测试序列
a_test = [100, 99, 98, 1, 2, 3]
b_test = [1, 2, 3, 4, 5, 40]

a_test_ans, b_test_ans, diff = f(a_test, b_test)
print('The result is: ')
print('a: {}'.format(a_test_ans))
print('b: {}'.format(b_test_ans))
print('Min difference of the two lists: {}'.format(diff))
