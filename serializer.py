def serializeBMP(nameFile, header, pixels):
    file = open(nameFile, "wb")

    for index in range(len(header)):
        file.write(bytes([header[index]]))

    for pixel in pixels:
        for value in pixel:
            file.write(bytes([value]))

    file.close()