import re
import os

text_path = 'C:/Users/j2x/Downloads/TEMP/test'
# 拿到文件夹下面的所有文件
text_list = os.listdir(text_path)
for path in text_list:
    with open(text_path + '\\' + path,'r',encoding="utf-8") as f:
        result = f.read()
        # 使用正则表达式去匹配标点符号、数字和英文
        result = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”。、~@#￥%……&*=-:]", "",result)
        result = re.sub('[a-zA-Z]','',result)
        result = re.sub('[\d]','',result) # [0-9]
        # result1 = demo(result)
        with open(text_path+ '\\' +path,'w',encoding="utf-8") as w:
            w.write(str(result))