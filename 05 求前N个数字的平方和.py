# 输入数字N
# 1^2 + 2^2 + 3^2 + .... + N^2

def get_N2(N):
    sum = 0
    for i in range(N + 1):
        sum += i**2
    return sum

print("sum of square 3: ", get_N2(3))
print("sum of square 4: ", get_N2(4))
print("sum of square 5: ", get_N2(5))