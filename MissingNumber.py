#Input nums = [0,1,3]
#Find missing terms
# Op = 2
# Brute force
nums = [0,1,3]
for i in range(len(nums)):
    if i not in nums:
        print(i)
# Best Approach
print(sum([i for i in range(len(nums)+1)])- sum(nums))