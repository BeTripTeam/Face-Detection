from PIL import Image


def open_img(path_to_img) -> Image:
    """
    Opens image of appropriate type
    :param path_to_img: path to img
    :return: Image
    """
    f = open(path_to_img, 'r+b')
    return Image.open(f)
