from watermark import watermark_image
from remove_watermark import remove_watermark
from input_handling import get_input, get_filename
import cv2

def main():
    choice = get_input()

    image_path = get_filename('image')
    watermark_path = get_filename('watermark')
    
    image = cv2.imread(image_path)
    watermark = cv2.imread(watermark_path)

    if choice == 1:
        watermarked_image = watermark_image(image, watermark)
        cv2.imwrite('watermarked_image.jpg', watermarked_image)

    elif choice == 2:
        unwatermarked_image = remove_watermark(image, watermark)
        cv2.imwrite('image_stripped_of_watermark.jpg', unwatermarked_image)

# Call the main function
if __name__ == "__main__":
    main()
