from PIL import Image, ImageOps, ImageEnhance
import numpy as np


def resizing(img, width):
    # width: the width in terms of number of characters
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio)

    # resize img based on width
    resized_photo = img.resize((width, height))
    return resized_photo


def proccess_image(img, contrast_factor, normalize=True):
    # increase contrast by factor of 'Contrast_factor'
    enhancer = ImageEnhance.Contrast(img)
    enhanced_img = enhancer.enhance(contrast_factor)

    # change image to grayscale (black and white)
    enhanced_img_grayscale = ImageOps.grayscale(enhanced_img)

    # normalize image to be between 0-255
    if normalize:
        arr = np.array(enhanced_img_grayscale)
        arr = ((arr - arr.min()) / (arr.max() - arr.min())) * 255
        enhanced_img_grayscale_norm = Image.fromarray(arr.astype('uint8'), 'L')
        return enhanced_img_grayscale_norm

    return enhanced_img_grayscale
