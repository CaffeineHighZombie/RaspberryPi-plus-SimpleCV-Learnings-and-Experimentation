from SimpleCV import Image

image = Image("./TestFiles/faces.jpg")
faces = image.findHaarFeatures('face.xml', min_neighbors=5)
faces.draw(width=4)
image.show()
