from Image2Char.image_processing import *
import random
import numpy as np
from PIL import Image


def pxl2chr(pixel, tree, chars):
    # Given a pixel, find the index of the closest character in the `chars` array
    _, closest_k = tree.query([pixel])
    return chars[closest]


def rand_px2chr(pixel, tree, chars, k):
    # Given a pixel, find the closest k characters in the `chars` array and return one randomly
    _, closest_k = tree.query([pixel], k=k)
    closest = random.choice(closest_k)
    return chars[closest]


def construct_chr_img(img, px2char_func):
    # Given an image and a pixel-to-character function, convert the image to a character array
    # Convert image to a numpy array and apply the pixel-to-character function to each pixel
    img_arr = np.array(img)
    func = np.vectorize(px2char_func)
    chr_arr = func(img_arr)
    return chr_arr


def make_image(img_path, tree, k, factor, width, chars, normalize=True):
    # Given an image path, a KDTree, a value k, a factor, a width, an array of characters, and a boolean `normalize`,
    # return a character array representation of the image
    # Read image
    img = Image.open(img_path)
    # Process image
    processed_img = process_image(img, factor, normalize=normalize)
    # Resize image
    resized_processed_img = resizing(processed_img, width)
    # Create a pixel-to-character function based on the value of k
    if k == 1:
        px2char_func = lambda pixel: pxl2chr(pixel, tree, chars)
    else:
        px2char_func = lambda pixel: rand_px2chr(pixel, tree, chars, k)
    # Convert image to character array using the pixel-to-character function
    chr_img = construct_chr_img(resized_processed_img, px2char_func)
    return chr_img


def show_image(closest_chars, seb):
    # Given a character array `closest_chars` and a separator `seb`, print the character array
    for i in range(closest_chars.shape[0]):
        print('', end='\n')
        for j in range(closest_chars.shape[1]):
            print(closest_chars[i, j], end=seb)


def save_image(closest_chars, name, seb='.'):
    # Given a character array `closest_chars`, a file name `name`, and a separator `seb`, save the character array as
    # a text file
    img_string = ''
    for i in range(closest_chars.shape[0]):
        img_string += seb.join(closest_chars[i]) + ' \n'
    with open(name, 'w') as file:
        file.write(img_string)
