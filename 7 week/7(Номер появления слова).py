words = open('input.txt', 'r', encoding='utf8').read().split()
tDic = {}

for i in range(len(words)):
    if words[i] in tDic:
        print(tDic[words[i]], end=' ')
        tDic[words[i]] += 1
    else:
        print(0, end=' ')
        tDic[words[i]] = 1
