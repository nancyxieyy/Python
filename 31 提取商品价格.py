content = """
小明上街买菜
买了1斤黄瓜花了8元；
买了2斤葡萄花了13.5元；
买了3斤白菜花了5.4元；
"""

# 要求提取(1、黄瓜、8)、(2、葡萄、13.5)、(3、白菜、5.4)

import re

for line in content.split("\n"):
    pattern = r"(\d)斤(.*)花了(\d+(\.\d+)?)元"
    match = re.search(pattern, line)
    if match:
        print(f"{match.group(1)}\t{match.group(2)}\t{match.group(3)}\n")