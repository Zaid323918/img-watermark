import os
import sys

current_directory = os.path.abspath(os.path.dirname(__file__))
parent_directory = os.path.dirname(current_directory)
source_directory = os.path.join(parent_directory, 'src')

data_directory = os.path.join(current_directory, 'data')
output_directory = os.path.join(current_directory, 'output')

sys.path.append(source_directory)

from watermark import watermark_image
from remove_watermark import remove_watermark
import cv2

def main() -> None:

    image_list = [
        'Beach.jpeg',
        'Bricks.jpg',
        'Farm.jpeg',
        'Motherboard-like.jpg'
    ]
    watermark_list = [
        'Plant.jpeg',
        'Square-Triangle-Search.png'
    ]

    # Test 1
    # Should add a blurred plant watermark at the bottom right of the beach picture
    test_add_watermark(image_list[0], watermark_list[0], 0.2, 0.4, True, 3, 3)

    # Test 2
    # Should add a non-blurred plant watermark at the top middle of the bricks picture
    test_add_watermark(image_list[1], watermark_list[0], 0.4, 0.3, False, 2, 1)

    # Test 3
    # Should add a blurred search watermark at the middle left of the farm picture
    test_add_watermark(image_list[2], watermark_list[1], 0.4, 0.3, True, 1, 2)

    # Test 4
    # Should add a non-blurred search watermark at the center of the motherboard-like picture
    test_add_watermark(image_list[3], watermark_list[1], 0.1, 0.7, False, 2, 2)

    # Test 5
    # Should remove watermark from beach picture
    test_remove_watermark(image_list[0], watermark_list[0], 0.2, 0.4, True, 3, 3)

    # Test 6
    # Should remove watermark from bricks picture
    test_remove_watermark(image_list[1], watermark_list[0], 0.4, 0.3, False, 2, 1)

    # Test 7
    # Should remove watermark from farm picture
    test_remove_watermark(image_list[2], watermark_list[1], 0.4, 0.3, True, 1, 2)

    # Test 8
    # Should remove watermark from motherboard-like picture
    test_remove_watermark(image_list[3], watermark_list[1], 0.1, 0.7, False, 2, 2)
    
def test_add_watermark(pic_file, watermark_file, scale, transparency, blur, x_pos, y_pos) -> None:
    pic = cv2.imread(os.path.join(data_directory, pic_file))
    watermark = cv2.imread(os.path.join(data_directory, watermark_file))
    
    watermarked_img = watermark_image(pic, watermark, scale, transparency, blur, x_pos, y_pos)
    cv2.imwrite(os.path.join(output_directory, 'watermarked_' + pic_file), watermarked_img)

def test_remove_watermark(pic_file, watermark_file, scale, transparency, blur, x_pos, y_pos) -> None:
    pic = cv2.imread(os.path.join(output_directory, 'watermarked_' + pic_file))
    watermark = cv2.imread(os.path.join(data_directory, watermark_file))

    unwatermarked_img = remove_watermark(pic, watermark, scale, transparency, blur, x_pos, y_pos)
    cv2.imwrite(os.path.join(output_directory, 'unwatermarked_' + pic_file), unwatermarked_img)

if __name__ == '__main__':
    main()
