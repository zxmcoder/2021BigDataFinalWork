# -*- coding: utf-8 -*-

# ans = []
# with open("raw_data/games_info.txt", 'r', encoding = 'utf-8') as f:
#     for line in f:
#         ans.append(line.strip('\n').strip(' ').strip('\t'))
# for e in ans:
#     if len(e) == 0:ans.remove(e)
#
# final_ans = []
# i = 0
# while i < len(ans):
#     if ans[i][0].isdigit() and ans[i][1] != 'D':
#         j = i + 1
#         tmp = [ans[i]]
#         while j < len(ans) and not(ans[j][0].isdigit() and ans[j][1] != 'D'):
#             tmp.append(ans[j])
#             j += 1
#         final_ans.append('/'.join(tmp))
#         i = j
# with open('raw_data/games1.txt', 'w+', encoding = 'utf-8') as f:
#     for e in final_ans:
#         f.write(e + '\n')


# ans = []
#
# with open("raw_data/games1.txt", 'r', encoding = 'utf-8') as f:
#     for line in f:
#         s1 = line.replace(' ', ',', 1)
#         s2 = s1.replace('/', ',', 1)
#         ans.append(s2)
#
# with open("raw_data/games1.txt", 'w+', encoding = 'utf-8') as f:
#     for e in ans:
#         f.write(e)
# with open("raw_data/games1.txt", 'r', encoding = 'utf-8') as f:
#     for line in f:
#         if '/' not in line:
#             print(line)

# lines = []
#
# with open("raw_data/games.txt", 'r', encoding = 'utf-8') as f:
#     for line in f:
#         cnt = 0
#         i = 0
#         while cnt < 3:
#             if line[i] == '/': cnt += 1
#             i += 1
#         lines.append(line[0 : i - 1])
#
# # print(lines)
#
# with open("raw_data/games.txt", 'w+', encoding = 'utf-8') as f:
#     for line in lines:
#         f.write(line + '\n')
