iMax = int(input())
tSet = set(range(1, iMax + 1))
noSet = set()
while True:
    iN = input()
    if iN == 'HELP':
        break
    iN = set(map(int, iN.split()))
    if input() == 'YES':
        tSet &= iN
    else:
        noSet |= iN
print(*sorted(tSet - noSet))
