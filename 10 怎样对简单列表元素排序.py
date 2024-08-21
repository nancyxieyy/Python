# 简单列表：元素类型不是符合类型（列表/元组/字典）
# 形式1:[20, 50, 10, 40, 30]
# 形式2:['bb', 'ee', 'aa', 'dd', 'cc']

lista = [20, 50, 10, 40, 30]
listb = ['bb', 'ee', 'aa', 'dd', 'cc']

lista.sort()
print("lista变化了（升序）", lista)
listc = sorted(lista, reverse=True)
print("lista没有变化（降序）", listc)

