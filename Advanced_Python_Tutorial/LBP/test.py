
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
from skimage.feature import local_binary_pattern # # pip install scikit-image

def displayImages(img, title):
    plt.figure()
    plt.axis("on")
    plt.title(title)
    plt.imshow(img,cmap='gray' )
    plt.show()

def calculateLBP(pixel, column, line):
    values = thresholded(pixel[line, column], neighbors(pixel, column, line))
    weights = [1, 2, 4, 8, 16, 32, 64, 128]
    lbp = 0
    for i in range(0, len(values)):
        lbp += values[i] * weights[i]
    return lbp

def neighbors(pixels, column, line):
        p1 = binary_neighbor_values(pixels, line - 1, column - 1)
        p2 = binary_neighbor_values(pixels, line - 1, column)
        p3 = binary_neighbor_values(pixels, line - 1, column + 1)
        p4 = binary_neighbor_values(pixels, line, column + 1)
        p6 = binary_neighbor_values(pixels, line, column - 1)
        p7 = binary_neighbor_values(pixels, line + 1, column - 1)
        p8 = binary_neighbor_values(pixels, line + 1, column)
        p9 = binary_neighbor_values(pixels, line + 1, column + 1)
        positions = [p1,p2,p3,p4,p6,p7,p8,p9]

        return positions

def thresholded(center, neighbours):
    result = []
    for neighbour in neighbours:
        if neighbour >= center:
            result.append(1)
        else:
            result.append(0)
    return result

def binary_neighbor_values(pixel, line, column):
    # if the index does not exist return 0
    try:
        return pixel[line, column]
    except IndexError:
        return 0
def _histogram(img, title):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    # cumsum -> Return the cumulative sum of the elements along a given axis.
    # CDF: cumulative distribution function
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.title(title)
    plt.legend(('Cumulative Distribution Function (CDF)', 'Histogram'), loc='upper left')
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    start = time.time()
    input_file1 = "C:\\Users\\TGDD\\PycharmProjects\\LBP\\LeNa_color.png"
    input_file2 = "C:\\Users\\TGDD\\PycharmProjects\\LBP\\Lena_grayscale.jpg"
    input = input_file1
    if os.path.isfile(input):
        # start = time.time()
        image = cv2.imread(input,0)
        height = len(image)
        width = len(image[0])
        img_lbp = np.zeros((height, width, 3), np.uint8)
        for line in range(height):
            for column in range(width):
                img_lbp[line, column] = calculateLBP(image, column, line)
        print(str(time.time() - start) + " s")

        # displayImages(img_lbp, "Lena image")
        _histogram(image, "Result 1")
        _histogram(img_lbp, "Result 2")
        displayImages(img_lbp, "Lena image")
    else:
        print("File '{}' does not exist.".format(input))

