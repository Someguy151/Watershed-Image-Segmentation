# Watershed Segmentation Project
# Author: Jonathan Hooper
# Date: 04/30/2023
# updated: 05/07/2023

import cv2
# Import libraries
import numpy as np


def image_segmentation(image_path):
    # Step 1: Pre-processing
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 2: Thresholding - Binary image
    binary = threshold(gray, 127)

    # Step 3: Morphological Operations
    kernel = np.ones((5, 5), np.uint8)  # structuring element

    eroded = erode(binary, kernel, iterations=2)
    opening = cv2.morphologyEx(eroded, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Step 4: Distance Transform
    dist_tf = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_tf, 0.4 * dist_tf.max(), 255, 0)

    # Step 5: locate the local maxima
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Step 6: Generate markers
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    # Step 7: Apply watershed algorithm
    markers = cv2.watershed(img, markers)

    traced_boundaries = np.zeros(img.shape, dtype=np.uint8)
    traced_original = img.copy()

    # img[markers == -1] = [255, 0, 0] # color the boundaries in blue
    # img[markers == -1] = [0, 255, 0] # color the boundaries in green
    # img[markers == -1] = [0, 0, 255] # color the boundaries in red

    # color the boundaries in blue
    traced_boundaries[markers == -1] = [255, 0, 0]
    # color the boundaries in blue
    traced_original[markers == -1] = [255, 0, 0]

    # output
    imshow("Original Image", img)
    imshow("Traced Boundaries", traced_boundaries)
    imshow("Traced Original", traced_original)


def threshold(img, T):  # global thresholding
    from numpy import mean, uint8, zeros

    # initialize the iteration counter
    iter = 0
    max_iter = 1000
    T_prev = 0

    while (iter < max_iter):
        # initialize the foreground and background pixel lists
        foreground_pixels = []
        background_pixels = []

        # iterate over the image
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                if img[i, j] > T:
                    foreground_pixels.append(img[i, j])
                else:
                    background_pixels.append(img[i, j])

        m1 = mean(foreground_pixels)
        m2 = mean(background_pixels)

        T = (m1 + m2) / 2

        # check if the threshold value has converged
        if T == T_prev:
            break

        T_prev = T

    # initialize the thresholded image
    img_thresholded = zeros(img.shape, dtype=np.uint8)

    # apply the threshold value
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if img[i, j] > T:
                img_thresholded[i, j] = 255
            else:
                img_thresholded[i, j] = 0

    return img_thresholded


def erode(img, kernel, iterations):
    # initialize the output image
    for i in range(iterations):
        output = np.zeros(img.shape, dtype=np.uint8)
        M, N = np.shape(img)

        # iterate over the image
        for i in range(0, M):
            for j in range(0, N):
                erosion_possible = True
                # iterate over the kernel (structuring element)
                for dy, row in enumerate(kernel):
                    for dx, value in enumerate(row):
                        if value == 1:
                            new_i = i + dy - 1
                            new_j = j + dx - 1
                            if new_i < 0 or new_i >= M or new_j < 0 or new_j >= N:
                                erosion_possible = False
                                break  # out of bounds
                            elif img[new_i, new_j] == 0:
                                erosion_possible = False
                                break  # pixel is not part of the object
                if erosion_possible:
                    output[i, j] = 255
                else:
                    output[i, j] = 0
    return output


def imshow(name_str, img_array):
    from cv2 import (WINDOW_AUTOSIZE, destroyAllWindows, imshow, imwrite,
                     namedWindow, waitKey)

    namedWindow(name_str, WINDOW_AUTOSIZE)
    imshow(name_str, img_array)
    print('\n******\n', name_str)
    print('\nPress "s" to save. Press any key to continue...\n')
    k = waitKey()

    if k == ord("s"):
        imwrite(name_str+'.png', img_array)

    destroyAllWindows()


if __name__ == "__main__":
    print('''\n\n
          **********************************************
          Watershed Segmentation Project
          **********************************************
          \n\n
          ''')
    image_path = "images/istanbul12.jpg"
    # image_path = "images/istanbul10.jpg"
    # image_path = "images/istanbul8.jpg"

    image_segmentation(image_path)
