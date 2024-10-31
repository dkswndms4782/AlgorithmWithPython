import re

t = input()
p = input()
res = re.findall(p, t)
print(len(res))