# -*- coding: utf-8 -*-

from py2neo import Graph

graph = Graph(
    "http://localhost:7474",
    username="neo_db",
    password="123456"
)

with open("./raw_data/games.txt", 'r', encoding = 'utf-8') as f:
    for line in f.readlines():
        words = line.strip('\n').split(',')
        id, name, tags = words[0], words[1], words[2]
        print(words)
        graph.run("MERGE(g: Game{Id: '%s', Name: '%s', Tags: '%s'})" % (id, name, tags))


with open("./raw_data/relation.txt", 'r', encoding = 'utf-8') as f:
    for line in f.readlines():
        rela_array=line.strip("\n").split(",")
        print(rela_array)
        graph.run(
            "MATCH(u: Game), (v: Game) \
            WHERE u.Name='%s' AND v.Name='%s'\
            CREATE(u)-[r:%s{relation: '%s'}]->(v)\
            RETURN r" % (rela_array[2], rela_array[4], rela_array[0],rela_array[0])
        )