# image2chars Generator

This is a command-line tool that converts an image into ASCII art using characters from a pre-defined set. The tool works by dividing the image into tiles and replacing each tile with a character that has a similar brightness value.

# Installation
Clone this repository to your local machine:

git clone https://github.com/your_username/ascii-art-generator.git
Install the required packages using pip:

pip install -r requirements.txt
Usage
The tool can be run from the command line using the following syntax:


python main.py --photo <path_to_image> --size <tile_size> --chars <character_set>
where:

<path_to_image> is the path to the input image file

<tile_size> is the size of each tile in characters (default: 10)

<character_set> is the set of characters to use for the ASCII art (default: all printable ASCII characters)

The output image will be saved to a file with the same name as the input image, but with the extension changed to ".txt".

# Example
To convert an image named "my_photo.jpg" using a tile size of 8 and a character set of "01", run the following command:


python main.py --photo my_photo.jpg --size 8 --chars 01
The output will be saved to a file named "my_photo.txt".
