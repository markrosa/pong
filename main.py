import time
from machine import Pin, Timer
from lib.lcd_1inch14 import LCD_1inch14
from random import randint

DEBUG = False

# Pinout for Waveshare 1.14 LCD
RST_PIN = 12
DC_PIN = 8
CS_PIN = 18
BL_PIN = 9

#
#MOSI = 11
#SCK = 10

# Define screen dimensions
screen_width = 240
screen_height = 135

# Paddle positions
paddle1_pos = screen_height // 2
paddle2_pos = screen_height // 2

# Ball position and velocity
init_ball_pos_x = screen_width // 2
init_ball_pos_y = screen_height // 2
ball_pos = [init_ball_pos_x, init_ball_pos_y]
ball_vel = [1, 1]

# Score
score1 = 0
score2 = 0

# Create LCD object
lcd = LCD_1inch14()
# Clear screen
lcd.fill(lcd.black)

if DEBUG: print("INIT screen") # DEBUG


# Define paddle dimensions
paddle_width = 4
paddle_height = 16
paddle_offset = 1

# Define ball dimensions
ball_width = 3
ball_height = ball_width


keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)

key_up = Pin(2 ,Pin.IN,Pin.PULL_UP)
key_center = Pin(3 ,Pin.IN,Pin.PULL_UP)
key_left = Pin(16 ,Pin.IN,Pin.PULL_UP)
key_down = Pin(18 ,Pin.IN,Pin.PULL_UP)
key_right = Pin(20 ,Pin.IN,Pin.PULL_UP)


# Draw initial paddles and ball
lcd.fill_rect(0, paddle1_pos, paddle_width, paddle_height, lcd.white)
lcd.fill_rect(screen_width - paddle_width, paddle2_pos, paddle_width, paddle_height, lcd.white)
if DEBUG: print("BALL pos: ", ball_pos[0], ball_pos[1]) # DEBUG
lcd.fill_rect(ball_pos[0], ball_pos[1], ball_pos[0] + ball_width, ball_pos[1] + ball_height, lcd.white)

# Define update functions
def update_paddles():
    global paddle1_pos, paddle2_pos

    # Read paddle1 buttons
    if key_up.value() == 0:
        paddle1_pos = max(paddle1_pos - 1, 0)
    if key_down.value() == 0:
        paddle1_pos = min(paddle1_pos + 1, screen_height - paddle_height)

    # Read paddle2 buttons
    if keyA.value() == 0:
        paddle2_pos = max(paddle2_pos - 1, 0)
    if keyB.value() == 0:
        paddle2_pos = min(paddle2_pos + 1, screen_height - paddle_height)

    # Redraw paddles
    lcd.fill_rect(0, paddle1_pos, paddle_width, paddle_height, lcd.white)
    lcd.fill_rect(screen_width - paddle_width, paddle2_pos, paddle_width, paddle_height, lcd.white)

def update_ball():
    global ball_pos, ball_vel, score1, score2

    # Check for collision with top/bottom walls
    if ball_pos[1] - ball_height <= 0 or ball_pos[1] + ball_height >= screen_height:
        ball_vel[1] *= -1

    # Check for paddle collisions
    if ball_pos[0] - ball_width <= paddle_width and paddle1_pos <= ball_pos[1] <= paddle1_pos + paddle_height:
        ball_vel[0] *= -1
    elif ball_pos[0] + ball_width >= screen_width - paddle_width and paddle2_pos <= ball_pos[1] <= paddle2_pos + paddle_height:
        ball_vel[0] *= -1

    # Check for score
    if ball_pos[0] - ball_width <= 0:
        score2 += 1
        ball_pos = [init_ball_pos_x, init_ball_pos_y]
        ball_vel = [randint(1, 2), randint(1, 2)]
    elif ball_pos[0] + ball_width >= screen_width:
        score1 += 1
        ball_pos = [init_ball_pos_x, init_ball_pos_y]
        ball_vel = [-randint(1, 2), randint(1, 2)]

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # redraw ball
    lcd.fill_rect(ball_pos[0] - ball_width // 2, ball_pos[1] - ball_height // 2, ball_width, ball_height, lcd.white)


while True:
    # Clear screen
    lcd.fill(lcd.black)

    if DEBUG: print("keyA: ", keyA.value()) # DEBUG

    # Update paddles
    update_paddles()

    # Update ball
    update_ball()
    if DEBUG: print("BALL pos: ", ball_pos[0], ball_pos[1]) # DEBUG

    # Draw score
    lcd.text(str(score1), screen_width // 2 - 12, 0, lcd.white)
    lcd.text(str(score2), screen_width // 2 + 4, 0, lcd.white)

    # Show on display
    lcd.show()

    # Delay
    time.sleep(0.02)

