import cv2
import numpy as np

def nothing(*arg):
        pass

image = 'C:\sample\80.jpg'
img = cv2.imread(image)
# Check if image is loaded fine
if img is None:
    print ('Error opening image!')

while True:

    #convert image to grayscale
    imgs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Grayscale', imgs)

    #blur method
    imgb = cv2.GaussianBlur(imgs, (15, 15), 0)
    #cv2.imshow('Blur', imgb)

    #finding circle in image
    circles = cv2.HoughCircles (imgb, cv2.HOUGH_GRADIENT, 1, 80,
                param1 = 40,
                param2 = 20,
                minRadius = 20,
                maxRadius = 40)

    #drawing circle
    #circles = np.uint8(np.around(circles))
    #for i in circles[0,:]:
        #edge
        #cv2.circle(img,(i[0],i[1]),i[1],(255,0,0),2)
        #center
        #cv2.circle(imgb,(i[0],i[1]),1,(255,255,255),1)

    # draw mask
    mask = np.full((imgb.shape[0], imgb.shape[1]), 0, dtype=np.uint8)
    for i in circles[0, :]:
        cv2.circle(mask, (i[0], i[1]), i[1], (255, 255, 255), -1)

    #show drawn circle
    cv2.imshow("detected", img)

    mask1 = cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow('mask1', mask1)

    #finding countours
    imgc, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #draw specified countour
    cnt = contours[0]
    cv2.drawContours(img, [cnt], -1, (255,0,0), 2)
    #cv2.drawContours(img, contours, 0, (0,255,0), 4)
    #x,y,w,h = cv2.boundingRect(cnt)
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #cv2.imshow("BB", img)
    #cv2.imshow("countour", img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
#print(mask1)
cv2.destroyAllWindows()
