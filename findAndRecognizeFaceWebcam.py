from SimpleCV import Camera, Image

cam = Camera()
img = cam.getImage()
recognizer = FaceRecognizer()
recognizer.load("training.xml")
feat = img.findAndRecognizeFaces(recognizer, "face.xml")
for feature, label, confidence in feat:
	i = feature.crop()
	i.drawTest(str(label))
	i.show()

