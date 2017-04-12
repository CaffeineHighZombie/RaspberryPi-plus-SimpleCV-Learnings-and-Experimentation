from SimpleCV import Image
from os import getcwd, walk

f =[]
for (dirpath, dirnames, filenames) in walk(getcwd()):
	f.extend(filenames)
	break
#print(f)

for imgFile in f:
	img = Image(imgFile)
	feat = img.findHaarFeatures('face.xml', min_neighbors=5)
	count = 0
	for face in feat:
		i = face.crop()
		i.save('face'+str(count)+'_'+imgFile)
	


