import re
str="TextBox[0](+padding)[score(0.765240),[x: 1145, y: 322], [x: 1405, y: 336], [x: 1317, y: 1952], [x: 1057, y: 1938]]"

x=re.findall(r'[)],[[]x: (\d+),',str)
y=re.findall(r'y: (\d+)[]]',str[40:58])
print (x,y)