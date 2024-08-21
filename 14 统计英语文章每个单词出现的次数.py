word_count = {}

with open("./14 随便找的文章.txt") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()

        # 如果单词不在字典中，把单词在字典中的数字变成0
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

print(word_count)
# 排序字典的内容,只看前十个
print(
    sorted(
        word_count.items(),
        key=lambda x:x[1],
        reverse=True
        )[:10]
)