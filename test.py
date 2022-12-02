# test.py

import turtle

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ゲーム画面を初期化する
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# ゲーム画面を描画する
turtle.title("Tetris")
turtle.bgcolor("black")
turtle.tracer(0)

# ゲームを実行する
while True:
    turtle.update()