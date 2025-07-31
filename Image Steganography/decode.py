from PIL import Image
import numpy as np

with Image.open("simage.png") as img:
    width,height=img.size
    data=np.array(img)
    
    
data=np.reshape(data,height*width*3)

data=data & 1

data=np.packbits(data)

for x in data:
    l=chr(x)
    if not l.isprintable():
        break
    print(l,end='')