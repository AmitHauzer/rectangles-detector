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
### **Analyse Image:**
  1. Open the `main.py` file.
  2. Set the `image_name` variable to the name of the image you want to analyze.  For example:<br>
     `image_name = 'image5.png'`
  3. Run `the main.py` script.
  4. The script will analyze the specified image and create a copy with the extracted rectangle details.

### **Create Image:**
In the create_image.py file, you can generate an image with rectangles.
  1. Open the `create_image.py` file.
  2. Modify the following variables to define the image settings:
     - `folder`: Specify the folder where the image will be saved.
     - `image_name`: Set the name of the generated image file.
     - `image_height` and `image_width`: Specify the dimensions of the image.
     - `background_color`: Set the RGB values for the background color of the image.
     - `rectangles`: Define the rectangles to be added to the image. Each rectangle should have the following attributes: width (`w`), height (`h`), location (`location`), and color (`color`).
        - The `location` attribute specifies the coordinates (x, y) of the top-left corner of the rectangle.
        - The `color` attribute specifies the RGB values for the rectangle color.
     - For example:
       ```
       folder = './images/'
       image_name = 'image6.png'
       image_height = 1000
       image_width = 1000
       background_color = (128, 128, 128)
       rectangles = [
         {'w': 50, 'h': 80, 'location': (-120, 200), 'color': (255, 0, 0)},
         {'w': 90, 'h': 30, 'location': (-260, 40), 'color': (255, 0, 0)},
         {'w': 70, 'h': 150, 'location': (-20, 60), 'color': (255, 0, 0)},
       ]
       ```
     
  3. Run the `create_image.py` script.
     
