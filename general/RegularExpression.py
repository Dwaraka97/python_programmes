import re
x="i have 3 numbers 45 43 and 64"
y=re.findall('[0-9]+',x)
print(y)
z="Find: me a solution: for this problem"
y=re.findall('^F.+?:',z)
print(y)
