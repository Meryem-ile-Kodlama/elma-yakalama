import pygame
import random

# PENCERE 
pygame.init()
saat = pygame.time.Clock()
genislik = 800
yukseklik = 600
pencere = pygame.display.set_mode((genislik,yukseklik))
pygame.display.set_caption("Elma Yakalama Oyunu :)")

# RENKLER
arkaplanrengi = (180,225,255)
yazirengi = (20,100,170)

# SEPET
sepet_resim = pygame.image.load("sepet.png")
sepet = sepet_resim.get_rect(center = (genislik/2, yukseklik-64))
sepet_hiz = 0

# ELMA
elma_resim = pygame.image.load("elma.png")
elma = []
elma_hiz = []
elma_sayisi = 3
for i in range(elma_sayisi):
    elma.append(elma_resim.get_rect(center = (random.randint(32,genislik-32), random.randint(-800,-32))))
    elma_hiz.append(7)

# SKOR-CAN
skor = 0
can = 3
font = pygame.font.Font(None, 50)

# OYUN DÖNGÜSÜ
oyun = True
while oyun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sepet_hiz -= 20
            if event.key == pygame.K_RIGHT:
                sepet_hiz += 20
        if event.type == pygame.KEYUP:
            sepet_hiz = 0

    # SEPET HAREKETİ 
    sepet.x += sepet_hiz
    if sepet.left <= 0:
        sepet.left = 0
    elif sepet.right >= genislik:
        sepet.right = genislik

    # ELMA HAREKETİ 
    for i in range(elma_sayisi):
        elma[i].y += elma_hiz[i]
        if elma[i].top >= yukseklik:
            can -= 1
            elma[i].x = random.randint(32,genislik-32)
            elma[i].y = random.randint(-800,-32)

    # ELMA-SEPET ETKİLEŞİMİ
    for i in range(elma_sayisi):
        if elma[i].colliderect(sepet):
            skor += 1
            elma[i].x = random.randint(32,genislik-32)
            elma[i].y = random.randint(-800,-32)

    # CANLAR BİTİNCE
    if can <= 0:
        oyun = False

    # EKRANA ÇİZME
    skorcan_yazisi = font.render("Skor: {} | Can: {}".format(skor,can),True,yazirengi) 

    pencere.fill(arkaplanrengi)

    for i in range(elma_sayisi):
        pencere.blit(elma_resim,elma[i])

    pencere.blit(sepet_resim,sepet)
    pencere.blit(skorcan_yazisi, (25,25))

    # PENCEREYİ GÜNCELLEME
    saat.tick(60)
    pygame.display.update()

pygame.quit()