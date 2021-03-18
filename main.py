import pygame
import math
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Constant variables

BALL_IMAGE = pygame.image.load(os.path.join('assets', 'ball.png'))
BALL = pygame.transform.scale(BALL_IMAGE, (20, 20))
BALL2 = pygame.transform.scale(BALL_IMAGE, (20, 20))
time_elapsed = 0

# Colors

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Configuration
RADIUS = 5
ROUND_RATIO = 5
ball_x = 0
ball_y = HEIGHT
FPS = 60
h_max = 0
h_max_temp = 0
SCALE_X = 13
SCALE_Y = 20
g = 9.81

# Parameters

V0 = 20  # m/s
alpha = 45  # degrees

# Calculations
angle = math.radians(alpha)  # conversion from degrees to radians
Vx = V0 * math.cos(angle)
Vy = V0 * math.sin(angle)


def move_ball(tick):
    global ball_y, ball_x, time_elapsed, h_max, h_max_temp
    time = pygame.time.get_ticks()/1000

    if tick == 1:
        time = 0
    ball_y = HEIGHT - (Vy*time - (g/2 * time**2))*SCALE_Y - 20
    if HEIGHT - ball_y > h_max_temp:
        h_max_temp = HEIGHT - ball_y
        h_max = Vy*time - (g/2 * time**2)
    ball_x = Vx*SCALE_X*time
    if ball_y >= HEIGHT - 20 and tick != 1:
        time_elapsed = round(time, ROUND_RATIO)
        time_ref = round(2*Vy/g, ROUND_RATIO)
        distance = round(ball_x/SCALE_X, ROUND_RATIO)
        h_max = round(h_max, ROUND_RATIO)
        h_max_ref = round(Vy**2/2/g, ROUND_RATIO)
        distance_ref = round(Vx*time_elapsed, ROUND_RATIO)
        distance_error = ((abs(distance - distance_ref)) / distance_ref)*100
        h_max_error = ((abs(h_max-h_max_ref))/h_max_ref)*100
        time_error = (abs(time-time_ref)/time_ref)*100
        print("Time: " + str(time_elapsed) + "s")
        print("Time reference: " + str(time_ref) + "s")
        print("Distance: " + str(distance) + "m")
        print("Distance reference = " + str(distance_ref))
        print("Hmax: " + str(h_max) + "m")
        print("Hmax reference: " + str(h_max_ref))
        print("Hmax error: " + str(round(h_max_error, ROUND_RATIO)) + "%")
        print("Distance error: " + str(round(distance_error, ROUND_RATIO)) + "%")
        print("Time error: " + str(round(time_error, ROUND_RATIO)) + "%")
        return False
    else:
        return True


def draw_ball():
    WIN.fill(BLACK)
    WIN.blit(BALL, (ball_x, ball_y))
    pygame.display.update()


def main():
    tick = 1
    moving = True
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_ball()
        if moving:
            moving = move_ball(tick)
            if tick == 1:
                tick = 2
    pygame.quit()


if __name__ == "__main__":
    main()
