# Image to Characters Generator

This is a Python command-line tool that converts a given image into a grid of characters that resembles the image. The tool works by dividing the image into tiles and replacing each tile with a character that has a similar brightness value.

## Installation

1. Clone this repository to your local machine:

```sh
git clone https://github.com/your_username/image-to-chars-generator.git
```
2. Install the required packages using pip:
```sh
pip install -r requirements.txt
```
# Usage
To use the tool, run the generate.py script from the command line, with the following arguments:



```sh
python generate.py --photo <path_to_input_image>  --size <size_of_each_tile> --chars <set_of_characters>
```
where:

- <path_to_input_image> is the path to the input image file
- <size_of_each_tile> is the size of each tile in pixels (eg: 5, the smaller the higher the resolution and the bigger the output)
- <set_of_characters> is the set of characters to use for the output (default: a pre-defined set of ASCII characters)

## The output text file will contain a grid of characters that resembles the input image.

# Example
To convert an image named "my_photo.jpg" using a tile size of 8 and a character set of "01", and save the output to a file named "my_output.txt", run the following command:

```sh
python main.py --photo my_photo.jpg --size 5 --chars MANDO.
```

The output should be find in the same directory as the input photo as a txt file
