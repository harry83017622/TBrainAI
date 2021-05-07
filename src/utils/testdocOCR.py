from PIL import Image #version 3.2.0
import pytesseract as ocr #version 0.2.5
import cv2 #version 3.4.5
import numpy as np #version 1.15.2

imgPath = "image2.jpg"
img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
gray = cv2.fastNlMeansDenoisingColored(img, None, 10, 3, 3, 3)
coefficients=[0,1,1]
m = np.array(coefficients).shape((1,3))
gray = cv2.transform(gray, m)

ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
ele = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 10))

dilation = cv2.dilate(binary, ele, iteration=1)
image, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for box in contours:
    i_index += 1
    h = abs(box[0][1] - box[2][1])
    w = abs(box[0][0] - box[2][0])
    max_point = box[3][0]
    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    y1 = min(Ys)

    cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    img_gray = img[y1:y1+h, x1:x1+w]
    
    idImg = cv2.resize(img_gray, (img_gray.shape[1]*3, img_gray.shape[0]*3), interpolation=cv2.INTER_CUBIC)
    idImg = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    retval, idImg = cv2.threshold(idImg, 120, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

    print("index:",str(i_index),"tag:",box,"high:",h,"width:",w)
    cv2.imwrite("data\idImg_"+str(i_index)+".png", idImg)
    cv2.imwrite("data\contours.png", img)    
    if (max_point>max_item and w//h>=4.0):
        max_item=max_point
        max_index=i_index

    
    if(idImg is not None):
        image = Image.fromarray(idImg)
        ocr.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract.exe' 
        tessdata_dir_config = '--tessdata-dir "Tesseract-OCR\\tessdata"'
        result = ocr.image_to_string(image,config=tessdata_dir_config)
        if(result==""):
            print("don't know")
        else:
            print('the detect result is '+result)
        f, axarr = plt.subplots(2, 3)
        axarr[0, 0].imshow(cv2.imread(imgPath))
        axarr[0, 1].imshow(cv2.imread("data\gray.png"))
        axarr[0, 2].imshow(cv2.imread("data/binary.png")
        axarr[1, 0].imshow(cv2.imread("data\dilation.png"))
        axarr[1, 1].imshow(cv2.imread("data\contours.png"))
        axarr[1, 2].imshow(cv2.imread("data\idImg_"+str(max_index)+".png"))
        plt.show()
    else:
        print('not found id')
