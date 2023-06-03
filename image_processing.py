from PIL import Image, ImageOps, ImageEnhance
import numpy as np


def resizing(img, width):
    # Given an image `img` and a desired width `width` in terms of number of characters,
    # resize the image while maintaining its aspect ratio
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio)
    # Resize image based on width
    resized_photo = img.resize((width, height))
    return resized_photo


def process_image(img, contrast_factor, normalize=True):
    # Given an image `img`, a contrast factor `contrast_factor`, and a boolean `normalize`, process the image by
    # increasing contrast, converting it to grayscale, and normalizing its pixel values (if `normalize` is True)
    # Increase contrast by factor of `contrast_factor`
    enhancer = ImageEnhance.Contrast(img)
    enhanced_img = enhancer.enhance(contrast_factor)

    # Convert image to grayscale (black and white)
    enhanced_img_grayscale = ImageOps.grayscale(enhanced_img)

    # Normalize image to be between 0-255
    if normalize:
        arr = np.array(enhanced_img_grayscale)
        arr = ((arr - arr.min()) / (arr.max() - arr.min())) * 255
        enhanced_img_grayscale_norm = Image.fromarray(arr.astype('uint8'), 'L')
        return enhanced_img_grayscale_norm

    return enhanced_img_grayscale