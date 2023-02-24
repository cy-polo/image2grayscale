def deserializeBMP(nameFile):
    header = []
    dataImage = []

    file = open(nameFile, "rb")
    data = file.read()
    file.close()

    for index in range(54):
        header.append(data[index])

    for index in range(54, len(data)):
        dataImage.append(data[index])

    pixels = []

    for index in range(0, len(data), 3):
        pixels.append([data[index], data[index + 1], data[index + 2]])

    return header, pixels