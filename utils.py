def grayscale(pixels):
    for index in range(len(pixels)):
        gray_value = int((pixels[index][0] + pixels[index][1] + pixels[index][2]) / 3)
        pixels[index] = [gray_value, gray_value, gray_value]

    return pixels