import cv2

# vídeo é uma sequência de imagens, chamadas quadros 
# cada quadro é formado por pixels, e em imagens coloridas, por canais de cor
# o fps que são os quadros por segundo determinam a taxa em que esses quadros são exibidos

cap = cv2.VideoCapture("video_exemplo.mp4")  # abre o vídeo pelo caminho do arquivo

if not cap.isOpened():  # verifica se o vídeo foi aberto corretamente
    print("Erro: não foi possível abrir o vídeo.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)  # obtém a taxa de quadros por segundo
quadros = []  # lista para guardar os quadros lidos

while True:
    ret, quadro = cap.read()  # Se a leitura funcionou o quadro é a imagem lida

    if not ret:  # não tem mais quadros para ler
        break

    quadros.append(quadro)  # adiciona o quadro à lista

cap.release()  # libera o arquivo de vídeo

total_lidos = len(quadros)  # conta quantos quadros foram  lidos

print("FPS:", fps)
print("Total de quadros:", total_lidos)

if total_lidos > 0:
    indice_meio = total_lidos // 2  # divisão inteira para obter o índice centraldo quadro

    cv2.imwrite(
        "frame_meio.jpg",  # arquivo de saída
        quadros[indice_meio],  # quadro do meio da sequência
    )

    print(
        "Quadro do meio salvo como frame_meio.jpg"
    )
else:
    print("Nenhum quadro foi encontrado.")