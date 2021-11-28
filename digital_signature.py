import cv2
import numpy as np
import glob
import os
import sys

# Loading the image of the signature
sign = cv2.imread("mysign.png")
h_sign, w_sign, _ = sign.shape

path = str(sys.argv[1])
images_path = glob.glob(f"{path}/*.*")

print("Signing Images...")
for img_path in images_path:
    img = cv2.imread(img_path)
    h_img, w_img, _ = img.shape

    # Get the center of the original. It's the location where we will place the signature
    center_y = int(h_img / 2)
    center_x = int(w_img / 2)
    top_y = center_y - int(h_sign / 2)
    left_x = center_x - int(w_sign / 2)
    bottom_y = top_y + h_sign
    right_x = left_x + w_sign

    # Get ROI (Region of Interest)
    roi = img[top_y:bottom_y, left_x:right_x]

    # Add the Logo to the ROI
    result = cv2.addWeighted(roi, 1, sign, 0.5, 0)

    # Replace the ROI on the image
    img[top_y:bottom_y, left_x:right_x] = result

    # Get filename and save the image
    filename = os.path.basename(img_path)
    cv2.imwrite("images/signed_" + filename, img)

print("Signature added to images successfully!")
