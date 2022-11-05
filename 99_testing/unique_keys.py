lis = [{"abc": "movies"}, {"abc": "sports"}, {"abc": "music"}, {"xyz": "music"}, {"pqr": "music"}, {"pqr": "movies"},
       {"pqr": "sports"}, {"pqr": "news"}, {"pqr": "sports"}]
s = set(val for dic in lis for val in dic.values())


print(s)