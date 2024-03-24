import numpy as np
import cv2

img = np.zeros((400, 400, 3), np.uint8)
img.fill(90)


text = 'Hello, OpenCV!'


cv2.putText(img, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 80), cv2.FONT_HERSHEY_PLAIN,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 120), cv2.FONT_HERSHEY_DUPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 160), cv2.FONT_HERSHEY_COMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 200), cv2.FONT_HERSHEY_TRIPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 240), cv2.FONT_HERSHEY_COMPLEX_SMALL,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 280), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.putText(img, text, (10, 320), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
  1, (0, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('My Image', img)
cv2.imwrite('my.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


