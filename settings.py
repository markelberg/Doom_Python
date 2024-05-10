import math


RES = WIDTH, HEIGHT = 1600, 900
FPS = 60

PLAYER_POS = 1.5, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

FOV = math.pi / 3  # nos proporciona un campo de visión de 60 grados.
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2  # cantidad de rayos para el raycasting.
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS  # conseguimos el ángulo de separación entre los rayos.
MAX_DEPTH = 20
