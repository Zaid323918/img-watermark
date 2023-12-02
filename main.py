from watermark import watermark_image
from remove_watermark import remove_watermark
from input_handling import get_input, get_filename, get_scale, get_transparency, get_blur, get_pos_top_to_bottom, get_pos_left_to_right
import cv2

def main():
    choice = get_input()

    image_path = get_filename('image')
    watermark_path = get_filename('watermark')
    
    image = cv2.imread(image_path)
    watermark = cv2.imread(watermark_path)

    scale = get_scale()
    transparency = get_transparency()
    blur = get_blur()
    y_pos = get_pos_top_to_bottom()
    x_pos = get_pos_left_to_right()

    if choice == 1:
        watermarked_image = watermark_image(image, watermark, scale=scale, transparency=transparency, blur=blur, x_pos=x_pos, y_pos=y_pos)
        cv2.imwrite('watermarked_image.jpg', watermarked_image)

    elif choice == 2:
        unwatermarked_image = remove_watermark(image, watermark, scale=scale, transparency=transparency, blur=blur, x_pos=x_pos, y_pos=y_pos)
        cv2.imwrite('image_stripped_of_watermark.jpg', unwatermarked_image)

# Call the main function
if __name__ == "__main__":
    main()
