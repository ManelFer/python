import pygame
from lutador import Lutador

pygame.mixer.init()
pygame.init()

largura = 1000
altura = 600

tela = pygame.display.set_mode((largura,altura))
clock = pygame.time.Clock()
FPS = 40

fundo = pygame.image.load("imagens/fundo/fundo.jpg")
pygame.mixer.music.load("audio/music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

som = pygame.mixer.Sound("audio/sword.wav")
som.set_volume(0.05)

fonte = pygame.font.SysFont('arial', 50)

marcial_lista = [pygame.image.load("imagens/marcial/Idle.png"),
                 pygame.image.load("imagens/marcial/Jump.png"),
                 pygame.image.load("imagens/marcial/Run.png"),
                 pygame.image.load("imagens/marcial/Attack2.png")]

marcial_dic = {'idle': [],
               'jump': [],
               'run': [],
               'attack': []
           }

medieval_lista = [pygame.image.load("imagens/medieval/Idle.png"),
                 pygame.image.load("imagens/medieval/Jump.png"),
                 pygame.image.load("imagens/medieval/Run.png"),
                 pygame.image.load("imagens/medieval/Attack3.png")]

medieval_dic = {'idle': [],
               'jump': [],
               'run': [],
               'attack': []
           }

def imagens(dic, lista):
    for x, tipo in enumerate(dic):
        img_l = lista[x].get_width()
        img_a = lista[x].get_height()
        for i in range(int(img_l / img_a)):
            img = lista[x].subsurface(i*img_a,0,img_a,img_a)
            dic[tipo].append(pygame.transform.scale(img, (img_a*4,img_a*4)))
    return(dic)

marcial = imagens(marcial_dic, marcial_lista)
medieval = imagens(medieval_dic, medieval_lista)


def desenhar_fundo():
    fundo_ajustado = pygame.transform.scale(fundo, (largura,altura))
    tela.blit(fundo_ajustado, (0,0))

def desenhar_saude(saude, x, y):
    taxa = saude / 100
    texto = fonte.render(str(saude), True, (255, 0, 0))
    tela.blit(texto, (x,y+30))
    pygame.draw.rect(tela, (255, 255, 255), (x-3, y-3, 406, 36))
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 400, 30))
    pygame.draw.rect(tela, (255, 255, 0), (x,y,400*taxa,30))


lutador_1 = Lutador(200,310)
lutador_2 = Lutador(700,310)

jogando = True
while jogando:
    clock.tick(FPS)
    desenhar_fundo()

    desenhar_saude(lutador_1.saude, 20, 20)
    desenhar_saude(lutador_2.saude, 580, 20)
    lutador_1.desenhar(tela, 1, lutador_2, marcial, som)
    lutador_2.desenhar(tela, 2, lutador_1, medieval, som )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    pygame.display.update()

pygame.quit()
