import cv2
import numpy as np


'''
Adding watermark to the center of the image
'''


def WatermarkImage(Image, Watermark):
    # Resizing watermark image keeping the aspect ratio
    # Resize is done such that watermark's height is equal to 10% of the image's height
    NewHeight = int(Image.shape[0]*0.1)
    NewWidth = int(NewHeight * (Watermark.shape[1]/Watermark.shape[0]))
    Watermark = cv2.resize(Watermark, (NewWidth, NewHeight), interpolation=cv2.INTER_AREA)
    
    # Creating 3 channeled watermark image and alpha image(range -> [0.0-1.0])
    Watermark = cv2.merge((Watermark, Watermark, Watermark))
    # Transparency of the watermark is 60% (0.4 is opacity)
    Alpha = (Watermark.astype(float) * 0.4)/255
    
    # Applying watermark on the bottom right corner leaving 20 pixels from both the boundaries
    WatermarkedImage = Image.copy()
    ah, aw = Alpha.shape[:2]
    WatermarkedImage[-(ah+20):-20, -(aw+20):-20] = cv2.add(cv2.multiply(Alpha, Watermark, dtype=cv2.CV_64F),
                                cv2.multiply(1.0-Alpha, Image[-(ah+20):-20, -(aw+20):-20], dtype=cv2.CV_64F))
    WatermarkedImage = np.uint8(WatermarkedImage)
    
    return WatermarkedImage

def watermark_image(image, watermark):
    # calculating dimensions 
    # height and width of the logo 
    h_logo, w_logo, _ = watermark.shape 
    
    # height and width of the image 
    h_img, w_img, _ = image.shape 
    
    # calculating coordinates of center 
    # calculating center, where we are going to  
    # place our watermark 
    center_y = int(h_img/2) 
    center_x = int(w_img/2) 
    
    # calculating from top, bottom, right and left 
    top_y = center_y - int(h_logo/2) 
    left_x = center_x - int(w_logo/2) 
    bottom_y = top_y + h_logo 
    right_x = left_x + w_logo 
    
    # adding watermark to the image 
    destination = image[top_y:bottom_y, left_x:right_x] 
    result = cv2.addWeighted(destination, 1, watermark, 0.5, 0) 
    return result