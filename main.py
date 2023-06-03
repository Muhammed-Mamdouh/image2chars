import argparse
from character_tree import *
from pixel_to_char import *

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add the arguments you want to accept
parser.add_argument('--photo', type=str, help='Photo path')
parser.add_argument('--size', type=int, help='Tile Size')
parser.add_argument('--chars', type=str, help='Tile Size')

# Parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
    ascii_range = (32, 127)
    if args.chars:
        chars = list(args.chars) + [' ']
    else:
        chars = get_chrs(ascii_range)

    tree, chars = make_chr_tree(chars)

    # In[13]:

    main_photo_path = args.photo
    tile_size = (int(args.size), int(args.size))
    k = 1
    factor = 3.5
    max_width = 100
    output_file_path = main_photo_path.split('.')[0] + ".txt"

    img = make_image(main_photo_path, tree, k, factor, max_width, chars)
    save_image(img, output_file_path, seb=' ')

    show_image(img, seb=' ')
    
    
    
    
    
