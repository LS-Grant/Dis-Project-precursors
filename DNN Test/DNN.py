#INPUT
# python DNN.py --image (IMAGE PATH) --prototxt (DEPLOY PROTOTXT FILE) --model (CAFFE MODEL FILE)
#Example input = python DNN.py --image Test2.jpg --prototxt DNNtest.prototxt.txt --model Face.caffemodel


import numpy as np
import argparse
import cv2

#Constructs a parser for the arguments on compiling# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
ap.add_argument("-p", "--prototxt", required=True)
ap.add_argument("-m", "--model", required=True)
ap.add_argument("-c", "--confidence", type=float, default=0.5)
args = vars(ap.parse_args())

net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

#Loads the input image 
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
	(300, 300), (104.0, 177.0, 123.0))

# Obtains the face detections
net.setInput(blob)
detections = net.forward()
#This section loops over the faces detected to draw the boxes around them
for i in range(0, detections.shape[2]):
	#Determins the conifdence of the detection
	confidence = detections[0, 0, i, 2]
	#Filters out low confidence basedon the parameter set at the parseing arguments
	if confidence > args["confidence"]:
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
		#Draws the rectangle around the detected faces, it also displays the
		#the level of confidence it has that what it has detected is a face
		text = "{:.2f}%".format(confidence * 100)
		y = startY - 10 if startY - 10 > 10 else startY + 10
		cv2.rectangle(image, (startX, startY), (endX, endY),
			(0, 0, 255), 2)
		cv2.putText(image, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

#Displays the image when the computations are complete
cv2.imshow("Output", image)
cv2.waitKey(0)