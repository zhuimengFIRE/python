# 利用set转换为集合
a = set("abcdefg")
print(type(a))
print(a)

# 利用集合去重
a = [1,2,3,3,3,4,5]
b = set(a)
print(b)
a = list(b)
print(a)

# 利用集合求交集 并集 补集
a = "abcdefg"
b = set(a)
A = "deg"
B = set(A)
print(b&B) # 交集
print(b|B) # 并集
print(b-B) # 补集
