import argparse
import cv2

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--piece", required=True, help="Path to the input piece")

	args = vars(ap.parse_args())

	piece = cv2.imread(args["piece"])
	piece_gray = cv2.cvtColor(piece, cv2.COLOR_BGR2GRAY)
	_, piece_thresh =cv2.threshold(piece_gray, 180, 200, cv2.THRESH_BINARY_INV)
	#binarySegmented.convertTo(binarySegmented,CV_8UC1);
	colorContours = piece.copy();
	(_, cnts, _) = cv2.findContours(binarySegmented, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
