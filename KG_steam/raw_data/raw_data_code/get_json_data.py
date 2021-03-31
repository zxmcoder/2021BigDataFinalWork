# -*- coding: utf-8 -*-

games = []

with open('./raw_data/games.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip('\n')
        games.append(line)

relations = []

with open('./raw_data/relation.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip('\n')
        relations.append(line)

json_data = {'data': [], "links": []}

idx = 0
game2idx = {}

for game in games:
    game_array = game.split(',')

    game_item = {}
    game_item['name'] = game_array[1]
    game_item['id'] = int(game_array[0])
    game_item['tags'] = game_array[2]
    game2idx[game_array[0]] = idx
    idx += 1
    json_data['data'].append(game_item)
for relation in relations:
    relation_item = {}

    relation_array = relation.split(',')

    relation_item['source'] = game2idx[relation_array[1]]

    relation_item['target'] = game2idx[relation_array[3]]
    relation_item['value'] = relation_array[0]
    json_data['links'].append(relation_item)

print(json_data)

with open('./static/data.json', 'w+', encoding = 'utf-8') as f:
    f.write(str(json_data))
