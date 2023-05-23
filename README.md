# rectangles-detector
The "rectangles-detector" project analyzes images and extracts data about rectangles in each image.<br>
It also generates images with rectangles. Below are the instructions for installation and usage:

## Installation:
1. Clone the repository using Git.
2. Open a terminal.
3. Create a virtual environment using the command:<br>
	 `python -m venv venv`
4. Activate the virtual environment:<br>
        - On Windows: `.\venv\Scripts\activate`<br>
        - On macOS/Linux: `source venv/bin/activate` 

5. Install requirements:<br>
   `pip install -r requirements.txt`

## Instructions:
### **Analysis:**
- Run the `main.py` script.
- The script will analyze each image listed in the CSV files and compare its details with the analysis details.
- For each image, the script performs the following checks:
	- Compares the image's width, height, and background color.
	- Compares the details of each rectangle detected in the image with the corresponding entry in the CSV file.
- The script prints "Pass" or "Failed" for each check.


### **Create Image:**
In the create_image.py file, you can generate an image with rectangles.
  1. Open the `create_image.py` file.
  2. Modify the following variables to define the image settings:
     - `folder`: Specify the folder where the image will be saved.
     - `image_name`: Set the name of the generated image file.
     - `image_height` and `image_width`: Specify the dimensions of the image.
     - `image_background`: Set the RGB values for the background color of the image.
     - `rectangles`: Define the rectangles to be added to the image. Each rectangle should have the following attributes: width (`w`), height (`h`), location (`location`), and color (`color`).
        - The `location` attribute specifies the coordinates (x, y) of the top-left corner of the rectangle.
        - The `color` attribute specifies the RGB values for the rectangle color.
     - For example:
       ```
       folder = './images/'
       image_name = 'image6.png'
       image_height = 1000
       image_width = 1000
       image_background = (128, 128, 128)
       rectangles = [
         {'w': 50, 'h': 80, 'location': (-120, 200), 'color': (255, 0, 0)},
         {'w': 90, 'h': 30, 'location': (-260, 40), 'color': (255, 0, 0)},
         {'w': 70, 'h': 150, 'location': (-20, 60), 'color': (255, 0, 0)},
       ]
       ```
     
  3. Run the `create_image.py` script.
     
