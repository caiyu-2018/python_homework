def f(num):
    """
计算阶乘
    :param num: 输入
    :return: num的阶乘
    """
    if num == 1:
        return 1
    else:
        return num * f(num - 1)


if __name__ == '__main__':
    print(f(100))
    print(help(f))
