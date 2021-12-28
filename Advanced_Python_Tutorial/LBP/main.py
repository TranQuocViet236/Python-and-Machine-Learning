
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# to compare after
from skimage import feature

class LBP:
    def __init__(self, input):
        # Read the image and convert to grayscale
        self.image = cv2.imread(input, 0)
        # a copy of the image to transform
        self.transformed_img = cv2.imread(input, 0)
        # get size informations
        self.height = len(self.image)
        self.width = len(self.image[0])

    def execute(self):
        # Run a example of LBP
        # self.example()

        # We create a matrix with zeros that it will be replaced with 1 or 0.
        # We compare value of pixel[line,column] with values of its neighbours.
        # When neighbour >= center we replace with 1, otherwise 0.
        # This procedure is done by _thresholded method
        img_lbp = np.zeros((self.height, self.width, 3), np.uint8)

        # for each pixel we will find its LBP
        for line in range(self.height):
            for column in range(self.width):
                img_lbp[line, column] = self._calculateLBP(self.image, column, line)
        self._displayImages(self.transformed_img, "Result from algorithm developed")

    def _displayImages(self, transformed_img, title):
        plt.figure()
        plt.axis("off")
        plt.title(title)
        plt.imshow(transformed_img, cmap='gray')
        plt.show()

    def _calculateLBP(self, pixel, column, line):
        # Now we want to get LBP for pixel[line,column].
        # we compare grey level value of pixel[line,column] with values of its neighbours
        # starting at the top-left pixel and moving clockwise
        values = self._thresholded(pixel[line, column], self._get_positions(pixel, column, line))

        # Mask with the weights
        weights = [1, 2, 4, 8, 16, 32, 64, 128]

        lbp = 0
        for i in range(0, len(values)):
            lbp += values[i] * weights[i]

        # Transform the image with the new value
        self.transformed_img.itemset((line, column), lbp)

        return lbp

    def _get_positions(self, pixels, column, line):
        top_left = self._get_pixel_value(pixels, line - 1, column - 1)
        top_up = self._get_pixel_value(pixels, line - 1, column)
        top_right = self._get_pixel_value(pixels, line - 1, column + 1)
        right = self._get_pixel_value(pixels, line, column + 1)
        left = self._get_pixel_value(pixels, line, column - 1)
        bottom_left = self._get_pixel_value(pixels, line + 1, column - 1)
        bottom_down = self._get_pixel_value(pixels, line + 1, column)
        bottom_right = self._get_pixel_value(pixels, line + 1, column + 1)

        positions = [top_left, top_up, top_right, left, right, bottom_left, bottom_down, bottom_right]

        return positions

    def _thresholded(self, center, neighbours):
        # we compare grey level value of pixel[x,y] (center) with values of its neighbours
        result = []
        for neighbour in neighbours:
            if neighbour >= center:
                result.append(1)
            else:
                result.append(0)
        return result

    def _get_pixel_value(self, pixel, line, column):
        # if the index does not exist return 0
        # Workaround to create a 'border'
        try:
            return pixel[line, column]
        except IndexError:
            return 0

if __name__ == "__main__":
    input_file1 = "./Python_basic_Tutorial/LBP/LeNa_color.png"
    input_file2 = "./Python_basic_Tutorial/LBP/Lena_grayscale.jpg"
    # if os.path.isfile(input_file):

        # run = LBP(input_file)
        # print("RUNNING algorithm developed")
        # run.execute()
    # print("RUNNING scikit-image")
    # run.compare()
    # else:
    #     print("File '{}' does not exist.".format(input_file))
    run1 = LBP(input_file1)
    print("RUNNING1 algorithm developed")
    run1.execute()
    run2 = LBP(input_file2)
    print("RUNNING2 algorithm developed")
    run2.execute()