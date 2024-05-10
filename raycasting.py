import pygame as pg
import numpy as np
from settings import *


class RayCasting:

    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos  # coordenadas del jugador en el mapa
        x_map, y_map = self.game.player.map_pos  # coordenadas del "tile/baldosa" en el que se encuentra el jugador

        ray_angles = np.linspace(self.game.player.angle - HALF_FOV, self.game.player.angle + HALF_FOV, NUM_RAYS)
        for ray_angle in ray_angles:  # calculamos el ángulo de cada rayo
            sin_a = np.sin(ray_angle)
            cos_a = np.cos(ray_angle)

            # HORIZONTAL 'LINES' LOGIC
            y_hor, dy = np.where(sin_a > 0, (y_map + 1, 1), (y_map - 0.000001, -1))

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)  # coordenadas del linea vertical del tile que cruza el rayo
                if tile_hor in self.game.map.world_map:  # comprobamos si las coordenadas de la línea vertical del tile está en el mapa
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # VERTICAL 'LINES' LOGIC
            x_vert, dx = np.where(cos_a > 0, (x_map + 1, 1), (x_map - 0.000001, -1))

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)  # coordenadas del linea vertical del tile que cruza el rayo
                if tile_vert in self.game.map.world_map:  # comprobamos si las coordenadas de la línea vertical del tile está en el mapa
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            depth = np.minimum(depth_hor, depth_vert)  # Elegimos el depth más pequeño (el que primero "choca") entre depth_vert y depth_hor

            pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy), (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)

    def update_rc(self):
        self.ray_cast()
