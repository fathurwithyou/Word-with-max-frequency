# Enter the input separated with space!
lst = list(map(str, input().split()))
dicts = {}
maxi = 0
for i in lst:
    if i not in dicts:
        dicts[i] = 1
    else:
        dicts[i] += 1
    maxi = max(maxi, dicts[i])

for i in lst:
    if dicts[i] == maxi:
        print(i, maxi)
        break
