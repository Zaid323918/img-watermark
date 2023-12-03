# Computer Vision Final Project | Image Watermarking 

### Team:
- Ryan Larsen 
- Yousif Al Saadi
- Zaid Jamal 

### Required Installations:
- opencv-python
- numpy 

### Breakdown:
The source code for the program is contained in the folder called _src_. It contains:
- ```watermark.py``` contains the function for adding a watermark to an image. 
- ```remove_watermark.py``` contains the function for removing a watermark from an image.
- ```input_handling.py``` contains functions for the program's interface. 
- ```main.py``` contains the driver code for running the program. 

The folder called _tests_ contains the following:
- A folder called _data_ whichc ontains the images and watermarks used for testing the program's capabilities. If further testing is desired, more image/watermark files can be added to this folder so that their file paths can be referenced when running the program. 
- A folder called _output_ that contains the results of running tests with images and watermarks in the _data_ folder. 
- ```alltest.py``` contains the various tests ran on the images with differing parameters. 

### Running the Program:
- With provided data and test cases: Use ```python alltest.py```
- With custom images and test cases: Add the desired images/watermarks to the data folder and use ```python main.py```. Follow the program's instructions to input the desired parameters. 