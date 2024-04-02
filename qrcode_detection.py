############################
# QR CODE DETECT AND DECODE
############################

import cv2 as cv
import numpy as np

src = cv.imread("qr.jpg")

# Qr kodu gri skalaya çevirme
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

qrcoder = cv.QRCodeDetector()

codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(gray)
print(points)

result = np.copy(src)
cv.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 2)

# qr code information
print("qrcode information is :\n%s" % codeinfo)
cv.imshow("result", result)
cv.waitKey(1)
