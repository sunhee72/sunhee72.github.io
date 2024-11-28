import pygame as pg
import sys
import random

pg.init()
screen = pg.display.set_mode((900, 400))

r1 = pg.Rect(50, 50, 50, 50)
r2 = pg.Rect(200, 50, 50, 50)

bg = pg.image.load("images/bg_cloud.png")
rr = pg.image.load("images/cloud_rabbit.svg")
potion = pg.image.load("images/potion.png")
fire = pg.image.load("images/fire.png")
mob = pg.image.load("images/dragon.svg")  # 몹 이미지 불러오기
win = pg.image.load("images/win.png")  # 상장 이미지 불러오기

x = random.randint(500, 650)  # 몹의 x축 등장 위치를 500~650에서 랜덤하게 결정
y = random.randint(0, 50)  # 몹의 y축 등장 위치를 0~50에서 랜덤하게 결정
r4 = pg.Rect(x, y, 50, 50)  # 몹의 이미지를 표시할 사각형 만들기

magic = False
fire_on = False


def move(r):  # r은 사각형
    if key[pg.K_RIGHT]:
        r.x = r.x + 0.5
    if key[pg.K_LEFT]:
        r.x = r.x - 0.5
    if key[pg.K_UP]:
        r.y = r.y - 0.5
    if key[pg.K_DOWN]:
        r.y = r.y + 0.5


pg.mixer.Sound("sounds/powerup.wav").play()  # 등장 음악 재생

while True:
    screen.blit(bg, (0, 0))
    key = pg.key.get_pressed()
    move(r1)
    screen.blit(rr, r1)

    if magic == True and r3.colliderect(r4):  # 불꽃 마법 얻은 후 몹과 충돌
        screen.blit(win, r4)  # 상장 이미지 그려주기
        pg.mixer.Sound("sounds/stage_clear.wav").play()  # 승리 음악 재생
        pg.display.update()  # 화면 업데이트
        pg.time.delay(5500)  # 5.5초 동안 기다리기
        pg.quit()  # 파이게임 종료
        sys.exit()  # 프로그램 종료

    screen.blit(mob, r4)  # 몹 이미지를 화면에 그리기
    r4.x = r4.x - 0.5  # 몹의 위치를 왼쪽으로 0.5만큼 이동시키기

    if magic == False:
        screen.blit(potion, r2)
        if r1.colliderect(r2):
            magic = True
            r3 = pg.Rect(
                r1.x + 65, r1.y + 25, 50, 50
            )  # 불꽃 이미지를 위한 사각형 만들기
            pg.mixer.Sound("sounds/powerup2.wav").play()  # 불꽃 마법 획득 음악 재생
    else:
        if key[pg.K_SPACE]:
            fire_on = True
            pg.mixer.Sound("sounds/fire.wav").play()  # 불꽃 발사 음악 재생
            screen.blit(fire, r3)

            if fire_on:
                r3.x = r3.x + 1
            else:
                move(r3)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
