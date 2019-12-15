cnds = open('input.txt', 'r', encoding='utf8').read().split('\n')
outF = open('output.txt', 'w', encoding='utf8')
tDic = {}
all = 0
for cnd in cnds:
    if cnd in tDic:
        tDic[cnd] += 1
    else:
        tDic[cnd] = 1
    all += 1
dicSorted = sorted(tDic, key=lambda x: tDic[x])
if (tDic[dicSorted[-1]] / all) * 100 > 50:
    outF.write(dicSorted[-1])
    outF.write('\n')
else:
    outF.write(dicSorted[-1])
    outF.write('\n')
    outF.write(dicSorted[-2])
