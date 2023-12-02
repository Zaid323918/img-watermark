import cv2
import numpy as np


'''
Adding watermark to the center of the image
'''


def watermark_image(image, watermark, scale, transparency, blur, x_pos, y_pos):

    # height and width of the image 
    h_img, w_img, _ = image.shape 

    # resize the watermark
    smallest_dimension_size = min(w_img, h_img)
    resized_watermark = cv2.resize(watermark, (int(smallest_dimension_size * scale), int(smallest_dimension_size * scale)), interpolation=cv2.INTER_AREA)

    # blur the watermark if necessary
    if blur:
        resized_watermark = cv2.GaussianBlur(resized_watermark, (5,5), 0)

    # calculating dimensions 
    # height and width of the logo 
    h_logo, w_logo, _ = resized_watermark.shape 
    
    # calculating coordinates of center 
    center_y = int(h_img/2) 
    center_x = int(w_img/2) 
    
    # calculating from top, bottom, right and left 
    top_y = center_y - int(h_logo/2) 
    left_x = center_x - int(w_logo/2) 
    bottom_y = top_y + h_logo 
    right_x = left_x + w_logo 

    # change bounds if center is not selected
    LEFT, RIGHT, TOP, BOTTOM = 1,3,1,3
    if x_pos == LEFT:
        left_x = 0
        right_x = left_x + w_logo
    elif x_pos == RIGHT:
        right_x = w_img - 1
        left_x = right_x - w_logo
    
    if y_pos == TOP:
        top_y = 0
        bottom_y = top_y + h_logo
    elif y_pos == BOTTOM:
        bottom_y = h_img - 1
        top_y = bottom_y - h_logo
    
    # adding watermark to the image 
    destination = image[top_y:bottom_y, left_x:right_x] 
    local_result = cv2.addWeighted(destination, transparency, resized_watermark, 1-transparency, 0) 

    global_result = np.copy(image)
    global_result[top_y:bottom_y, left_x:right_x] = local_result
    return global_result
