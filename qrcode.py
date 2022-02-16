# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

#read qr code
#create a text file

from re import A
import cv2
import webbrowser
from cv2 import line
from pyzbar.pyzbar import decode
import datetime
import numpy as np


#variables for cam
webcam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, img = webcam.read()
    data, code, _ = detector.detectAndDecode(img)
    if data:
        rd = data
        #create a txt file
        with open ("qrcodescannedresults.txt", 'a') as file:
            file.write(f'Scanned QR code results: {rd}')
            file.write('data recorded at' (datetime.datetime.now()))
        break
    for barcode in decode(img):
        rd = data
        txt = barcode.data.decode ('utf-8')
        print(txt)
        lne= np.array ([barcode.polygon], np.int32)
        lne = lne.reshape ((-1,1,2))
        cv2.polylines(img, [lne], True, (230, 67, 107),5 )
        with open("qrcodescannedresults.txt", 'a') as file:
            file.write(f'Scanned QR code results: {rd}')
            file.write('data recorded at' (datetime.datetime.now()))
            webcam.release (txt)
            cv2.destroyAllWindows
        break
    cv2.imshow('QR Code Scanner here!', img)
    if cv2.waitKey(1) == ord('a'):
        break

go = webbrowser.open((str(rd)))
webcam.release (rd)
cv2.destroyAllWindows


