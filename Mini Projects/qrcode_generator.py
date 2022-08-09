import cv2
import numpy as np
import qrcode
from PIL import Image
# Generating QR code
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
source=str(input("Enter the source to generate Qrcode: "))
qr.add_data(source)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
name=str(input("Enter the name of the file to save: "))
img.save(name+".png")
print("Qrcode generated successfully")
print("Qrcode saved as "+name+".png")

# Reading QRcode
qr_img=cv2.imread(name+".png")
qr_det=cv2.QRCodeDetector()
data,bbox,rectifiedImage = qr_det.detectAndDecode(qr_img)
def display(im, bbox):
    n = len(bbox)
    for i in range(n):
        cv2.line(im, tuple(bbox[i][0]), tuple(bbox[(i+1)%n][0]), (255,0,0), 2)
    cv2.imshow('qr_code', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(qr_img, bbox)
    rectifiedImage=np.uint8(rectifiedImage)
    cv2.imshow('rectified QR code',rectifiedImage)
else:
    print("QR code not detected")
    cv2.imshow('rectified QR code',qr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
