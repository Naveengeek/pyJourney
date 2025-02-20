# Given an array, print all missing numbers. N = len(arr)
# Input = [1,2,2,3,3,5]
# op = [4,6]
arr = [1,2,2,3,3,5]
s = set(arr)
op = []
for i in range(1,len(arr)+1):
    if i not in s:
        op.append(i)
print(op)
