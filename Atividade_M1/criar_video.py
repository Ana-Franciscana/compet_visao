import cv2
import numpy as np

fps = 20
largura, altura = 320, 240

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

escritor = cv2.VideoWriter(
    "video_exemplo.mp4",
    fourcc,
    fps,
    (largura, altura),
)

n_quadros = 40

for i in range(n_quadros):
    quadro = np.zeros((altura, largura, 3), dtype=np.uint8)

    x = int(30 + (largura - 60) * i / n_quadros)

    cv2.circle(
        quadro,
        (x, altura // 2),
        20,
        (255, 0, 255),
        thickness=-1,
    )

    escritor.write(quadro)

escritor.release()

print("Vídeo criado com", n_quadros, "quadros.")