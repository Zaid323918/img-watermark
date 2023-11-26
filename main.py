from watermark import watermark_image
import cv2



def main():
    # Example paths to image and watermark
    image_path = 'path/to/your/image.jpg'   #this is the original img
    watermark_path = 'path/to/your/watermark.png'   #this is the watermark img

    # Read the images
    image = cv2.imread(image_path)  #reading the img
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)    #reading img

    # Remove the watermark
    result = watermark_image(image, watermark) 

    # Display the result
    cv2.imshow('Original Image', image)
    cv2.imshow('Image with Watermark Removed', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()