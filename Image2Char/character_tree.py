import matplotlib.pyplot as plt
from scipy import spatial
import numpy as np


def get_chars(ascii_range=(32, 127)):
    # Given an ASCII range, return a dictionary of ASCII characters within that range
    # excluding the underscore and backtick characters
    ascii_chars = dict(zip(range(*ascii_range), map(chr, range(*ascii_range))))
    ascii_chars.pop(95)  # remove underscore character
    ascii_chars.pop(96)  # remove backtick character
    # Convert dictionary values to a list of characters
    chars = list(ascii_chars.values())
    return chars


def make_char_tree(chars):
    # Given a list of characters `chars`, create a KD Tree of their brightness values Compute the brightness of each
    # character by creating a small plot of the character and counting the number of white pixels
    chars_brightness = []
    for c in chars:
        # Create a random plot of the character and count the number of white pixels
        fig = plt.figure(figsize=(2, 2))
        fig.add_subplot(111)
        plt.text(0.5, 0.5, c, fontsize=200, verticalalignment='center', horizontalalignment='center')
        plt.axis('off')
        fig.tight_layout()
        fig.canvas.draw()
        plt.close()
        data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))[:, :, 0] < 255
        chars_brightness.append([data.sum()])
    chars_brightness_arr = np.array(chars_brightness)
    # Normalize characters' brightness values to be between 0-255
    chars_brightness_arr = ((chars_brightness_arr - chars_brightness_arr.min()) / (
            chars_brightness_arr.max() - chars_brightness_arr.min())) * 255
    # Train a KD Tree on the normalized brightness values
    tree = spatial.KDTree(np.stack(chars_brightness_arr))
    return tree, chars