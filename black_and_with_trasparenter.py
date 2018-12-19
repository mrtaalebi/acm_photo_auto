from PIL import Image
import numpy as np
import os
from scipy import ndimage


def trans_back(data):
    converted = []
    for d in data:
        if d[0] * 0.33 + d[1] * 0.33 + d[2] * 0.33 >= 200:
            converted.append((255, 255, 255, 0))
        else:
            converted.append(d)
    return converted


for f in os.listdir("{}/{}".format(os.getcwd(), "logos")):
    img = Image.open("{}/{}".format("logos", f))
    img = img.convert("RGBA")
    data = img.getdata()
    trans = trans_back(data)
    trans2 = []
    for t in trans:
        if t[3] != 0:
            trans2.append((255, 255, 255, 255))
        else:
            trans2.append((0, 0, 0, 0))
    trans3 = ndimage.gaussian_filter(trans2, 0.5)    
    trans5 = []
    for t in trans3:
        trans5.append((t[0], t[1], t[2], t[3]))
    img.putdata(trans5)
    img.save('new_logos/{}'.format(f.split('.')[0]), 'JPEG')
    print(f)

