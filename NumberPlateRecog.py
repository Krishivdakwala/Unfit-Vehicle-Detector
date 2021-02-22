import pytesseract
import matplotlib.pyplot as plt
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def ImgToStr(img):
    img = cv2.imread(img)

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    blur = cv2.medianBlur(gray_image, 3)
    blur = cv2.resize(blur, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    predicted_result = pytesseract.image_to_string(thresh, lang='eng',
                                                   config='--oem 3  --psm 6')

    filter_predicted_result = "".join(predicted_result.split()).replace(":", "").replace("-", "")
    return "".join(str for str in filter_predicted_result.strip() if str.isalnum())
