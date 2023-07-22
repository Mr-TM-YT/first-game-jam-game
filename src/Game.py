# necessary imports
import pygame as pg
from sys import exit
from Settings import *
from Enemy import Enemy


class Game:
    #  init method
    def __init__(self) -> None:
        pg.init()
        self.display = pg.display.set_mode(
            (WINDOW_SIZE["x"], WINDOW_SIZE["y"]))
        self.running = True
        self.clock = pg.time.Clock()
        pg.display.set_caption("The (Team Name) is here baby")
        self.keys = pg.key.get_pressed()
        self.enemy = Enemy(self.display)
        # Initial x position of the square
        self.square_x = WINDOW_SIZE["x"] // 2
        # Initial y position of the square
        self.square_y = WINDOW_SIZE["y"] // 2

    # checks if the game is running
    def is_running(self) -> bool:
        return self.running

    # update the game
    def update(self) -> None:
        self.check_events()
        self.enemy.update()

    # draw stff on the screen
    def render(self) -> None:
        self.display.fill((0, 0, 255))
        pg.draw.rect(self.display, square_color, (self.square_x,
                                                  self.square_y, square_size, square_size))
        self.enemy.render()
        pg.display.flip()
        self.clock.tick(60)

    # check for events
    def check_events(self) -> None:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

        # Update keys state on each iteration
        self.keys = pg.key.get_pressed()

        # Now use self.square_x and self.square_y to update the position
        # The other condition is for clamping the square inside the window
        if (self.keys[pg.K_LEFT] or self.keys[pg.K_a]) and self.square_x >= 0:
            self.square_x -= movement_speed

        if (self.keys[pg.K_RIGHT] or self.keys[pg.K_d]) and self.square_x <= WINDOW_SIZE["x"] - square_size:
            self.square_x += movement_speed

        if (self.keys[pg.K_UP] or self.keys[pg.K_w]) and self.square_y >= 0:
            self.square_y -= movement_speed

        if (self.keys[pg.K_DOWN] or self.keys[pg.K_s]) and self.square_y <= WINDOW_SIZE["y"] - square_size:
            self.square_y += movement_speed
    # close the game and cleanup

    def close(self):
        pg.quit()
        exit()
