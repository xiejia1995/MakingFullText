import re


def extracttxt(txtpath):
    f = open (txtpath, encoding='utf-8')
    line = f.readline()
    XYlist=[]
    txtlist=[]
    while line:        
        line = f.readline()
        #读取TextBox信息行，加入列表
        if 'TextBox[' in line:
            #print (line, end = '')
            #TextBoxNum = re.findall('\d+', line[7:10])
            x=re.findall(r'[)],[[]x: (\d+),',line)
            y=re.findall(r'y: (\d+)[]]',line[40:58])
            #提取文本box左上角x和y的值
            strx="".join(x)
            stry="".join(y)
            #print (strx,stry)
            #STRxy = "".join(xy)
            #XYlist.append(str(xy))
            xy=(eval(strx),eval(stry))
            #xy值返回为数值，以免函数按字符排序。
            XYlist.append(xy)
        
        if 'textLine[' in line:
            txtline = re.findall(r'\((.*?)\)',line)
            STRtxtline = "".join(txtline)
            ttcont=(STRtxtline,)
            txtlist.append(ttcont)
    #print (Numlist, XYlist, txtlist)
    XYtxt = [i+j for i, j in zip(XYlist, txtlist)] 
    f.close()
    return XYtxt

def takeKlammerNum(infoline):
    num = re.findall(r'\[(.*?)\]',infoline)
    return num

def CompXY(XYtxt):
    Fxytxt=sorted(XYtxt, key=lambda XYtxt: XYtxt[1])
    #print (Fxytxt)
    #840, 1610,2680
    l1,l2,l3,l4=[],[],[],[]
    #print (Fxytxt[0][0])
    for i in Fxytxt:
        if i[0]<=990:
            l1.append(i)
        elif 840 < i[0] <= 1910:
            l2.append(i)
        elif 1610 < i[0] <= 2780:
            l3.append(i)
        elif i[0] > 2680:
            l4.append(i)
    #print (l1)
    txtl1=[x[2] for x in l1]
    txtl2=[x[2] for x in l2]
    txtl3=[x[2] for x in l3] 
    txtl4=[x[2] for x in l4]   
    txt1="".join(txtl1)
    txt2="".join(txtl2)
    txt3="".join(txtl3)
    txt4="".join(txtl4)
    txtcontent = txt1+txt2+txt3+txt4
    return txtcontent


for i in range (0,407):
    txtpath=r'C:\Users\cu183\Desktop\Shimin\OcrLiteOnnx-1.6.1\images\INPUT/'+ str(i) +'.png-result.txt'
    XYtxt=extracttxt(txtpath)
    txtcontent=CompXY(XYtxt)
    filename=r'C:\Users\cu183\Documents\GitHub\MakingFullText\data\Nongjianv_Baishitong\1993/'+ str(i) +'.txt'
    file = open(filename, "w", encoding='UTF-8')
    file.write(txtcontent)



