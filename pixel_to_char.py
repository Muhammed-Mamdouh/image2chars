import random
from image_processing import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def pxl2chr(pixel, tree, chars):
    closest = tree.query([pixel])[1]
    return chars[closest]


def rand_px2chr(pixel, tree, chars, k):
    closest_k = tree.query([pixel], k=k)
    # if k is bigger than 1 it introduces some randomness to character selection
    closest = random.choice(closest_k[1])
    return chars[closest]


def construct_chr_img(img, px2char_func):
    # using kdtree to find the closest character for each pixel given its brightness

    width, height = img.size

    # empty matrix to store corresponding character for each pixel
    np.zeros((width, height), dtype='object')
    img_arr = np.array(img)
    func = np.vectorize(px2char_func)
    chr_arr = func(img_arr)
    return chr_arr


def make_image(img_path, tree, k, factor, width, chars, normalize=True):
    # read image
    img = Image.open(img_path)

    # procces image
    processed_img = proccess_image(img, factor, normalize=normalize)

    # resize image
    resized_processed_img = resizing(processed_img, width)

    # if k is bigger than 1 it introduces some randomness to character selection
    if k == 1:
        px2char_func = lambda pixel: pxl2chr(pixel, tree, chars)
    else:
        px2char_func = lambda pixel: rand_px2chr(pixel, tree, chars, k)
    # turn image into characters

    chr_img = construct_chr_img(resized_processed_img, px2char_func)
    return chr_img


def show_image(closest_chrs, seb):
    for i in range(closest_chrs.shape[0]):
        print('', end='\n')
        for j in range(closest_chrs.shape[1]):
            print(closest_chrs[i, j], end=seb)


def save_image(closest_chrs, name, seb='.'):
    img_string = ''
    for i in range(closest_chrs.shape[0]):
        img_string += seb.join(closest_chrs[i]) + ' \n'
    with open(name, 'w') as file:
        file.write(img_string)