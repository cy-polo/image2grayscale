from deserializer import deserializeBMP
from serializer import serializeBMP
from utils import grayscale

header, data = deserializeBMP("assets/input.bmp")
dataImg = grayscale(data)
serializeBMP("assets/output.bmp", header, dataImg)

print("Image converted successfully!")