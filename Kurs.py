import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def Turn(img, val):
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
    
    '''
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    tur90 = cv2.warpAffine(img, M, (w, h))
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    tur180 = cv2.warpAffine(img, M, (w, h))
    M = cv2.getRotationMatrix2D(center, 270, 1.0)
    tur270 = cv2.warpAffine(img, M, (w, h))
    titles = ['Original Image', '90*', '180*', '270*']
    images = [img, tur90, tur180, tur270]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
    '''

    M = cv2.getRotationMatrix2D(center, val, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))

    #cv2.imwrite('testrotated.jpg',rotated)
    return rotated


def Blur(img):
    blurGaus = cv2.GaussianBlur(img, (7, 7), 0) 
    
    '''
    kernel = np.ones((5,5),np.float32)/25
    blur2DConv = cv2.filter2D(img,-1,kernel)
    blurAver = cv2.blur(img, (5, 5)) 
    blurMed = cv2.medianBlur(img, 5) 
    blurBilFiltr = cv2.bilateralFilter(img, 9, 75, 75) 
    titles = ['Original Image', 'Gaussian', '2D Convolution', 'Averaging', 'Median', 'BilateralFiltering']
    images = [img, blurGaus, blur2DConv, blurAver, blurMed, blurBilFiltr]
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
    '''

    #cv2.imwrite('testblur.jpg',blurGaus)
    return blurGaus


def Binary(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thGlobal = cv2.threshold(imgGray, 165, 255, cv2.THRESH_BINARY)

    '''
    thAdaptMean = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    thAdaptGaus = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    titles = ['Original Image', 'Global Thresholding (v = 165)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [imgGray, thGlobal, thAdaptMean, thAdaptGaus]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
    '''

    #cv2.imwrite('testbin.jpg',thGlobal)
    return thGlobal


def Square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, ((size - x) // 2, (size - y) // 2))
    return new_im

def ConverPILtoOpenCV(pil_image):
    numpy_image = np.array(pil_image)  
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
    return opencv_image


def Squeeze(img, size):
    wpercent = (size/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((size,hsize), Image.ANTIALIAS)
    return img

def main():
    in_img = "test.jpg"
    #image = cv2.imread(in_img)                   
    image = Image.open(in_img)                  # load image
    image = Square(image)
    image = Squeeze(image, 1600)
    image = ConverPILtoOpenCV(image)
    image = Turn(image, 180)
    image = Blur(image)
    image = Binary(image)
    cv2.imwrite('output.jpg',image)              # save image
    #cv2.imshow("Rotated image", image)          # show image
    #cv2.waitKey(0)                              # readkey
    #cv2.destroyAllWindows()                     # press enter to close all windows

main()