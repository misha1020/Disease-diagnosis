import cv2
import numpy as np 
import os
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
    rotated = cv2.warpAffine(img, M, (w, h), borderValue=(255,255,255))
    return rotated


def Blur(img):
    blurGaus = cv2.GaussianBlur(img, (5, 5), 0) 
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
    return blurGaus

def Binary(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retGl, thGlobal = cv2.threshold(imgGray, 165, 255, cv2.THRESH_BINARY)
    '''
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thGlobal = cv2.threshold(imgGray, 165, 255, cv2.THRESH_BINARY)
    ret, thBinInv = cv2.threshold(imgGray, 165, 255, cv2.THRESH_BINARY_INV)
    ret, thTrunc = cv2.threshold(imgGray, 165, 255, cv2.THRESH_TRUNC)
    ret, thTozero = cv2.threshold(imgGray, 165, 255, cv2.THRESH_TOZERO)    
    ret, thTozeroInv = cv2.threshold(imgGray, 165, 255, cv2.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [imgGray, thGlobal, thTrunc, thTrunc, thTozero, thTozeroInv]
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])    
    
    thAdaptGaus = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    retOt, thOtsuBin = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    titles = ['Original Image', 'Global Thresholding (v = 165)', 'Adaptive Gaussian Thresholding', 'Otsu’s Binarization']
    images = [imgGray, thGlobal, thAdaptGaus, thOtsuBin]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    
    plt.show()
    '''
    return thGlobal


def Canny(img):
    edges = cv2.Canny(img,100,200)
    '''
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()
    '''
    return edges


def Square(im, min_size = 256, fill_color = (255, 255, 255)):
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

def Capitalize(myStr):
    return myStr.upper()

def LoadFilesNamesFromDir(dir):
    files = os.listdir(dir)
    for i, file in enumerate(files):
        splited = file.split(".")
        splited[1] = Capitalize(splited[1])
        file = splited[0] + "." + splited[1]
        files[i] = file
    imgNames = filter(lambda x: x.endswith(".PNG") or x.endswith(".BMP") or x.endswith(".JPG") or x.endswith(".JPEG"), files)
    return imgNames

def main():
    directory = "../Test"
    imagesNames = LoadFilesNamesFromDir(directory)
    for imageName in imagesNames:
        print(imageName)
        k = 0
        imageInput = Image.open(directory + "/" + imageName)
        while (k < 360):
            image = imageInput.copy()           
            image = Square(image)
            image = Squeeze(image, 128)
            image = ConverPILtoOpenCV(image)
            #image = Turn(image, k)
            #image = cv2.imread(directory + "/" + imageName) 
            image = Blur(image)
            image = Binary(image)
            #image = Canny(image)
            splited = imageName.split(".")
            imageName = splited[0]
            cv2.imwrite("../Test/" + imageName + "_" + str(k) + ".JPG", image)              # save image
            k += 360
main()


#image = cv2.imread(in_img)                  # load image CV
#cv2.imshow("Rotated image", image)          # show image
#cv2.waitKey(0)                              # readkey
#cv2.destroyAllWindows()                     # press enter to close all windows