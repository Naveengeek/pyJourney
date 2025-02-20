# Find all the numbers in a list smaller than current number
# eg = [1,2,2,3,4]
# op = [0,1,1,2,3]
# 1 is the smallest and no other number smaller than current
eg = [1,2,2,3,4]
s = sorted(eg)
h = {}
for i, v in enumerate(s):
    if v not in h:
        h[v] = i
ans = []
for i in eg:
    ans.append(h[i])
print(ans)