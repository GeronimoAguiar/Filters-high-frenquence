import cv2
import os

os.mkdir('./imagens/questao1')
for i in range(1, 7):
    i = str(i)
    arq = "imagens/img"+i+".png"
    imagem = cv2.imread(arq, 0)
    sobelx = cv2.Sobel(imagem, cv2.CV_8U, 1, 0, ksize = 3)
    sobely = cv2.Sobel(imagem, cv2.CV_8U, 0, 1, ksize = 3)
    imgTratada = cv2.Laplacian(imagem, cv2.CV_8U)

    cv2.imwrite("./imagens/questao1/img"+i+"sobelx.png", sobelx) 
    cv2.imwrite("./imagens/questao1/img"+i+"sobely.png", sobely)
    cv2.imwrite("./imagens/questao1/img"+i+"Laplacian.png", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()

