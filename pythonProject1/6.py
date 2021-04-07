from PIL import Image


def load_image(filename):
    image = Image.open(filename)
    width, height = image.size
    pixels = list(image.getdata())
    image = [pixels[i:i + width] for i in range(0, len(pixels), width)]
    return image


def save_image(filename, image):
    flat_image = [item for sublist in image for item in sublist]
    height, width = len(image), len(image[0])
    image_out = Image.new("L", (width, height))
    image_out.putdata(flat_image)
    image_out.save(filename)


def mean(rgb):
    return (sum(rgb))//3


def weighted_mean(rgb):
    return int((0.3 * rgb[0]) + (0.59 * rgb[1]) + (0.11 * rgb[2]))


def color_to_grey(image, average=True):
    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if average:
                image[i][j] = mean(pixel)
            else:
                image[i][j] = weighted_mean(pixel)
    return image


if __name__ == "__main__":
    in_file = "signallost.jpg"
    out_file = "signal2.jpg"
    image = load_image(in_file)
    image = color_to_grey(image)
    save_image(out_file, image)
