
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

print cap
print(cap.get(3))
print(cap.get(4))
# if cv2.isOpened
print("Hello World")

# def invert_image(imagem, new_name):
#     imagem = (255-imagem)
#     cv2.imwrite(new_name, imagem)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Uninvert camera image (flip image over Y-Axis)
    pos_flipped_gray =  cv2.flip(gray,1)
    # cv2.imshow('frame1',pos_flipped_gray)

    flipped_gray = (255 - pos_flipped_gray)
    # cv2.imshow('Negative',inverted)
    # ///////////////////////////


    kernel = np.ones((3,3),np.uint8)
    mask_eroded = cv2.erode(flipped_gray, kernel, iterations = 22)

    # Blur
    blurred = cv2.blur(mask_eroded, (5,5))

    # Dilate
    mask_dilated = cv2.dilate(blurred, kernel, iterations = 22)

    # Find Contours
    ret, thresh_neg = cv2.threshold(mask_dilated, 127,255,0)

    # cv2.imshow("neg", thresh)
    # cv2.imshow("pos", (255 - thresh))

    # thresh_pos = (255 - thresh_neg)

    # contours_pos, hierarchy_p = cv2.findContours(thresh_pos, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_neg, hierarchy_n = cv2.findContours(thresh_neg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # contours_neg = get_largest_contour(contours_neg)

    # pos = pos_flipped_gray
    neg = flipped_gray
    # if(contours_pos):
    # cv2.drawContours(pos, contours_pos, -1, (0,255,0), 3)
    # if(contours_neg):
    cv2.drawContours(neg, contours_neg, -1, (0,255,0), 3)

    # cv2.imshow('Pos', pos)
    cv2.imshow('Neg', neg)
    
    # cv2.imshow('frame1',flipped_gray)
    # ///////////////////////////

    # gray_x =  cv2.flip(gray,0)
    # flipped_gray_x =  cv2.flip(flipped_gray,0)

    # Display the resulting frame
    
    # cv2.imshow('frame2',gray)

    # cv2.imshow('frame3',flipped_gray_x)
    # cv2.imshow('frame4',gray_x)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()