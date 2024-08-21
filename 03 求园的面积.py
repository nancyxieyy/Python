# 输入半径，返回圆的面积
import math

def get_AreaOfCircle(radius):
    return round(math.pi * radius ** 2, 2)

print("半径为2的圆的面积为： ", get_AreaOfCircle(2))