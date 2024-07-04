import typing as typ
import cv2
import numpy as np
from loopfinder import utils


def canny_masker(
    img: np.ndarray,
    min_sharpness=100,
):
    return cv2.Canny(img, min_sharpness, min_sharpness + 10)


def mini_canny_masker(
    img: np.ndarray, min_sharpness: int = 100, processing_size=(128, 128)
) -> np.ndarray:
    small_img = cv2.resize(img, processing_size)
    edges = canny_masker(small_img, min_sharpness=min_sharpness)
    return cv2.resize(edges, img.shape[::-1], interpolation=cv2.INTER_NEAREST)


def find_tip_of_mask(
    mask: np.ndarray, head_orientation: utils.HeadComesFrom
) -> typ.Optional[tuple[int, int]]:
    """
    Finds the coordinates of the furthest point in the mask from the goniometer head.
    """
    match head_orientation:
        case utils.HeadComesFrom.BELOW:
            # call this again, but flip the input and flip the output
            flipped_mask = mask[-1::-1]
            ret = find_tip_of_mask(flipped_mask, utils.HeadComesFrom.ABOVE)
            if ret is None:
                return None
            x, y = ret
            height = mask.shape[0]
            return x, height - y - 1

        case utils.HeadComesFrom.ABOVE:
            for y in range(len(mask) - 1, 0, -1):  # starting at the bottom, go upwards
                row = mask[y]
                if any(row):
                    nonzero_indexes = np.nonzero(row)[0]
                    leftmost = nonzero_indexes[0]
                    rightmost = nonzero_indexes[-1]
                    x = (rightmost + leftmost) // 2
                    return x, y
    return None


def find_loop(
    img: np.ndarray, head_orientation=utils.HeadComesFrom.ABOVE
) -> typ.Optional[tuple[int, int]]:
    """
    return values are x, y pixel coordinates of the loop tip.
    returns None if there is no foreground visible.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    mask = mini_canny_masker(gray)
    utils.save_img("mask", mask)
    tip = find_tip_of_mask(mask, head_orientation)
    if tip:
        x, y = tip
        utils.save_img("cross", utils.draw_crosshair(img, y, x))
    return tip
