def queen(A, cur=0):
    """
八皇后问题解答
    :param A: list. 存储每一行放置皇后的位置。A的长度表示棋盘的边长
    :param cur: 当前需要放置皇后的行号
    """
    if cur == len(A):  # 当前行号达到A的长度，说明皇后已经全部放置完成，打印结果
        print(A)
        return 0
    for col in range(len(A)):  # 遍历当前行的每一列col，看是否可以放置皇后
        A[cur], flag = col, True  # 在当前行把皇后暂且放在第col列。flag为True时表示暂未发生冲突
        for row in range(cur):  # 遍历前面已经放置过的所有行
            if A[row] == col or abs(col - A[row]) == cur - row:  # 若前面已经在第col列放置过，或当前位置的斜方向已放置过，则产生冲突，flag=False，跳出循环
                flag = False
                break
        if flag:  # 若falg为True，则当前位置不冲突，继续放置下一位置；否则，有冲突，当前位置无效，继续循环。
            queen(A, cur + 1)


queen([None] * 8)
