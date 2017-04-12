from SimpleCV import JpegStreamCamera, Image, FaceRecognizer

cam = JpegStreamCamera("http://192.168.1.9:8080/video")
recognizer = FaceRecognizer()
recognizer.load("Saranyaraj_Others(Gates-Elon-Sathiya)_trainingdata.xml")

while True:
    img = cam.getImage()
    feat = img.findAndRecognizeFaces(recognizer, "face.xml")
    if feat is not None:    	
	for feature, label, confidence in feat:
        	feature.draw(width=4)
        	img.drawText(str("Saranyaraj" if label else "Unauthorised"), fontsize=30)
        	img.show()



