import matplotlib.pyplot as plt
import numpy as np

# definir as core da pintura
blue = '#034694'
yellow = '#FDB913'
white = '#FFFFFF'
black = '#000000'
light_blue = '#7BC8F6'

# define a imagem de fundo
fig = plt.figure(facecolor='black')

# define o tamanho da figura
fig.set_size_inches(10,8)

# define o eixo x e y
ax = plt.axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# cria uma lista de circulos 
stars = [plt.Circle((np.random.uniform(), np.random.uniform()), 0.005, color=white) for i in range(500)]

# adicionar os circulos ao eixo
for s in stars:
    ax.add_artist(s)

# desenhar a lua
moon = plt.Circle((0.75, 0.8), 0.1, color=light_blue) 
ax.add_artist(moon)

# Desenha o cipreste
tree = plt.Rectangle((0.05, 0.1), 0.1, 0.4, color=black)
ax.add_artist(tree)

# Cria uma lista de pontos para desenhar a curva
x = np.linspace(0, 1, 1000)
y = 0.5 + 0.3 * np.sin(4 * np.pi * x)

# Desenha a curva com a cor azul escura
line, = ax.plot(x, y, color=blue, lw=2)

# Adiciona algumas nuvens amarelas
cloud1 = plt.Circle((0.2, 0.7), 0.1, color=yellow)
cloud2 = plt.Circle((0.4, 0.6), 0.1, color=yellow)
cloud3 = plt.Circle((0.6, 0.75), 0.1, color=yellow)
ax.add_artist(cloud1)
ax.add_artist(cloud2)
ax.add_artist(cloud3)

# Exibe a imagem
plt.show()