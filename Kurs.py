import cv2
import numpy as np
from matplotlib import pyplot as plt    
from PIL import Image

def make_square(old_path, new_path, max_size=600, fill_color=(0, 0, 0)):
    # find image dimensions
    old_img = Image.open(old_path)
    size = (min(max_size, max(old_img.size)),) * 2

    # resize if old image is larger than max_size
    if size[0] < old_img.size[0] or size[1] < old_img.size[1]:
        old_img.thumbnail(size)

    # create new image with the given color and computed size
    new_img = Image.new(old_img.mode, size, fill_color)

    # find coordinates of upper-left corner to center the old image in the new image
    assert new_img.size[0] >= old_img.size[0]
    assert new_img.size[1] >= old_img.size[1]

    x = (new_img.size[0] - old_img.size[0]) // 2
    y = (new_img.size[1] - old_img.size[1]) // 2

    # paste image
    new_img.paste(old_img, (x, y))
    # save image
    new_img.save(new_path)

def Blur(img):
    #blur = cv2.blur(img,(5,5)) 
    blur = cv2.GaussianBlur(img,(9,9),0) 
    #blur = cv2.medianBlur(img,5) 
    #blur = cv2.bilateralFilter(img,9,75,75) 
    
    #plt.subplot(121),plt.imshow(img),plt.title('Original')         # paint on plt form
    #plt.xticks([]), plt.yticks([]) 
    #plt.subplot(122),plt.imshow(blur),plt.title('Blurred') 
    #plt.xticks([]), plt.yticks([]) 
    #plt.show()
    return blur
    #cv2.imwrite("Blured.png", blur)
    #cv2.imshow("Blur image", blur)
    #cv2.waitKey(0)


def main():
    in_img = "dog.jpg"
    image = cv2.imread(in_img)          # load image
    Blur(image)
    '''
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, 270, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    '''
    #cv2.imwrite('lol.png',image)                # save image
    cv2.imshow("Rotated image", image)          # show image
    cv2.waitKey(0)                              # readkey
    cv2.destroyAllWindows()                     # press enter to close all windows
    

main()

'''
mode = int(input('mode:'))
image = Image.open("test.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

if (mode == 5):
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = a + b + c
			if (S > (((255 + factor) // 2) * 3)):
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			draw.point((i, j), (a, b, c))

image.save("result200.jpg", "JPEG")
del draw
'''
