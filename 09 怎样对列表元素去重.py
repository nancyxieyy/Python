# 输入，包含重复元素的原始列表：
# [10, 20, 30, 10, 20]
# 返回：
# [10, 20, 30]

list = [10, 20, 30, 10, 20]

def remove_numbers(list):
    result = []
    for item in list:
        # 如果item不在结果列表中，则把它放进去
        if item not in result:
            result.append(item)
    return result

print("The output is ", remove_numbers(list))