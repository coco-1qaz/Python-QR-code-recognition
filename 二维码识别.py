from pyzbar.pyzbar import decode
import webbrowser
import pyzbar
import cv2
import numpy as np

video = cv2.VideoCapture(1)
  
while True:
    ret, frame = video.read()

    if ret == False: 
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    barcodes = decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect

        cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 2)
        cv2.putText(frame, str(barcode.data, 'UTF-8'), (x, y - 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        print(barcode)

        cv2.waitKey(40)

        s = "y"
        t = "Y"

        if "http" in str(barcode.data):
            sr = input("是否打开?(y/n)")

            if sr == s or sr == t:
                webbrowser.open_new_tab(barcode.data)
                print("is open")

            else:
                print("ok")

    cv2.imshow("p", frame)
    
    if cv2.waitKey(20) & 0xFF==ord(' '):
        break

cv2.destroyAllWindows()