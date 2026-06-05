import cv2
from image_processing import ImageProcessing
import traceback, zxingcpp
import cv2, numpy as np

def original():
    led_brightness_percent = 2

    image = cv2.imread("img-scb_barcodes.png")

    # Spliting the image to ensure we have a better chance of catching the barcode.
    # Otherwise, BarCodeReader is capable to reading all barcodes in an image.
    height, width, _ = image.shape
    img_scb_id = image[:, : width // 2]
    cv2.imwrite("img-scb_id.jpg", img_scb_id)

    # The ublox barcode sits right in front of the LED and therefore some adjustment is needed.
    img_ublox = image[:, width // 2 :]
    img_ublox_qr = img_ublox[1200:1800, 800:1500]
    # NOTE This is a huge headache just because LED position causes glare on the QR code. In well-lit conditions we have no issues.
    # TODO Move the LED back on the Rpi cover to avoid glare and adjust the following settings.
    brightness = 10 if (led_brightness_percent > 0.0) else 0.0
    contrast = 2.5 if (led_brightness_percent > 0.0) else 1.0
    adjusted = (img_ublox_qr * contrast) + brightness
    cv2.imwrite("img_ublox.jpg", adjusted)

    # Analyze bar codes.
    bcr = ImageProcessing()
    read_scb_id = bcr.read_barcode("img-scb_id.jpg")
    scb_id = read_scb_id[0].text if read_scb_id else None
    read_ublox = bcr.read_barcode("img_ublox.jpg")
    ublox = read_ublox[0].text if read_ublox else None
    print(read_scb_id)
    print(read_ublox)

def process_result(img, description):
    print(f"---------{description}-----------")
    cv2.imwrite(description + ".png", img)
    results = zxingcpp.read_barcodes(img)
    for r in results:
        print("Text :", r.text)
        print("Format :", r.format)

def test():
    # Analyze bar codes.
    raw_image = cv2.imread("test-image11.png")
    process_result(raw_image, "raw_image")

    # -------------------------
    # 1. QR 영역 잘라내기
    # -------------------------
    h, w = raw_image.shape[:2]

    # 이미지 기준으로 대략 중앙 QR 추출
    x = int(w * 0.55)
    y = int(h * 0.45)
    cw = int(w * 0.10)
    ch = int(h * 0.10)

    roi = raw_image[y:y+ch, x:x+cw]
    process_result(roi, "cut_image")

    # -------------------------
    # 2. 확대
    # -------------------------
    resized = cv2.resize(
        roi,
        None,
        fx=8,
        fy=8,
        interpolation=cv2.INTER_CUBIC
    )
    process_result(resized, "resized_image")
    # -------------------------
    # 3. 그레이 변환
    # -------------------------
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    process_result(gray, "gray_image")
    # -------------------------
    # 4. Contrast 향상
    # -------------------------
    clahe = cv2.createCLAHE(
        clipLimit=3.0,
        tileGridSize=(8, 8)
    )

    contrast = clahe.apply(gray)
    process_result(contrast, "contrast_image")
    # -------------------------
    # 5. 이진화
    # -------------------------
    _, thresh = cv2.threshold(
        contrast,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    process_result(thresh, "thresh_image")
    
if __name__ == "__main__":
    test()
    
