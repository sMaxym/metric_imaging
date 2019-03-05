from PIL import Image
from math import floor


def intensity_euclid(x, y, max_x, max_y, lb=0, ub=255):
    """

    :param x:
    :param y:
    :param lb:
    :param ub:
    :return:
    """
    intens = (x ** 2 + y ** 2) ** 0.5
    max_intens = (max_x ** 2 + max_y ** 2) ** 0.5
    intens = ub / max_intens * intens
    return floor(intens)


def intensity_hamming(x, y, max_x, max_y, lb=0, ub=255):
    """

    :param x:
    :param y:
    :param lb:
    :param ub:
    :return:
    """
    intens_code = int(bin(x)[2:]) ^ int(bin(y)[2:])
    intens = str(intens_code).count('1')
    max_intens = max(len(bin(max_x)), len(bin(max_y))) - 2
    intens = ub / max_intens * intens
    return floor(intens)


if __name__ == '__main__':
    w, h = 1000, 1000
    img = Image.new('RGB', (w, h))
    pixelmap = img.load()
    for row in range(img.size[0]):
        for col in range(img.size[1]):
            color = intensity_hamming(row + 1, col + 1, w, h)
            pixelmap[row, h - col - 1] = (color, 0, color)
    img.save('hamming.bmp')