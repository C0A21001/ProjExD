import pygame as pg
import sys
import random
import time
class Screen:
    def __init__(self,title,wh,image_path):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(image_path)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)


class Bird:#w,s,a,dで移動
    key_delta = {
        pg.K_w:   [0,-1],
        pg.K_s: [0,+1],
        pg.K_a: [-1,0],
        pg.K_d:[+1,0],
    }

    def __init__(self,image,size,xy):
        self.tori_sfc = pg.image.load(image)
        self.tori_sfc = pg.transform.rotozoom(self.tori_sfc,0,size)
        self.tori_rct = self.tori_sfc.get_rect()
        self.tori_rct.center = xy
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.tori_sfc,self.tori_rct)

    def update(self,scr:Screen):
        key_dct = pg.key.get_pressed()
        for key,delta in Bird.key_delta.items():
            if key_dct[key]:
                self.tori_rct.centerx += delta[0]
                self.tori_rct.centery += delta[1]
            if check_bound(self.tori_rct,scr.rct) != (+1,+1):
                self.tori_rct.centerx -= delta[0]
                self.tori_rct.centery -= delta[1]
        self.blit(scr)

#敵キャラを表示
class Enemy:
    def __init__(self,image,size,xy):
        self.enmy_sfc = pg.image.load(image)
        self.enmy_sfc = pg.transform.rotozoom(self.enmy_sfc,0,size)
        self.enmy_rct = self.enmy_sfc.get_rect()
        self.enmy_rct.center = xy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.enmy_sfc,self.enmy_rct)



class Bomb:
    def __init__(self,color,r,vxy,scr:Screen):
        self.bomb_sfc = pg.Surface((2*r,2*r)) #正方形の空のSurface
        self.bomb_sfc.set_colorkey((0,0,0))
        pg.draw.circle(self.bomb_sfc,color,(r,r),r)
        self.bomb_rct = self.bomb_sfc.get_rect()
        self.bomb_rct.centerx = random.randint(0,scr.rct.width)
        self.bomb_rct.centery = random.randint(0,scr.rct.height)
        self.vx , self.vy = vxy
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.bomb_sfc,self.bomb_rct)
    
    def update(self,scr:Screen):
        self.bomb_rct.move_ip(self.vx,self.vy)
        yoko,tate = check_bound(self.bomb_rct,scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
       
    
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
    scr = Screen("負けるな！こうかとん",(1600,900),"fig/pg_bg.jpg")
    tori = Bird("fig/6.png",2.0,(900,400))
    tori.update(scr)
    enmys = []
    for i in range(5):
        sx = random.randint(100,1400)
        sy = random.randint(100,800)
        enmy = Enemy("fig/slime.png",0.1,(sx,sy))
        enmys.append(enmy)
    bombs = []
    for i in range(5):
            vx = random.choice([-1,+1])
            vy = random.choice([-1,+1])
            r  = random.randint(10,50)
            bombs.append(Bomb((255,0,0),r,(vx,vy),scr)) 
    

    #時間を計測するbための変数
    time = 0 
    #HPを表す変数
    life = 1000
    
    while True:
        scr.blit()
        #時間を計測し、表示する
        txt = fonto.render(str(int(time)),True, (0,0,0))
        scr.sfc.blit(txt, (1450,30))
        time += 0.01
        if time == 10:
            life += 100

        #HPを表示する
        txt1 = fonto.render("HP:"+str(int(life)),True, (0,0,0))
        scr.sfc.blit(txt1, (100,30))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        tori.update(scr)
        for enmy in enmys:
            enmy.blit(scr)
        
        #爆弾を複数個設置
        for bomb in bombs:
            bomb.update(scr)
            if tori.tori_rct.colliderect(bomb.bomb_rct):
                life -= 1
                #HPが0になったら終了(0の表示が見えるようにするため-1未満とする)
                if life < -1:
                    return
                    
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()