# def unique_values(a_dict:dict)-> dict:


all_key_pairs = []
unique_values = list(set(d1.values()))

d1 = {'Z': 3, 'P': 3, 'E': 2, 'G': 0, 'T': 5, 'L': 1, 'Q': 0}
count = {}

for v in d1.values():
    if v in count:
        count[v] += 1
    else:
        count[v] = 1
for k, v in count.items():
    if v == 1:
        print(k)
