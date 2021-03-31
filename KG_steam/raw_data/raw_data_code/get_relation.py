# -*- coding: utf-8 -*-

id2title = dict()
tag2id = dict()

with open('raw_data/games.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip('\n')
        id = int(line[0 : line.find(',')])
        title = line[line.find(',') + 1 : line.rfind(',')]
        id2title[id] = title
        tags = line[line.rfind(',') + 1 : ].split('/')
        # print(tags)
        for tag in tags:
            if tag not in tag2id:
                tag2id[tag] = []
            tag2id[tag].append(id)



# print(len(id2title))
# for k, v in tag2id.items():
#     print(k, v)

# 生成relation.txt文件
lines = []

for k, v in tag2id.items():
    if len(v) >= 2:
        for i in range(0, len(v)):
            for j in range(i + 1, len(v)):
                lines.append([k, v[i], id2title[v[i]], v[j], id2title[v[j]]])

with open('raw_data/relation.txt', 'w+', encoding = 'utf-8') as f:
    for line in lines:
        for e in line:
            f.write(str(e) + ',')
        f.write('\n')



