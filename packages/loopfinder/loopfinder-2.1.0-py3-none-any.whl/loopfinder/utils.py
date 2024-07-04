from datetime import datetime
from enum import Enum, auto
import os
import cv2


class HeadComesFrom(Enum):
    """
    Represents the orientation of the goniometer head.
    """

    ABOVE = auto()
    BELOW = auto()


def draw_crosshair(img, row, col, thickness=2, color=(128, 128, 128)):
    out = img.copy()
    out[row - thickness : row + thickness, :] = color  # draw horisontal line
    out[:, col - thickness : col + thickness] = color  # draw vertical line
    return out


def save_img(label, img):
    img_diag_dir = os.environ.get("LOOPFINDER_DIAGNOSTICS_PATH")
    if not img_diag_dir or not os.path.isdir(img_diag_dir):
        return
    path = img_diag_dir + "{}-{}.png".format(datetime.isoformat(datetime.now()), label)
    # logger.debug("saving image to {}".format(path))
    cv2.imwrite(path, img)
