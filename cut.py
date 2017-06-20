import cv2
import os

img = cv2.imread('plates_to_test3/timg.jpg', -1)
print(img.shape)

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 125, 255, cv2.THRESH_BINARY)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


def sort_func(c1, c2):
    (x1, y1, w1, h1) = cv2.boundingRect(c1)
    (x2, y2, w2, h2) = cv2.boundingRect(c2)
    
    if x1 > x2:
        return 1
    elif y1 > y2:
        return 1
    else:
        return -1


contours.sort(cmp=sort_func)

i = 0
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)

    if 350 < w * h < 1500:
        dst = img[y:y + h, x:x + w]  # 输出该区域
        dir = 'plates_to_test3/charOut/'
        os.system('mkdir -p ' + dir)
        cv2.imwrite(dir + str(i) + 'ch.png', dst)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)  # 标注该区域
        i += 1
    print((x, y), (x + w, y + h))

cv2.imwrite('plates_to_test3/charOut/preview.png', img)
print(img.shape)
