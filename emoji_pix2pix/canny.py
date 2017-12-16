import cv2
import glob
import numpy as np

fl = glob.glob('RGB_emoji/*.jpg')

for f in fl:
    img = cv2.imread(f)
    img_canny = cv2.Canny(img,140,160)
    imgsave = np.ones_like(img_canny)
    imgsave[img_canny==255] = 0
    imgsave[img_canny==0] = 255
    
    cv2.imwrite('canny/'+f.split('/')[-1],imgsave)
