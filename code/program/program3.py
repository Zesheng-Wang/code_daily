import os
from pyzbar.pyzbar import decode
from MyQR import myqr
from PIL import Image

image = './images/timg.JPG'
img = Image.open(image)
barcodes = decode(img)
for barcode in barcodes:
    url = barcode.data.decode('utf-8')


myqr.run(
    words=url,  # 二维码内容，链接或者句子
    version=10,  # 二维码大小 [1, 40]
    level='H',  # 二维码纠错级别，范围{L,M,Q,H}
    picture='./images/girl.gif',  # 自定义二维码背景图
    colorized=True,  # 二维码背景颜色，默认False，黑白
    contrast=1.0,  # 对比度
    brightness=1.0,  # 亮度
    save_name=None,  # 二维码名称
    save_dir=os.getcwd()  # 二维码路径
)
