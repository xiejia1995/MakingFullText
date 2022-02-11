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
    
for i in range(1,121):
    i=str(i)
    InputPath='C:/Users/j2x/Downloads/TEMP/OcrLiteOnnx-1.6.1/images/NJN1997/njn'+ i +'.png'
    OutputPath='C:/Users/j2x/Downloads/TEMP/OcrLiteOnnx-1.6.1/images/NJN1997blackandwhite/' + i +'.png'
    Chuli(InputPath,OutputPath)
    print ("图片"+i+"黑白版保存成功")
