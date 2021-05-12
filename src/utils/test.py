from tools import tesseractModel
import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('data/image/ni.jpg')
    img = np.array(img)
    img = img[:,:,::-1]
    # print('hello')
    
    model = tesseractModel(os_sys='windows')
    img_process = model.img_preprocessing_(img)
    print(img_process.shape)
    # 顯示圖片
    cv2.imshow('My Image', img_process)

    # 按下任意鍵則關閉所有視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(model.predict_(img_process))