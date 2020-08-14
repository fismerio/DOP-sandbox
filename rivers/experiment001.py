import cv2
from random import randrange
# import numpy as np
width = 640 * 2
height = 480 * 2
river = []
shape = [width,height]

def build_river(river,shape):
    # Add list of river branches.
    # Each branch adds more branch until bottom of the window.
    green = 255
    xMax = shape[1]
    yMax = shape[0]
    xMin = 0
    yMin = 0
    incrX = 5
    incrY = 5
    incrW = 1
    incrColor = -1

    x1 = xMax // 2
    y1 = yMin
    x2 = x1
    y2 = y1 + incrY
    color1 = (0, green, 0)
    thick = 1
    river.append([(x1,y1),(x2,y2),color1,thick])

    while (y1 < yMax):

        x1 = x2
        y1 = y2
        # x2 = x1 + incrX
        x2 = x1 + randrange(10) # random river
        y2 = y1 + incrY
        # thick = thick + incrW
        thick = thick + randrange(2)
        green = green + incrColor
        color1 = (0, green, 0)
        river.append([(x1,y1),(x2,y2),color1,thick])

        x1 = x2
        y1 = y2
        # x2 = x1 - incrX
        x2 = x1 - randrange(10) #random river
        y2 = y1 + incrY
        # thick = thick + incrW
        thick = thick + randrange(2)
        green = green + incrColor
        color1 = (0, green, 0)
        river.append([(x1,y1),(x2,y2),color1,thick])


def draw_river(img, river):
    # Traverse the list river and draw each segment.

    for segment in river:
        cv2.line(img, segment[0], segment[1], segment[2] , segment[3])

# --------------------------------------------- Main --------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

cap = cv2.VideoCapture(0)

cap.set(3,width)
cap.set(4,height)
cap.set(50,500)

build_river(river,shape)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGray2 = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
    draw_river(imgGray2, river)

    cv2.imshow( "DOP Sandbox", imgGray2)

    if cv2.waitKey(1) &  0xFF == ord('q'):
        break
