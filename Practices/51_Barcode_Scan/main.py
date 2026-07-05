import cv2
import zxingcpp

def test_qr(img, message):
    # -------------------------
    # 7. ZXingCPP 인식
    # -------------------------
    results = zxingcpp.read_barcodes(img)
    print(f"----------{message}----------")
    if results == []:
        print("barcode is not recognised")
    else:
        for r in results:
            print("Text :", r.text)
            print("Format :", r.format)

# 원본 읽기
img = cv2.imread("blur_QR.png")
test_qr(img, "raw image")
# -------------------------
# 1. QR 영역 잘라내기
# -------------------------
h, w = img.shape[:2]

# 이미지 기준으로 대략 중앙 QR 추출
x = int(w * 0.45)
y = int(h * 0.45)
cw = int(w * 0.12)
ch = int(h * 0.20)

roi = img[y:y+ch, x:x+cw]
test_qr(roi, "cut image")
cv2.imwrite("cut_QR.png", roi)
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
test_qr(resized, "resized image")
cv2.imwrite("resized_QR.png", resized)

# -------------------------
# 3. 그레이 변환
# -------------------------
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
test_qr(gray, "gray image")
cv2.imwrite("gray_QR.png", gray)
# -------------------------
# 4. Contrast 향상
# -------------------------
clahe = cv2.createCLAHE(
    clipLimit=3.0,
    tileGridSize=(8, 8)
)

contrast = clahe.apply(gray)
test_qr(contrast, "contrast image")
cv2.imwrite("contrast_QR.png", contrast)
# -------------------------
# 5. 이진화
# -------------------------
_, thresh = cv2.threshold(
    contrast,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
test_qr(thresh, "thresh image")
# ------------------------- 
# 6. 저장 
# ------------------------- 
cv2.imwrite("qr_enhanced.png", thresh)






