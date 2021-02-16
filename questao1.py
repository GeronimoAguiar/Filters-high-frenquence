import argparse
import cv2
import os
import shutil

def process(input_data):
    try:
        os.makedirs('./imagens/questao1')
    except FileExistsError:
        shutil.rmtree('./imagens/questao1')
        os.makedirs('./imagens/questao1')

    for path, _,  file in os.walk(input_data):
        for img in file:
            imagem = cv2.imread(f"{path}/{img}", 0)
            
            sobelx = cv2.Sobel(imagem, cv2.CV_8U, 1, 0, ksize = 3)
            sobely = cv2.Sobel(imagem, cv2.CV_8U, 0, 1, ksize = 3)
            
            imgTratada = cv2.Laplacian(imagem, cv2.CV_8U)
            cv2.imwrite(f"./imagens/questao1/{img.split('.png')[0]}_sobelx.png", sobelx) 
            cv2.imwrite(f"./imagens/questao1/{img.split('.png')[0]}_sobely.png", sobely)
            cv2.imwrite(f"./imagens/questao1/{img.split('.png')[0]}_Laplacian.png", imgTratada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
   
    ap = argparse.ArgumentParser()

    ap.add_argument('-i', '--input',
                    default='default path',
                    help='Input folder path containing test images')
               
    args = vars(ap.parse_args())
    
    process(args['input'])

if __name__ == "__main__":
    main()