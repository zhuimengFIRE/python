from functools import reduce

# map函数，第一个参数为函数名，后面为可迭代对象

# 一个参数
res = map(lambda x:x*x, [1,2,3])
for temp in res:
    print(temp)

# 两个参数
res1 = map(lambda x,y:x+y,[1,2,3],[4,5,6])
print(list(res1))


def test(x,y):
    return x,y

aa = [1,2,3,4,5,6,7]
bb = ['Sun','M','T','W','T','F','S']
cc = map(test,aa,bb)
print(list(cc))


# filter 过滤数据
# 过滤掉与2取余为0的数
res2 = filter(lambda x:x%2,[1,2,3,4])
print(list(res2))

# reduce 可以实现累加 矩阵
res3 = reduce(lambda x,y:x+y,[1,2,3,4])
print(res3)

res4 = reduce(lambda x,y:x+y,[1,2,3,4,5],6)
print(res4)

res5 = reduce(lambda x,y:x+y,['aa','bb','cc'],'dd')
print(res5)

# sorted
a = [123,312,1,23,435,23,56,43,44,56,8,618,67,867,9]
# # 从小到大排序
# a.sort()
# print(a)
#
# # 从大到小排序
# a.sort(reverse=True)
# print(a)

# 正向
print(sorted(a))
# 逆向
print(sorted(a,reverse=1))






