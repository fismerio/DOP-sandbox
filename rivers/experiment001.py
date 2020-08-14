import cv2
# import numpy as np

river = []
shape = [640,480]

def build_river(river,shape):
    # Add list of river branches.
    # Each branch adds more branch until bottom of the window.
    # river = [[],[]]
    x1 = shape[1] // 2
    y1 = 0
    x2 = x1
    y2 = y1 + 50
    color1 = (0, 255, 0)
    thick = 20
    river.append([(x1,y1),(x2,y2),color1,thick])

    x1 = x2
    y1 = y2
    x2 = x1 + 50
    y2 = y1 + 50
    color1 = (0, 200, 0)
    thick = 15
    river.append([(x1,y1),(x2,y2),color1,thick])

    x1 = x2
    y1 = y2
    x2 = x1 - 50
    y2 = y1 + 50
    color1 = (0, 200, 0)
    thick = 15
    river.append([(x1,y1),(x2,y2),color1,thick])

    x1 = x2
    y1 = y2
    x2 = x1 + 50
    y2 = y1 + 50
    color1 = (0, 150, 0)
    thick = 10
    river.append([(x1,y1),(x2,y2),color1,thick])

    x1 = x2
    y1 = y2
    x2 = x1 - 50
    y2 = y1 + 50
    color1 = (0, 150, 0)
    thick = 10
    river.append([(x1,y1),(x2,y2),color1,thick])



def draw_river(img, river):
    # Traverse the list river and draw each segment.
    # for segment in river:
    #     cv2.line(img,(segment[0][0],segment[0][1]),(segment[1][0],segment[1][1]),(0, 255, 0), 3)

    # x1 = img.shape[1] // 2
    # y1 = 0
    # x2 = img.shape[1] // 2
    # y2 = img.shape[0] // 2
    # color1 = (0, 255, 0)
    # thick = 3
    for segment in river:
        cv2.line(img, segment[0], segment[1], segment[2] , segment[3])


    pass

# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cap = cv2.VideoCapture("Resources/test-video.mp4")
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
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
