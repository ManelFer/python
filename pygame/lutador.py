import pygame


class Lutador():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 120, 180))
        self.y = y
        self.saude = 100
        self.img_index = 0
        self.atc_index = 0


    def desenhar(self, tela, lutador, oponente, lut_dic, som):
        velocidade = 10

        lutador_img = lut_dic['idle'][self.img_index]
        self.img_index += 1
        if self.img_index >= len(lut_dic['idle']):
            self.img_index = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a] and lutador == 1 or key[pygame.K_LEFT] and lutador == 2:
            if self.img_index >= len(lut_dic['run']):
                self.img_index = 0
            lutador_img = lut_dic['run'][self.img_index]
            self.rect.x -= velocidade
            if self.rect.left < 0:
                self.rect.x = 0
        if key[pygame.K_d] and lutador == 1 or key[pygame.K_RIGHT] and lutador == 2:
            if self.img_index >= len(lut_dic['run']):
                self.img_index = 0
            lutador_img = lut_dic['run'][self.img_index]
            self.rect.x +=  velocidade
            if self.rect.right >= tela.get_width():
                self.rect.x = tela.get_width() - 90


        if self.y != self.rect.y:
            self.rect.y += 6
            if self.y - self.rect.y > 25:
                if self.img_index >= len(lut_dic['jump']):
                    self.img_index = 0
                lutador_img = lut_dic['jump'][self.img_index]


        if ((key[pygame.K_w] and lutador == 1) or (key[pygame.K_UP] and lutador == 2)) and self.rect.top > 0:
            self.img_index = 0
            lutador_img = lut_dic['jump'][self.img_index]
            self.rect.y -= 30


        if self.atc_index != 0:
            if self.atc_index < len(lut_dic['attack']):
                lutador_img = lut_dic['attack'][self.atc_index]
                self.atc_index += 1
            else:
                self.atc_index = 0

        if ((key[pygame.K_SPACE] and lutador == 1) or (key[pygame.K_DOWN] and lutador == 2)) and self.atc_index == 0:
            som.play()
            lutador_img = lut_dic['attack'][self.atc_index]
            self.atc_index = 1

            if self.rect.centerx < oponente.rect.centerx:
                ataque = pygame.Rect((self.rect.right, self.rect.y, 80, 180))
            else:
                ataque = pygame.Rect((self.rect.left-80, self.rect.y, 80, 180))

            if ataque.colliderect(oponente.rect) and oponente.atc_index == 0:
                oponente.saude -= 10


        if self.rect.centerx > oponente.rect.centerx:
            lutador_img = pygame.transform.flip(lutador_img, True, False)
        if lutador == 1:
            tela.blit(lutador_img, (self.rect.x - 190, self.rect.y - 148))
        else:
            tela.blit(lutador_img, (self.rect.x - 190, self.rect.y - 164))