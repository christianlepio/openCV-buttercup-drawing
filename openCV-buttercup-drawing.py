import cv2 as cv
import numpy as np

obj = np.zeros((600, 850, 3), dtype="uint8")

#Background Color
obj[:] = 203, 192, 255

#CIRCLE ARMS
cv.circle(obj, (370,515), 120, (0,0,0), thickness=3)
cv.circle(obj, (370,515), 120, (196, 228, 255), thickness=cv.FILLED)
cv.circle(obj, (480,515), 120, (0,0,0), thickness=3)
cv.circle(obj, (480,515), 120, (196, 228, 255), thickness=cv.FILLED)

#CIRCLE BODY
cv.circle(obj, (425, 500), 150, (0, 190, 0), thickness=cv.FILLED)
cv.circle(obj, (425, 500), 150, (0, 0, 0), thickness=2)
cv.circle(obj, (425, 410), 61, (0,0,0), thickness=2)
cv.circle(obj, (425, 410), 60, (196, 228, 255), thickness=cv.FILLED)

#RECTANGLE CHEST
cv.rectangle(obj, (300,490), (550,550), (255,2555,255), thickness=cv.FILLED)
cv.rectangle(obj, (300,490), (550,550), (0,0,0), thickness=2)


#CIRCLE HEAD
cv.circle(obj, (360, 250), 150, (0,0,0), thickness=cv.FILLED)
cv.circle(obj, (490, 250), 150, (0,0,0), thickness=cv.FILLED)
cv.circle(obj, (320, 70), 150, (203,192,255), thickness=cv.FILLED)
cv.circle(obj, (530, 70), 150, (203,192,255), thickness=cv.FILLED)
cv.circle(obj, (425, 300), 150, (0,0,0), thickness=5)
cv.circle(obj, (425, 300), 150, (196, 228, 255), thickness=cv.FILLED)

#CIRCLE EYE
cv.circle(obj, (350,290), 70, (255,255,255), thickness=cv.FILLED)
cv.circle(obj, (357,292), 64, (0,255,0), thickness=cv.FILLED)
cv.circle(obj, (367,297), 52, (0,0,0), thickness=cv.FILLED)
cv.circle(obj, (380,305), 25, (255,255,255), thickness=cv.FILLED)
cv.circle(obj, (350,290), 71, (0,0,0), thickness=1)
cv.circle(obj, (500,290), 70, (255,255,255), thickness=cv.FILLED)
cv.circle(obj, (493,292), 64, (0,255,0), thickness=cv.FILLED)
cv.circle(obj, (483,297), 52, (0,0,0), thickness=cv.FILLED)
cv.circle(obj, (470,305), 25, (255,255,255), thickness=cv.FILLED)
cv.circle(obj, (500,290), 71, (0,0,0), thickness=1)
cv.circle(obj, (425,390), 20, (0,0,0), thickness=cv.FILLED)
cv.circle(obj, (425,385), 18, (196, 228, 255), thickness=cv.FILLED)

#LINE HAIR
cv.line(obj, (285,242), (405, 242), (0,0,0), thickness=3)
cv.line(obj, (445,242), (570, 242), (0,0,0), thickness=3)
cv.line(obj, (405,242), (425, 212), (0,0,0), thickness=3)
cv.line(obj, (425,212), (445, 242), (0,0,0), thickness=3)
cv.line(obj, (400,155), (450, 155), (0,0,0), thickness=9)
cv.line(obj, (378,159), (472, 159), (0,0,0), thickness=9)
cv.line(obj, (362,165), (488, 165), (0,0,0), thickness=9)
cv.line(obj, (352,170), (498, 170), (0,0,0), thickness=9)
cv.line(obj, (342,177), (508, 177), (0,0,0), thickness=10)
cv.line(obj, (331,185), (519, 185), (0,0,0), thickness=9)
cv.line(obj, (323,192), (527, 192), (0,0,0), thickness=9)
cv.line(obj, (315,200), (535, 200), (0,0,0), thickness=9)
cv.line(obj, (309,208), (541, 208), (0,0,0), thickness=9)
#LINE LEFT
cv.line(obj, (305,213), (420, 213), (0,0,0), thickness=9)
cv.line(obj, (301,221), (416, 221), (0,0,0), thickness=9)
cv.line(obj, (295,228), (411, 228), (0,0,0), thickness=9)
cv.line(obj, (290,233), (405, 233), (0,0,0), thickness=9)
cv.line(obj, (280,236), (400, 236), (0,0,0), thickness=9)
#LINE RIGHT
cv.line(obj, (422,213), (545, 213), (0,0,0), thickness=9)
cv.line(obj, (434,221), (550, 221), (0,0,0), thickness=9)
cv.line(obj, (442,228), (555, 228), (0,0,0), thickness=9)
cv.line(obj, (447,233), (560, 233), (0,0,0), thickness=9)
cv.line(obj, (450,236), (562, 236), (0,0,0), thickness=9)

#PUT TEXT
cv.putText(obj, "Buttercup", (345, 530), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.3, (0,0,0), thickness=2)



cv.imshow("ACTIVITY 1", obj)
cv.waitKey(0)