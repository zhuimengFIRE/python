
# == 值相同
# is 是比较两个引用是否指向同一个对象
a = [1,2,3]
b = a
a == b # true
a is b # ture

c = copy.deepcopy(a)
a == c # true
a is c # false
