from SimpleCV import Camera, Image, FaceRecognizer
import time

cam = Camera()
recognizer = FaceRecognizer()
recognizer.load("Saranyaraj_Others(Gates-Elon-Sathiya)_trainingdata.xml")

while True:
    img = cam.getImage()
    feat = img.findAndRecognizeFaces(recognizer, "face.xml")
    if feat is not None:    
	for feature, label, confidence in feat:
            i = feature.crop()
            i.drawText(str("Saranyaraj" if label else "Unauthorised"))
            i.show()
    time.sleep(1)


