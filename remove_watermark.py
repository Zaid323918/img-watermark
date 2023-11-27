import cv2
import numpy as np

def remove_watermark(image):
  
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use the thresholding to detect the watermark
    _, thresholded = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Fill the detected contours with white color
    mask = np.ones_like(image, dtype=np.uint8) * 255
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Invert the mask
    inverted_mask = cv2.bitwise_not(mask)

    # Combine the original image and the inverted mask
    result = cv2.bitwise_and(image, inverted_mask)

    return result 