#此脚本能将PDF转化为PNG图像

import fitz

'''
# 将PDF转化为图片
pdfPath pdf文件的路径
imgPath 图像要保存的文件夹
zoom_x x方向的缩放系数
zoom_y y方向的缩放系数
rotation_angle 旋转角度
'''
def pdf_image(pdfPath,imgPath,zoom_x,zoom_y,rotation_angle):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    print ("打开PDF成功")
    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.save(imgPath+str(pg+253)+".png")
        print (imgPath+str(pg)+"DONE")
    pdf.close()
   
pdf_image(r"C:\Users\cu183\Desktop\Shimin\primary sources\农家女1997/Multipage_2021-12-23_161446.pdf",r"C:\Users\cu183\Desktop\Shimin\primary sources\1997png/",5,5,0)