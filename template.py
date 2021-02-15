
import argparse
import cv2
import os


def process(input_data):
    # função que deve executar fluxograma principal do processo
    aux_function_A(input_data)
    aux_function_B()


def main():

    ap = argparse.ArgumentParser()

    ap.add_argument('-i', '--input',
                    default='default path',
                    help='Input folder path containing test images')
    ap.add_argument('-arg1', '--optional argument',
                    default='default argument',
                    help='info that help using this argument')

    args = vars(ap.parse_args())

    process(args['input'])


if __name__ == "__main__":
    main()