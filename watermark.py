import cv2
import numpy as np


'''
Adding watermark to the center of the image
'''


def watermark_image(image, watermark, scale, transparency, blur):

    # height and width of the image 
    h_img, w_img, _ = image.shape 

    # resize the watermark
    resized_watermark = cv2.resize(watermark, (int(h_img * scale), int(w_img * scale)), interpolation=cv2.INTER_AREA)

    # blur the watermark if necessary
    if blur:
        resized_watermark = cv2.GaussianBlur(resized_watermark, (5,5), 0)

    # calculating dimensions 
    # height and width of the logo 
    h_logo, w_logo, _ = resized_watermark.shape 
    
    
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
    local_result = cv2.addWeighted(destination, transparency, resized_watermark, 1-transparency, 0) 

    global_result = np.copy(image)
    global_result[top_y:bottom_y, left_x:right_x] = local_result
    return global_result
