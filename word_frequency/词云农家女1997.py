#新词云
import jieba
import wordcloud

def takeSecond(elem):
    return elem[1]

def createWordCloud(text):
    w=wordcloud.WordCloud(font_path="C:/Windows/Fonts/simhei.ttf",width=600,height=400,background_color="white")
    w.generate(text)
    w.to_file("C:/Users/j2x/Downloads/TEMP/test/wordcloudNJN1997.jpg")

def main():
    path = "C:/Users/j2x/Downloads/TEMP/test/NJN1997.txt"
    file = open(path,"r",encoding="utf-8")
    text=file.read()
    file.close()

    words = jieba.lcut(text)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue            
        else:
            rword = word
        counts[rword] = counts.get(rword,0) + 1

    file = open("C:/Users/j2x/Downloads/TEMP/test/excludes.txt","r", encoding='UTF-8')
    excludes =file.read().split(",")
    file.close

    for delWord in excludes:
        try:
            del counts[delWord]
        except:
            continue

    items = list(counts.items())
    items.sort(key = takeSecond,reverse=True)    

    for i in range(50):
        item=items[i]
        keyWord =item[0]
        count=item[1]
        print("{0:<10}{1:>5}".format(keyWord,count))

    createWordCloud(str(items[0:80]).replace("'", ""))

main()
