import cv2
import os

arq = "imagens/img2.png"
imagem = cv2.imread(arq, 0)
imgTratada1 = cv2.blur(imagem, (5,5))
imgTratada2 = cv2.GaussianBlur(imgTratada1, (5,5), 0)
cv2.imshow("imagem", imagem)
#cv2.imwrite("./imagens/imagens_tratadas/img"+i+".png", imgTratada2) 

cv2.waitKey(0)
cv2.destroyAllWindows()

