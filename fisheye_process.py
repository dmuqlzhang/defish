from defish import Defisheye
import glob
import os
import numpy as np
import cv2
def defishprocess(img, img_out, dtype = 'equalarea',format ='circular',fov=180, pfov= 120):
    # dtype = 'linear'
    # format = 'circular'
    # fov = 180
    # pfov = 120
    img = cv2.imdecode(np.fromfile(img, dtype=np.uint8), -1)
    # radius = (1920-92*2)/2
    radius = 868

    obj = Defisheye(img, dtype=dtype, format=format, fov=fov, pfov=pfov, radius = radius)
    obj.convert(img_out)
    return
if __name__ == '__main__':
    # img = r"C:\Users\zhangqinlu\Web\DownloadFiles\2020-12-24\01000000270000000\750.jpg"
    # img_out = f"example3_{dtype}_{format}_{pfov}_{fov}.jpg"
    # defishprocess(img, img_out)
    dtype = 'linear'
    format = 'fullframe'
    fov = 182
    pfov = 144
    # fov = 178
    # pfov = 130

    img_list = glob.glob(os.path.join(r'D:\酒录像\异常\out', r'*\*.jpeg'))
    for ind, i in enumerate(img_list):
        out_name = i.split('\\')[-1]
        out_path = os.path.join(r'D:\酒录像\异常\out\defish', i.split('\\')[-2])
        os.makedirs(out_path, exist_ok=True)
        print(i, out_path, out_name)
        defishprocess(i, os.path.join(out_path, out_name.replace('.jpeg', '.jpg')), dtype = 'equalarea', fov=fov, pfov= pfov)