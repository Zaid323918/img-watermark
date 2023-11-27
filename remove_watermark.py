import cv2
import numpy as np

def remove_watermark(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use thresholding to detect the watermark
    _, thresholded = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask to cover the watermark region
    mask = np.ones_like(image, dtype=np.uint8) * 255
    cv2.drawContours(mask, contours, -1, (0, 0, 0), thickness=cv2.FILLED)

    # Inpainting to remove the watermark
    result = cv2.inpaint(image, mask[:, :, 0], 3, cv2.INPAINT_TELEA)

    return result