import cv2
import time

path = "C:\\path\\to\\image\\"
destination = "C:\\path\\to\\destination\\image-name.png"
src = cv2.imread(path + "0.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", src)

scale_percent = 50

new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

dsize = (new_width, new_height)

output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
cv2.waitKey(0)
