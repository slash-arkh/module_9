from itertools import combinations

def all_variants(text):
    for i in range(1, len(text)+1):
        test = []
        combi = combinations(text, i)
        test.extend(combi)
        for j in test:
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    if i == 'ac':
        continue
    print(i)