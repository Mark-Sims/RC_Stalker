# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)
 
# ret, frame = cap.read()

# # Our operations on the frame come here

# imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



# kernel = np.ones((3,3),np.uint8)
# mask_eroded = cv2.erode(imgray, kernel, iterations = 1)

# # Dilate
# mask_dilated = cv2.dilate(mask_eroded, kernel, iterations = 1)

# # Find Contours
# ret, thresh = cv2.threshold(mask_dilated, 127,255,0)

# cv2.imshow('2222', thresh)

# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# #count = contours[0]

# #v2.drawContours(im,contours,-1,(0,255,0),3)

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     exit()

def get_largest_contour(contours):

	# Calculate rectangles around min,min and max, max.
	# Note, this is only taking 2 points into account... nvm it is doing
	# top, bottom, left and right most points, and drawing a rectangle
	for x in xrange(len(contours)):
		min_x = wid
		max_x = 0
		min_y = hei
		max_y = 0
		# print "wid",wid
		# print "hei",hei
		for point in contours[x]:
			# print point[0][0]
			if point[0][0] < min_x:# and point[0][0] > 80:
				if(point[0][0] > 40 and point[0][0] != 0):
					min_x = point[0][0]
			elif point[0][0] > max_x:# and point[0][0] < wid - 80:
				if(point[0][0] < wid - 40 and point[0][0] != 0):
					max_x = point[0][0]
			if point[0][1] < min_y:
				if(point[0][1] > 40 and point[0][1] != 0):
					min_y = point[0][1]
			elif point[0][1] > max_y:# and point[0][1] < hei - 80:
				if(point[0][1] < hei - 40 and point[0][1] != 0):
					max_y = point[0][1]
		contour = np.array([[[min_x, min_y]], [[min_x, max_y]], [[max_x, max_y]], [[max_x, min_y]]])
		# Start in upper left, goes counter clock-wise
		contours[x] = contour

	# Now calculate the area of each contour, and select only the biggest

	max_area = 0
	largest_contour = 0
	for x in xrange(len(contours)):

		# 		 contours[contour number][point][0][0:x or 1:y]

		length = contours[x]			 [2]	[0][0] - contours[x][0][0][0]
		height = contours[x]			 [2]	[0][1] - contours[x][0][0][1]

		# print "length:", length
		# print "height:", height
		area = length * height

		if(height < 0 or length < 0):
			continue
		# print "area:", area

		if area > max_area:
			max_area = area
			largest_contour = x


	# {
	# min_x = contours[largest_contour][0][0][0]
	# min_y = contours[largest_contour][0][0][1]
	# max_x = contours[largest_contour][2][0][0]
	# max_y = contours[largest_contour][2][0][1]
	# contourz = [np.array(([[[min_x, min_y]], [[min_x, max_y]], [[max_x, max_y]], [[max_x, min_y]]]))]
	# }

	if(len(contours) <= largest_contour):
		return -1
	else:
		# print "selected:", contours[largest_contour]
		return [contours[largest_contour]]


# print len(contours)
# #print count


import numpy as np
import cv2
# import move

cap = cv2.VideoCapture(1)

ret, fram = cap.read()

hei, wid, dep = fram.shape

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

    contours_neg, hierarchy_n = cv2.findContours(thresh_neg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours_neg = get_largest_contour(contours_neg)

    if(contours_neg == -1):
    	continue;

    neg = flipped_gray

    cv2.drawContours(neg, contours_neg, -1, (0,255,0), 3)
    # print "1", contours_neg[0][0][0][0]
    # print "2", contours_neg[0][3][0][0]
    # print "3", contours_neg[0][1][0][1]
    # print "4", contours_neg[0][2][0][1]

    middle_x = (contours_neg[0][0][0][0] + contours_neg[0][3][0][0])/2
    middle_y = (contours_neg[0][1][0][1] + contours_neg[0][0][0][1])/2



    # img = np.zeros((480,640,1), np.uint8)
    # # Top Left
    # cv2.circle(img,(contours_neg[0][0][0][0], contours_neg[0][0][0][1]), 5, (255,0,0), 5)    

    # # Top Right
    # cv2.circle(img,(contours_neg[0][3][0][0], contours_neg[0][3][0][1]), 5, (255,0,0), 5)    

    # # Bottom Left:
    # cv2.circle(img,(contours_neg[0][1][0][0], contours_neg[0][1][0][1]), 5, (255,0,0), 5)

    # # Bottom Right
    # cv2.circle(img,(contours_neg[0][2][0][0], contours_neg[0][2][0][1]), 5, (255,0,0), 5)    

    # cv2.imshow('image',img)

    if(middle_y > 260):
    	# move.forward()
    	print "forward"
    else:
    	print "stopped"
    if(middle_x < 300):
    	print "RIGHT"
    if(middle_x > 340):
    	print "LEFT"

    # if(middle_x)

    # print contours_neg[0]
    # print contours_neg[0][0]
    # print contours_neg[0][0][0]
    # print middle_x, middle_y

    cv2.imshow('Neg', neg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
