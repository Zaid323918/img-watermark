import cv2
import numpy as np


'''
Adding watermark to the center of the image
'''


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