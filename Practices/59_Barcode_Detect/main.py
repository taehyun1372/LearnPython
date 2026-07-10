import cv2
import zxingcpp
from pathlib import Path

def test_cv2_detect(img_path):
    img = cv2.imread(img_path)
    
    detector = cv2.QRCodeDetector()
    retval, points = detector.detect(img)
    print(retval, points)
    data, points, _ = detector.detectAndDecode(img)
    print(data, points)
    
    results = zxingcpp.read_barcodes(img)
    if len(results) == 0:
        print("barcode not detected")
    else:
        for r in results:
            print(r.text)
            
def test_pyzbar_detect(img_path):
    img = cv2.imread(img_path)
    results = zxingcpp.read_barcodes(img)
    
    for result in results:
        print(result.text)

if __name__ == "__main__":
    img_path = "raw_image.png"
    print(img_path)
    test_pyzbar_detect(img_path)