"""
根据ABC三人描述，推测他们帽子的颜色
"""
from collections import Counter

conditions = []  # 用于存储所有可能的情况
for A_hat in ['r', 'w']:  # 遍历所有情况，'r’表示红帽子，'w'表示白帽子
    for B_hat in ['r', 'w']:
        for C_hat in ['r', 'w']:
            A_see = {'B': B_hat, 'C': C_hat}  # 记录A、B、C、看到的结果
            B_see = {'A': A_hat, 'C': C_hat}
            C_see = {'A': A_hat, 'B': B_hat}
            if (A_hat == 'w') + (B_hat == 'w') + (C_hat == 'w') == 3:  # 白帽子只有两顶，3人不可能都是白帽子
                continue
            elif Counter(A_see.values())['w'] == 2 or Counter(B_see.values())['w'] == 2 or \
                    Counter(C_see.values())['w'] == 2:  # 若看到另外两人都是白帽子，则能确定自己是红。故不可能。
                continue
            elif B_see['C'] == 'w':  # 由A所说知，B、C中至少一顶红帽子。若C是白帽子，则B能确定，故舍去
                continue
            elif C_see['B'] == 'w':  # 仅根据A所说的，C还不能确定自己的帽子，同B
                continue
            else:  # 剩余的情况均满足要求，以字典的形式保存到列表中
                conditions.append({'A': A_hat, 'B': B_hat, 'C': C_hat})

print('Possible conditions: {}'.format(conditions))  # 打印出所有可能的结果
C_set = []  # 总结出C可能戴的帽子
for e in conditions:
    C_set.append(e['C'])
C_set = set(C_set)
print('C: {}'.format(C_set))  # 打印C可能的帽子集合
