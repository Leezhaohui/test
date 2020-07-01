# 安德医智笔试（网格中小山个数）
# def onesGroups(grid, queries):
#     n = len(grid)
#     group_num = 2
#     # 创建数组，标志网格中的元素是否被遍历过
#     flags = [[0 for _ in range(n)] for _ in range(n)]
#
#     # 判断周围是否还有满足条件的点，是则返回所有的点
#     def judge(i, j):
#         res = []
#         dots = [[i+1, j],[i-1, j],[i, j-1],[i, j+1]]
#         for dot in dots:
#             if dot[0] in range(n) and dot[1] in range(n) and \
#                flags[dot[0]][dot[1]] == 0:
#                 res.append(dot)
#         if not res:
#             return False
#         else:
#             return res
#
#     # 深度优先搜索与当前点连接的点, 并将其标志为group_num
#     def dfs(i, j):
#         # 定义一个列表，用来盛放与当前搜索点为一个group的点
#         dot_group = []
#         def search(i, j):
#             # 网格中为0的点不进行搜索，并将其flag标记为1
#             if grid[i][j] == 0:
#                 flags[i][j] = 1
#                 return
#             # 网格中为1的点将其加入当前group并将其flag标记为1
#             if flags[i][j] == 0:
#                 dot_group.append([i, j])
#                 flags[i][j] = 1
#             # 搜索终止条件
#             if not judge(i, j):
#                 return
#             # 对周围满足条件的点进行递归搜索
#             for dot in judge(i, j):
#                 search(dot[0], dot[1])
#         search(i, j)
#         # 将搜索到的所有点进行group标记
#         for dot in dot_group:
#             grid[dot[0]][dot[1]] = group_num
#
#     # 遍历网格中所有的点，每个点都进行深度优先搜索并进行group_num标注, 每遍历完一组，group_num加1
#     def travel():
#         nonlocal group_num
#         for i in range(n):
#             for j in range(n):
#                 dfs(i, j)
#                 group_num += 1
#     travel()
#
#     # 统计group_num的组数以及每一组中元素的个数
#     def count():
#         group_num_dict = {}
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] > 1:
#                     if grid[i][j] not in group_num_dict:
#                         group_num_dict[grid[i][j]] = 1
#                     else:
#                         group_num_dict[grid[i][j]] += 1
#         # 以元素个数为key重新组合
#         group_num_dict_f = {}
#         for key, value in group_num_dict.items():
#             if value not in group_num_dict_f:
#                 group_num_dict_f[value] = 1
#             else:
#                 group_num_dict_f[value] += 1
#         return group_num_dict_f
#
#
#     num_dic = count() # 得到以1个数为key，对应group个数为value的字典
#     result = []
#     for num in queries:
#         if num in num_dic:
#             result.append(num_dic[num])
#         else:
#             result.append(0) # 没有相应个数的group则添加0
#     return result

# numpy 处理nan值
# import numpy as np
# def trans_nan(arr):
#     # 对于每一列
#     for i in range(arr.shape[1]):
#         col = arr[:, i]
#
#         # 得到这一列不是nan值的其余值并计算均值
#         col_tmp = col[col==col]
#         mean = col_tmp.mean()
#
#         # 将这一列中的nan值赋值为均值
#         col[np.isnan(col)] = mean
#
# arr = np.arange(12).reshape((3, 4)).astype(float)
# arr[1, 2:] = np.nan
# print(arr)
# trans_nan(arr)
# print(arr)
