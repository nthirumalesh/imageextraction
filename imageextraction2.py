import cv2
image1= cv2.imread("D:\img\pancard1.png")
#print(type(img))

# Shape of the image
print("coordinates of actual pancard", image1.shape)
arr = image1.shape

# [rows, columns]]
image_in_pan_card = image1[125:250, 20:143]

cv2.imshow('original', image1)
cv2.imshow('image in pan card', image_in_pan_card)
print("coordinates of the image in pard", image_in_pan_card.shape)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

image2 = cv2.imread("D:\img\pancard1.png")
#print(type(imgage2))

# Shape of the image
print("coordinates of second pancard", image2.shape)
arr1 = image2.shape




# [rows, columns]
image_in_pan_card1 = image2[125:250, 20:143]

if arr[0]==arr1[0] and arr[1]==arr1[1] and arr[2]==arr1[2]:
    print("co-ordinates of both cards matched")
else:
    print("coordinates of both cards are not matched")

cv2.imshow('second pan card', image2)
cv2.imshow('image in pan card1', image_in_pan_card1)
#print("coordinates of the image in second pard", image_in_pan_card1.shape)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

from skimage.metrics import structural_similarity
import imutils

#resize image
image1 = cv2.resize(image1, (250, 160))
#print("pancard1 image size:",img.size)
#pancard1.save('C:/pan_card_tampering/image/pancard1.png')
image2 = cv2.resize(image2, (250, 160))
#print("pancard2 image size",img1.size)
#pancard2.save('C:/pan_card_tampering/image/pancard2.png')

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

(score, diff) = structural_similarity(gray1, gray2, full=True)
diff = (diff*255).astype("uint8")
print("SSIM Score is:{}".format(score*100))



#calculating threshold and contours
thresh = cv2.threshold(diff, 0, 128, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#creating bounding boxes(contours)
no_of_differences=0
for c in cnts:
    #applying contours on images
    no_of_differences = no_of_differences + 1
    (x, y, w, h)=cv2.boundingRect(c)
    cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 0, 255),6)
    cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 0, 255),6)

print("number of differences", no_of_differences)
#show output images
cv2.imshow("pancard1", image1)
cv2.imshow("spot the differences", image2)
cv2.imshow("difference image", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
