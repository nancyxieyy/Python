# input:[1, 2, 3, 4], output: 10

def SumOfList(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

print("sum of [1, 2, 3, 4] is ", SumOfList([1, 2, 3, 4]))
print("sum of [17, 5, 3, 5] is ", SumOfList([17, 5, 3, 5]))