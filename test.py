import cv2
from videostabilizer import VideoStabilizer

video = cv2.VideoCapture("path-to-your-video")
stabilizer = VideoStabilizer(video)

while True:
	success, _, frame = stabilizer.read()
	if not success:
		print("No frame is captured.")
		break
		
	cv2.imshow("frame", frame)
	if cv2.waitKey(20) == 27:
		break
