words = open("input.txt", "r", encoding="utf8").read().split()
tDic = {}

for word in words:
    if word in tDic:
        tDic[word] += 1
    else:
        tDic[word] = 1

nSr = sorted(tDic, key=lambda x: tDic[x])
print(min(list(filter(lambda y: tDic[y] == tDic[nSr[-1]], nSr))))
