from PIL import Image


if __name__ == '__main__':
    w, h = 400, 400
    img = Image.new('RGB', (w, h))
    pixelmap = img.load()
    for row in range(img.size[0]):
        for col in range(img.size[1]):
            pixelmap[row, col] = (255, 0, 0)
    img.save('out.bmp')