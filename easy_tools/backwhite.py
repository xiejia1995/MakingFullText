#此脚本能将图片转换为黑白，并适当增强颜色及对比度

from PIL import Image, ImageEnhance

def Chuli(InputPath, OutputPath):
    im  =  Image.open(InputPath)
    # convert to grey level image 
    Lim  =  im.convert("L")
    Lim = Lim.convert('RGB')
    Enhance1 =ImageEnhance.Color(Lim)
    img= Enhance1.enhance(4)
    Enhance2 =ImageEnhance.Contrast(img)
    img=Enhance2.enhance(1.6)
    img.save(OutputPath)
    return img
    
for i in range(407,505):
    i=str(i)
    InputPath=r'C:\Users\cu183\Desktop\Shimin\primary sources\1997png/'+ i +'.png'
    OutputPath=r'C:\Users\cu183\Desktop\Shimin\primary sources\1997BW/' + i +'.png'
    Chuli(InputPath,OutputPath)
    print ("图片"+i+"黑白版保存成功")
