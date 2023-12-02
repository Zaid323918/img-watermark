import cv2
import numpy as np

def remove_watermark(image, watermark, scale, transparency, blur, x_pos, y_pos):
    """
    Removes a provided watermark from an image. 

    Parameters: 
    image (numpy.ndarray): The input image to remove the watermark from.
    watermark (numpy.ndarray): The watermark to remove from the first parameter.
    scale (float): The size difference between the image and the watermark.
    transparency (float): Transparency of the watermark on the image.
    blur (bool): Whether or not the watermark was blurred. 
    x_pos (int): The location of the watermark in the x direction.
    y_pos (int): The location of the watermark in the y direction.

    Returns: 
        The output image with the watermark removed from it  
    
    """

    # height and width of the image 
    h_img, w_img, _ = image.shape 

    # resize the watermark
    smallest_dimension_size = min(w_img, h_img)
    resized_watermark = cv2.resize(watermark, (int(smallest_dimension_size * scale), int(smallest_dimension_size * scale)), interpolation=cv2.INTER_AREA)

    # blur the watermark if necessary
    if blur:
        resized_watermark = cv2.GaussianBlur(resized_watermark, (5,5), 0)
 
    # height and width of the logo 
    h_watermark, w_watermark, _ = resized_watermark.shape 
    
    # calculating coordinates of center 
    center_y = int(h_img/2) 
    center_x = int(w_img/2) 
    
    # calculating from top, bottom, right and left 
    top_y = center_y - int(h_watermark/2) 
    left_x = center_x - int(w_watermark/2) 
    bottom_y = top_y + h_watermark 
    right_x = left_x + w_watermark 

    # change bounds if center is not selected
    LEFT, RIGHT, TOP, BOTTOM = 1,3,1,3
    if x_pos == LEFT:
        left_x = 0
        right_x = left_x + w_watermark
    elif x_pos == RIGHT:
        right_x = w_img - 1
        left_x = right_x - w_watermark
    
    if y_pos == TOP:
        top_y = 0
        bottom_y = top_y + h_watermark
    elif y_pos == BOTTOM:
        bottom_y = h_img - 1
        top_y = bottom_y - h_watermark

    # removing watermark from the image 
    destination = image[top_y:bottom_y, left_x:right_x] 
    watermark_removed_area = (destination - resized_watermark * (1 - transparency)) / transparency

    global_result = np.copy(image)
    global_result[top_y:bottom_y, left_x:right_x] = watermark_removed_area
    
    return global_result
