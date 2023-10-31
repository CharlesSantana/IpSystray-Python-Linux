#Script Para checar ip Local
#Autor = Charles Santana - 31/10/2023
#Modificado por = Coloque seu nome aqui e data
#Gostou? Ajude com o valor de um cafezinho - 
#Chave Pix Aleatoria - 7055e7e8-0794-4627-ae98-3e8ba22457ae

# Script em Python para verificar ip de rede local para maquina com sistema operacional linux

#Caso o script nao rode em sua maquina, favor instalar os complementos e bibliotecas abaixo.

# Pip
#sudo apt install python-pip

# Pil
#Instale para que a bliblioteca de imagem possa ser importada
#sudo apt-get install python3-pil python3-pil.imagetk

# Biblioteca Image
#Biblioteca para criacao da imagem no systray
#pip install image

# Biblioteca socket
#Esta biblioteca cria e checa a conexao
#ip install socket

# Biblioteca Pystray
#pip install pystray
#Esta biblioteca facilita a usar o script como um icone no systray



# Faça uma pequena alteração
#Onde se le image=Image.open("/home/master/ipsystray/ip.png"), na linha 53 deste manual, mude o nome MASTER pelo usuario de seu sistema.


import os
import pystray
import socket


from PIL import Image, ImageDraw

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(f"IP DA MAQUINA É : " + s.getsockname()[0])



def create_image(width, height, color1, color2):
    # Aqui é criada uma variavel para que possa ser apontada atravez da bliblioteca
    #  onde esta a imagem esta e possa ser usada como icone
    image=Image.open("/home/master/ipsystray/ip.png")
   

    return image
# Aqui é criada uma variavel que sera usada como titulo de nossa aplicacao,
# baseada na condicao de mostar o ip quando colocar o mouse no icone sem precisar clicar em cima dele

title=(f"IP DA MAQUINA É : " + s.getsockname()[0])

# Aqui montamos a variavel icone com base nas informaçoes assim o icone é criado e colocado no systray com dados importantes
# como o ip da maquina, criacao do icone com tamanho e caso imagem nao encontrada ele cria um icone com duas cores, e o titulo do 
# do icone com o mesmo nome da aplicacao
icon = pystray.Icon(f"IP DA MAQUINA É : " + s.getsockname()[0],
    icon=create_image(64, 64, 'black', 'white'),title=(f"IP DA MAQUINA É : " + s.getsockname()[0]))


# aqui neste comando iremos chamar a aplicacao e icone com o comando run 

icon.run()
