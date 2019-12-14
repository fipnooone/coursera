allDic = {}
allS = int(input())
for i in range(allS):
    for j in range(int(input())):
        newLang = input()
        if newLang in allDic:
            allDic[newLang].append(i)
        else:
            allDic[newLang] = [i]
allKnow = []
for lang in allDic.keys():
    if len(allDic[lang]) == allS:
        allKnow.append(lang)
print(len(allKnow), *allKnow, sep='\n')
print(len(allDic), *allDic, sep='\n')
