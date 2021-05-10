import pytesseract
# from pytesseract import Output
# from PIL import Image
import cv2

class tesseractModel(object):
    def __init__(self, os_sys='linux'):
        self._load_system(os_sys)

    def _load_system(self,os_sys):
        if os_sys=='windows':
            # To Do
            # path need to be up-date
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        else:
            pass
    
    def img_preprocessing_(self,img):
        # To Do
        # 1. Tesseract needs img to look like document.
        # 2. Morphological closing needs to be perform to identify the word size.
        # 3. We need to pad img so that the word would look like a single word in the document.
        # 4. Maybe word/img ratio = 1/10~1/20 would be fine.
        # 5. This is how tesseract preferred to recognize the word.
        ## Note: Somehow tesseract only recognize a series of word, instead of a single word. So I add a concat step.
        img = cv2.hconcat([img, img])
        img_process = cv2.copyMakeBorder(img, 300, 300, 300, 300, cv2.BORDER_CONSTANT, value=[255,255,255])
        img_process = cv2.resize(img_process, (500, 500), interpolation=cv2.INTER_AREA)
        return img_process

    def predict_(self,img):
        text = pytesseract.image_to_string(img, lang='chi_tra')
        if len(text)>0:
            for candidate in text:
                if candidate!=None:
                    text=candidate
                    break
        elif text == None:
            text = "is_null"
        return text


# def preprocess():
#     img = cv2.imread('image4.JPG')
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#     (cnts, _) = cv2.findContours(binary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#     clone = img.copy()

#     cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
#     cv2.imshow('img', clone)
#     cv2.waitKey(0)
# def main():
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     # img = Image.open(r"E:\TDSC\OCR\image.jpg")
#     # img.show()
#     #img = cv2.imread('invoice-sample.jpg')
#     img = cv2.imread('image7.jpg')
#     print(type(img))
#     # lang = "eng"
#     d = pytesseract.image_to_data(img, lang="chi_tra",output_type=Output.DICT)
#     print(d.keys())
#     return img, d

# def plot_detect(img, d):
#     n_boxes = len(d['text'])
#     for i in range(n_boxes):
#         if int(d['conf'][i]) > 60:
#             (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     print(d['text'])
#     cv2.imshow('img', img)
#     cv2.waitKey(0)

# if __name__ == "__main__":
#     # preprocess()
#     img, dict_d = main()
#     plot_detect(img, dict_d)
