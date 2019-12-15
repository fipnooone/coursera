letS = open("input.txt", "r", encoding="utf8")
myLets = {}
for let in letS.read().split():
    myLets[let] = myLets.get(let, 0) + 1
myLets = [(fr, lt) for lt, fr in myLets.items()]
myLets.sort(key=lambda x: (-x[0], x[1]))
for i in range(len(myLets)):
    print(myLets[i][1])
