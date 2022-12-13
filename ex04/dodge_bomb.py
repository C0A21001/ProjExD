import pygame as pg
import sys
import random
import time

def check_bound(obj_rct,scr_rct):
    #第1引数は、こうかとんrectまたは爆弾rect
    #第２因数は、スクリーンの
    #範囲内:+1/範囲外/-1
    yoko,tate = +1,+1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        tate = -1
    return yoko,tate

def main():
    clock = pg.time.Clock()
    fonto = pg.font.Font(None,100)
    pg.display.set_caption("逃げろこうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,90,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 600,400
    #scrn_sfcにtori_rctに従って,tori_sfcを張り付ける

    bomb_sfc = pg.Surface((20,20)) #正方形の空のSurface
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_rct.centery = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(bomb_sfc,bomb_rct)

    vx,vy = +1,+1
    #時間を計測するための変数
    time = 0 
    game_txt = "geme over"
    txt1 = fonto.render(str(game_txt),True, (0,0,0))

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        #時間を計測し、表示する
        txt = fonto.render(str(int(time)),True, (0,0,0))
        scrn_sfc.blit(txt, (1450,30))
        time += 0.01

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_dct[pg.K_BACKSPACE]:
            return
        if check_bound(tori_rct, scrn_rct) != (+1,+1):
            #どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)
        
        bomb_rct.move_ip(vx,vy)
        yoko,tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= tate
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        if time > 20 and (-４ < vx < 4) and (-4 < vy < 4):
            vx *= 1.01
            vy *= 1.01
        if tori_rct.colliderect(bomb_rct):
            pass
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()