from SimpleCV import Image, Camera, Display

# Initialize the camera
cam = Camera(2) #Using USB connected camera for testing purpose on Ubuntu PC
# Initialize the display
display = Display()

while True:
	# Sanp a picture using the camera
	image = cam.getImage()
	# Find faces with Haar Feature detection
	faces = image.findHaarFeatures('face.xml', min_neighbors=5)
	faces.draw(width=4)
	# Show the picture on the display
	image.save(display)
