def hanoi(n, a, b, c):
    """
打印汉诺塔的解法：将n个盘子从柱子a移到柱子c，b为中间的柱子
    :param n: 盘子的个数
    :param a: 第一根柱子的名称
    :param b: 第二根柱子的名称
    :param c: 第三根柱子的名称
    :return: None
    """
    if n == 1:
        print(str(a) + '->' + str(c))  # 只有一个盘子，则直接移到c
        return
    hanoi(n - 1, a, c, b)  # 先将a里的n-1个盘子通过c移到b，则a中只剩下1个盘子
    print(str(a) + '->' + str(c))  # 将a中剩下的一个盘子直接移到c，此时b中的n-1个盘子不变
    hanoi(n - 1, b, a, c)  # 将b里的n-1个盘子通过a移到c，完成任务


if __name__ == '__main__':
    # a, b, c为3根柱子的名称
    a = 'A'
    b = 'B'
    c = 'C'
    hanoi(3, a, b, c)
    print(help(hanoi))
