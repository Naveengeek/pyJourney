# Given an array, find the position of two numbers where their sum is equal to targeted sum
ip = [2,4,5,7,9]
t = 9
# op = [0,3]
# # bruteForce
# for i in range(len(ip)-1):
#     v = t-ip[i]
#     if v in ip[i+1:]:
#         print(i,) 2 0
s = {}
for i,v in enumerate(ip):
    s[v] = i
    req = t-v
    if req in s:
        print(s[req], i)