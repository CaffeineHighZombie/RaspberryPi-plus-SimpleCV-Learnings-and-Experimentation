from SimpleCV import *

MIN_BLOB_SIZE = 1000 #Change this depending on the required sensitivity

cam = Camera(2) #Using USB connected camera for testing purpose on Ubuntu PC

old_image = cam.getImage()

while True:
	new_image = cam.getImage()
	diff = new_image - old_image
	blobs = diff.findBlobs(minsize=MIN_BLOB_SIZE)
	if blobs:
		print("Movement detected")
	old_image = new_image

