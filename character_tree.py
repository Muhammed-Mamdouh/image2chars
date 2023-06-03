import matplotlib.pyplot as plt
from scipy import spatial
import numpy as np


def get_chrs(asci_range=(32, 127)):
    ascii_chars = dict(zip(range(*asci_range), map(chr, range(*asci_range))))
    ascii_chars.pop(95)
    ascii_chars.pop(96)

    # list of characters
    chars = list(ascii_chars.values())
    return chars


def make_chr_tree(chrs):
    # list of characters' brightness
    chrs_brightness = []
    for c in chrs:
        # Make a random plot...
        fig = plt.figure(figsize=(2, 2))
        fig.add_subplot(111)
        plt.text(0.5, 0.5, c, fontsize=200, verticalalignment='center', horizontalalignment='center')
        # If we haven't already shown or saved the plot, then we need to
        # draw the figure first...
        plt.axis('off')
        fig.tight_layout()
        fig.canvas.draw()
        plt.close()

        # Now we can save it to a numpy array.
        data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))[:, :, 0] < 255
        chrs_brightness.append([data.sum()])
    chars_brightness_arr = np.array(chrs_brightness)
    # normalize characters brightness
    chars_brightness_arr = ((chars_brightness_arr - chars_brightness_arr.min()) / (
            chars_brightness_arr.max() - chars_brightness_arr.min())) * 255
    # train KD Tree
    tree = spatial.KDTree(np.stack(chars_brightness_arr))
    return tree, chrs

