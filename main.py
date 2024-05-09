import pygame as pg 
import sys
from settings import *
from map import *
from player import *


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
    
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update_player()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw_map()
        self.player.draw_player()

    def run_game(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pg.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, event):
        pass


if __name__ == '__main__':
    game = Game()
    game.run_game()