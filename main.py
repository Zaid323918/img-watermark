from watermark import watermark_image
import cv2

def main():
    # Example paths to image and watermark
    image_path = 'data/original-farm.jpeg'   # this is the original img
    watermark_path = 'data/Farm.jpeg'   # this is the watermark img

    # Read the images
    image = cv2.imread(image_path)  # reading the img
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)    # reading img

    # Remove the watermark
    result = watermark_image(image, watermark)

    # Display the original image
    print("Original Image:")
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)  # Wait until a key is pressed

    # Display the image with watermark removed
    print("Image with Watermark Removed:")
    cv2.imshow('Image with Watermark Removed', result)
    cv2.waitKey(0)  # Wait until a key is pressed

    # Print information
    print("Image Shape (Original):", image.shape)
    print("Image Shape (Result):", result.shape)

    # Close all windows
    cv2.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()
