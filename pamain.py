from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import re

# Initialize PaddleOCR with Vietnamese language support
ocr = PaddleOCR(use_angle_cls=True, lang='vi')  # need to run only once to download and load model into memory

# Path to the input image
img_path = './1.jpg'

# Perform OCR on the image
result = ocr.ocr(img_path, cls=True)

# Define a post-processing function to correct common OCR misrecognitions
def correct_vietnamese_text(text):
    replacements = {
        'Hoa don': 'Hóa đơn',
        'Mau s6': 'Mẫu số',
        'Ky hieu': 'Ký hiệu',
        'Thanh phó': 'Thành phố',
        'Ha Nöi': 'Hà Nội',
        'Viet Nam': 'Việt Nam',
        "HOA": "HÓA", 
        "DON": "ĐƠN",
        "TRI":"TRỊ",
        "GIA": "GIÁ",
        "TANG": "TĂNG",
        "S6":"Số",
        "CHUYEN":"CHUYỂN",
        "DOI":"ĐỔI",
        "DIEN":"ĐIỆN",
        "TU":"TỬ",
        "Ngay":"Ngày",
        "thang":"tháng",
        "nam ":"năm"
        # Add more replacements as needed
    }
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)
    return text

# Print the OCR results in Vietnamese with corrections
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        corrected_text = correct_vietnamese_text(line[1][0])
        print(corrected_text)  # Print the corrected text

# Draw the OCR results on the image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [correct_vietnamese_text(line[1][0]) for line in result]
scores = [line[1][1] for line in result]

# Font path for drawing text
font_path = './texgyreheros-regular.otf'  # Path to the Vietnamese font

# Draw OCR results on the image
im_show = draw_ocr(image, boxes, txts, scores, font_path=font_path)
im_show = Image.fromarray(im_show)

# Save the result image
im_show.save('result.jpg')

# Print the recognized texts for testing purposes
print("Recognized texts:", txts)
