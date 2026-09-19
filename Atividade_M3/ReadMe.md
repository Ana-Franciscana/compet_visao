Frases explicando o conteudo do keypoint.json e sobre metadata e frames!

R: O metadata contém informações gerais da extração como o FPS, o número de quadros processados e as taxas de detecção das mãos e da poses
Os frames armazenam os dados de cada quadro do vídeo, incluindo informações sobre as mãos e as poses detectadas
Nos dados das mãos estão os landmarks, sendo 21 pontos por mão, com coordenadas x, y, z e score. E a taxa de detecção das mãos está registrada em metadata no campo hand_detection_rate