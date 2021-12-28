'''
	author: Jackson Antonio do Prado Lima <jacksonpradolima at gmail dot com>

	Objective: Implement the LBP algorithm seen in the classroom using any programming language.
	The algorithm should receive as input any image and return the LBP image and also the
	256-position histogram with the distribution of the LBP codes.

	This class is a main to separate the algorithm logic from my main
	In the case I developed future LBP algorithms, like circular :D
'''
import argparse
import os.path
import LBP
import time

def main():
    # # Tạo một biến là ap, có description là thông tin mô tả
    # ap = argparse.ArgumentParser(description='Run the local binary patterns algorithm using a basic 3x3.')
    # #Thêm vào các thuộc tính cho ap
    # ap.add_argument('-i', '--input', dest='input', type=str, required=True,
    #                 help='file name with path of the input image')
    # #Biến các tham số được đưa ra ở trên thành một thuộc tính và trả về object đó
    # arguments = ap.parse_args()
    # # input_file = arguments.input  # 'data/simpsons/Test/bart116.jpg'
    # input_file = arguments.input
    input_file = "./Python_basic_Tutorial/LBP/LeNa_color.png"
    if os.path.isfile(input_file):

        run = LBP.LBP(input_file)
        print("RUNNING algorithm developed")
        run.execute()
        # print("RUNNING scikit-image")
        # run.compare()
    else:
        print("File '{}' does not exist.".format(input_file))


if __name__ == "__main__":
    start_time = time.time()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))