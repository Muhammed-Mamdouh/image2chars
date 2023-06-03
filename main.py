import argparse
from character_tree import *
from pixel_to_char import *
import os
import pickle

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add the arguments you want to accept
parser.add_argument('--photo', type=str, help='Photo path')
parser.add_argument('--width', type=int, help='Tile Size')
parser.add_argument('--chars', type=str, help='Tile Size')

# Parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
    ascii_range = (32, 127)
    if args.chars:
        chars = list(args.chars) + [' ']
        tree, chars = make_char_tree(chars)
    else:
        chars = get_chars(ascii_range)
        if os.path.exists("tree.pickle"):
            with open("tree.pickle", "rb") as f:
                # Deserialize the contents of the file into a Python object
                tree = pickle.load(f)
        else:
            tree, chars = make_char_tree(chars)
            with open("tree.pickle", "wb") as f:
                pickle.dump(tree, f)


    # In[13]:

    main_photo_path = args.photo
    k = 1
    factor = 3.5
    max_width = int(args.width or 0) or 200
    output_file_path = main_photo_path.split('.')[0] + ".txt"

    img = make_image(main_photo_path, tree, k, factor, max_width, chars)
    save_image(img, output_file_path, seb=' ')

    show_image(img, seb=' ')
    
    
    
    
    
