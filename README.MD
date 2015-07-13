
## Resumo:
Dada a imagem de uma mão executando uma jogada do jokenpo o programa classifica-a. 

## Dependências

### Linux
- kubuntu trusty 14.04.2 TLS
- Python 2.7.6 
- scikit-image
- Opencv 2.7

### Windows

- Instale o [Anaconda](http://continuum.io/downloads) que contém todas depenência, inclusive o Python. Basta fazer o download do arquivo .exe e executa-lo.


## Como instalar o OpenCV

### Linux
  Seguir as instruções disponíveis em [OpenCV-Linux](http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html#linux-installation). Lí em algum lugar que dá para instalar com o comando abaixo, não testei mas pode funcionar:
  ```
  $ sudo apt-get install python-opencv
  ```

### Windows
 - [OpenCV-Python](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows).
	1. Baixe o [Opencv](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows)
	2. Extraia os arquivos no local desejado.
	3. Vá para a pasta opencv/build/python/2.7.
	4. Cipie o arquivo cv2.pyd para C:/Python27/lib/site-packeges.
	5. Abra o terminal e digite python para executar o interpretador.
	6. Digite:
    	
      ```
        >>> import cv2
        >>> print cv2.__version__
      ```
    Pronto!




## Como instalar scikit-image e arff
```
  $ sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose python-pip python-networkx 
  $ sudo pip install -U scikit-image
```

  Em uma das máquinas em que tentei instalar deu um erro que resolvi rodando o comando abaixo antes de executar a linha acima:
  ```
  $ sudo apt-get build-dep python-matplotlib
  ```
