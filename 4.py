"""
有一个五位数abcde，乘以4以后变成edcba，abcde是多少?
"""
# 5位数abcde乘4是5位数edcba，说明a是偶数。则a只能是2，那么e可以从8开始。要满足乘4后还是5位数，最大值为24999，从而确定候选范围如下。
for res in range(20008, 25000):
    a = res // 10000  # 分别计算出原数字的a,b,c,d,e5位
    b = res % 10000 // 1000
    c = res % 1000 // 100
    d = res % 100 // 10
    e = res % 10

    new = 10000 * e + 1000 * d + 100 * c + 10 * b + a  # 新数字为5位数调换顺序
    if 4 * res == new:  # 若新数字刚好为原数字4倍，满足要求，则打印结果
        print(res)
