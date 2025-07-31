import numpy as np;
from PIL import Image

message="hari bhai"

bMsg=''.join(["{:08b}".format(ord(x)) for x in message])
bMsg=[int(x) for x in bMsg]

bMsgLen=len(bMsg)


with Image.open("image.png") as img:
    width,height=img.size
    data=np.array(img)


data=np.reshape(data,width*height*3)

data[:bMsgLen]=data[:bMsgLen] & ~np.uint8(1) | bMsg

data=np.reshape(data,(height,width,3))

new_img=Image.fromarray(data)
new_img.save("simage.png")
new_img.show()