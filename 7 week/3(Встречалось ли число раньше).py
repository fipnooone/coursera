arr = map(int, input().split())
nSet = set()
for a in arr:
    if a in nSet:
        print('YES')
    else:
        print('NO')
        nSet.add(a)
