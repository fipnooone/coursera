nDic = {}
for i in range(int(input())):
    nStr = input().split()
    nDic[nStr[0]] = nStr[1]
    nDic[nStr[1]] = nStr[0]
print(nDic[input()])
