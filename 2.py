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
		min_x = 800
		max_x = 0
		min_y = 1000
		max_y = 0
		for point in contours[x]:
			# print point[0][0]
			if point[0][0] < min_x:
				min_x = point[0][0]
			elif point[0][0] > max_x:
				max_x = point[0][0]
			if point[0][1] < min_y:
				min_y = point[0][1]
			elif point[0][1] > max_y:
				max_y = point[0][1]
		contour = np.array([[[min_x, min_y]], [[min_x, max_y]], [[max_x, max_y]], [[max_x, min_y]]])
		# contour = [[[min_x, min_y]], [[max_x, max_y]]]
		# print "---Contour:---"
		# print contour
		# print "---Numpy:---"
		contours[x] = contour

	# Now calculate the area of each contour, and select only the biggest

	max_area = 0
	largest_contour = 0
	for x in xrange(len(contours)):
		length = 0
		height = 0
		area = 0
		# 		 contours[contour number][point][0][0:x or 1:y]
		length = contours[x]			 [2]	[0][0] - contours[x][0][0][0]
		height = contours[x]			 [2]	[0][1] - contours[x][0][0][1]

		# print "length:", length
		# print "height:", height
		area = length * height

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

	return [contours[largest_contour]]


# print len(contours)
# #print count


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

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
    #blurred = cv2.blur(mask_eroded, (5,5))

    # Dilate
    mask_dilated = cv2.dilate(mask_eroded, kernel, iterations = 22)

    # Find Contours
    ret, thresh_neg = cv2.threshold(mask_dilated, 127,255,0)

    # cv2.imshow("neg", thresh)
    # cv2.imshow("pos", (255 - thresh))

    # thresh_pos = (255 - thresh_neg)

    # contours_pos, hierarchy_p = cv2.findContours(thresh_pos, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_neg, hierarchy_n = cv2.findContours(thresh_neg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # contours_pos = get_largest_contour(contours_pos)
    contours_neg = get_largest_contour(contours_neg)

    # pos = pos_flipped_gray
    neg = flipped_gray
    # if(contours_pos):
    # cv2.drawContours(pos, contours_pos, -1, (0,255,0), 3)
    # if(contours_neg):
    cv2.drawContours(neg, contours_neg, -1, (0,255,0), 3)

    # cv2.imshow('Pos', pos)
    #cv2.imshow('Neg', neg)
    print "FRAME" 
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
