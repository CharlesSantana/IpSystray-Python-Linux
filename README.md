# Script em Python para verificar ip de rede local para maquina com sistema operacional linux

Caso o script nao rode em sua maquina, favor instalar os complementos e bibliotecas abaixo.
# Pip
sudo apt install python-pip

# Pil
Instale para que a bliblioteca de imagem possa ser importada
sudo apt-get install python3-pil python3-pil.imagetk

# Biblioteca Image
Biblioteca para criacao da imagem no systray
pip install image

# Biblioteca socket
Esta biblioteca cria e checa a conexao
pip install socket

# Biblioteca Pystray
pip install pystray
Esta biblioteca facilita a usar o script como um icone no systray



# Faça uma pequena alteração
Onde se le image=Image.open("/home/USUARIO/ipsystray/ip.png"), na linha 53 deste manual, mude o nome USUARIO pelo usuario de seu sistema.


# O CODIGO
O codigo abaixo faz toda a magica, dê uma estudada e modifique como vc quiser, deixe os comentarios dando creditos ao seu amigo Charles Santana, que tive que estudar para deixar funcinando para que vc tambem use. 

#====COPIE O SCRIPT APARTIR DAQUI==============================

# Script Para checar ip Local
# Autor = Charles Santana - 31/10/2023
# Modificado por = Coloque seu nome aqui e data
# Gostou? Ajude com o valor de um cafezinho - 
# Chave Pix Aleatoria - 7055e7e8-0794-4627-ae98-3e8ba22457ae


import pystray
import socket
from PIL import Image, ImageDraw

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(f"IP DA MAQUINA É : " + s.getsockname()[0])



def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image=Image.open("/home/USUARIO/ipsystray/ip.png")
   

    return image

title=(f"IP DA MAQUINA É : " + s.getsockname()[0])
# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon(f"IP DA MAQUINA É : " + s.getsockname()[0],
    icon=create_image(64, 64, 'black', 'white'),title=(f"IP DA MAQUINA É : " + s.getsockname()[0]))


# To finally show you icon, call run

icon.run()
icon.mainloop()



