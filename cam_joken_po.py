# -*- coding: utf-8 -*-

__author__ = 'Ueliton'
import numpy as np
import cv2

"""
Joken po com a câmera.
Utiliza a câmera para determinar o movimento da mão feito pelo usuário com base na área da mão.

Modo de usar:
    Execute o código e e posicione a mão dentro do retângulo formado na imagem em cores.
    Faça o moviento desejado até o formato da mão aparecer na janela correspondendo ao desenho da mão.
    A classificação é feita com base nos limiares descritos no código.
    Movimente a mão para tráz e frente para melhorar os resultados. Como a classificação é baseada na área
    erros podem ocorrer devido aos diferentes tamanhos de mãos. Assim, movimentado a mão para frente e tráz
    reduz amenisa o impacto da diferença de tamanho.

    O programa funciona melhor com as luzes do ambientes apagadas facilitando a remoção do fundo e diminuindo os
    ruídos da imagem.

"""


#Limiares utilizados para detectar pele.
MIN_H = 28
MAX_H = 154

MIN_S = 59
MAX_S = 149

MIN_V = 139
MAX_V = 89

#Limiares máximos e mínimos para detecção de peles.
min_amarelo = np.array([MIN_H,MIN_S,MIN_V])
max_amarelo = np.array([MAX_H,MAX_S,MAX_V])


if __name__ == '__main__':

    #Camera.
    camera = cv2.VideoCapture(0)

    #Imagens utilizadas na classificação.
    pedra = cv2.imread("rock.png")
    papel = cv2.imread("paper.png")
    tesoura = cv2.imread("scissor.png")

    #Limites utilizados para obtenção dos limiares de área para a classificação.
    area_minima = float("inf")
    area_maxima = float("-inf")

    while(True):
        #Imagem da câmera
        _, quadro = camera.read()

        #Operacores com os frames
        #Imagem em preto e branco.
        imagem_cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)
        imagem_hsv = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV)

        #Ponto central da imagem. Utilizado para desenhar o retângulo na imagem.
        w = imagem_cinza.shape[1]   #largura
        h = imagem_cinza.shape[0]   #altura

        #Dimensões do retângulo.
        recH = 300
        recW = 200

        #Desenha o retângulo.
        rectangle = cv2.rectangle(quadro, (w/2-recW/2, h/2 -recH/2), (w/2+recW/2, h/2+recH/2), (0, 255, 0), 3)

        #Recorta o retângulo do quadro.
        imagem_cinza = imagem_cinza[h/2 -recH/2:h/2+recH/2, w/2-recW/2:w/2+recW/2]
        imagem_hsv = imagem_hsv[h/2 -recH/2:h/2+recH/2, w/2-recW/2:w/2+recW/2]

        #Remove ruidos com a gaussiana.
        imagem_borrada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
        #aplica um limiar (trasehold). Está usando um núcleo invertido para ser utilizado no escuro para remover o fundo com facilidade
        _, imagem_borrada_e_limiarizada = cv2.threshold(imagem_borrada, 70, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        #Segmenta a imagem utilizando um limiar para detectar a cor da pele
        # segmentada = cv2.inRange(imagem_hsv, min_amarelo, max_amarelo)

        #encontra os contornos da mão.
        _, contornos, _ = cv2.findContours(imagem_borrada_e_limiarizada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #encontra o contorno de maior area.
        controno_de_area_maxima = 0.0
        for i in range(len(contornos)):

                cnt = contornos[i]
                area = cv2.contourArea(cnt)
                if(area > controno_de_area_maxima):
                    controno_de_area_maxima = area
                    ci=i
        contorno_de_maior_area = contornos[ci]

        #Desenha os contornos.
        hull = cv2.convexHull(contorno_de_maior_area)
        epsilon = 0.01*cv2.arcLength(contorno_de_maior_area, True)
        approx = cv2.approxPolyDP(contorno_de_maior_area, epsilon, True)

        #Imagem utilizada para mostra o desenho da mão.
        desenho = np.zeros(quadro.shape, np.uint8)

        #Desenha o contorno.
        cv2.drawContours(desenho,[contorno_de_maior_area], 0, (0, 255, 0), 2)
        #Desenha a hull.
        cv2.drawContours(desenho,[hull], 0, (0, 0, 255), 2)

        #Obtém a área da hull.
        area = cv2.contourArea(cnt)

        # cv2.imshow("HSV", imagem_hsv)

        #Utilizado para determinar os valores máximos e mínimos de áreas utilizados no treinamento.
        if (area > area_maxima):
            area_maxima = area

        if (area < area_minima):
            area_minima = area

        print "Area: "+str(area_maxima)+", "+str(area_minima)

        #Comparações de áreas para definir o movimento
        if (area < 10000):
            quadro[0:100, 0:100] = pedra
        elif (area > 10000 and area < 14000):
            quadro[0:100, 0:100] = tesoura
        else:
            quadro[0:100, 0:100] = papel

        cv2.imshow("Original", quadro)
        cv2.imshow('Result', desenho)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera a câmera e destroi as janelas.
    camera.release()
    cv2.destroyAllWindows()
