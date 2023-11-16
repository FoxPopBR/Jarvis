import pygame
import sys
import random

# Inicializa o pygame
pygame.init()

# Constantes para o jogo
LARGURA, ALTURA = 1280, 720
TAMANHO_SLOT = 150
LINHA_COR = (200, 200, 200)
BG_COR = (28, 170, 156)
CIRCULO_COR = (0, 0, 0)
X_COR = (255, 0, 0)
LINHA_LARGURA = 10
CIRCULO_LARGURA = 15
X_LARGURA = 25
RAIO = TAMANHO_SLOT // 3
MARGEM_SUPERIOR = 100
MARGEM_LATERAL = 150

# Calcula as margens para centralizar a grade
MARGEM_X = MARGEM_LATERAL + (LARGURA - MARGEM_LATERAL * 2 - (TAMANHO_SLOT * 3)) // 2
MARGEM_Y = MARGEM_SUPERIOR + (ALTURA - MARGEM_SUPERIOR - (TAMANHO_SLOT * 3)) // 2

# Configura a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Velha')
tela.fill(BG_COR)

# Tabuleiro do jogo (3x3)
tabuleiro = [[None] * 3 for _ in range(3)]

# Placar
placar = {'Usuário': 0, 'Computador': 0}

# Classe para gerenciar os menus
class Menu:
    def __init__(self, x, y, largura, altura, opcoes):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.opcoes = opcoes
        self.fonte = pygame.font.Font(None, 32)
        self.placar_fonte = pygame.font.Font(None, 40)
        self.mensagem_inicial = ""

    def desenhar(self):
        pygame.draw.rect(tela, (50, 50, 50), (self.x, self.y, self.largura, self.altura))
        for i, opcao in enumerate(self.opcoes):
            texto = self.fonte.render(opcao, True, (255, 255, 255))
            tela.blit(texto, (self.x + 10, self.y + 10 + i * 40))
        # Desenha o placar dentro do menu lateral esquerdo
        placar_texto_usuario = self.placar_fonte.render(f"Usuário: {placar['Usuário']}", True, (255, 255, 255))
        placar_texto_computador = self.placar_fonte.render(f"Computador: {placar['Computador']}", True, (255, 255, 255))
        tela.blit(placar_texto_usuario, (self.x + 10, self.y + 100))
        tela.blit(placar_texto_computador, (self.x + 10, self.y + 140))
        # Desenha a mensagem inicial no menu superior
        if self.mensagem_inicial:
            mensagem_texto = self.fonte.render(self.mensagem_inicial, True, (255, 255, 255))
            tela.blit(mensagem_texto, (self.x + 10, self.y + 10))

# Instancia os menus
menu_superior = Menu(0, 0, LARGURA, MARGEM_SUPERIOR, [""])
menu_esquerdo = Menu(0, MARGEM_SUPERIOR, MARGEM_LATERAL, ALTURA - MARGEM_SUPERIOR, ["Jogar", "Sair"])
menu_direito = Menu(LARGURA - MARGEM_LATERAL, MARGEM_SUPERIOR, MARGEM_LATERAL, ALTURA - MARGEM_SUPERIOR, ["Informações Futuras"])

# Funções para desenhar os elementos do jogo
def desenhar_menus():
    menu_superior.desenhar()
    menu_esquerdo.desenhar()
    menu_direito.desenhar()

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for x in range(1, 3):
        pygame.draw.line(tela, LINHA_COR, (MARGEM_X + x * TAMANHO_SLOT, MARGEM_Y), (MARGEM_X + x * TAMANHO_SLOT, MARGEM_Y + TAMANHO_SLOT * 3), LINHA_LARGURA)
        pygame.draw.line(tela, LINHA_COR, (MARGEM_X, MARGEM_Y + x * TAMANHO_SLOT), (MARGEM_X + TAMANHO_SLOT * 3, MARGEM_Y + x * TAMANHO_SLOT), LINHA_LARGURA)

# Função para desenhar as formas
def desenhar_formas():
    for linha in range(3):
        for coluna in range(3):
            centro_x = MARGEM_X + coluna * TAMANHO_SLOT + TAMANHO_SLOT // 2
            centro_y = MARGEM_Y + linha * TAMANHO_SLOT + TAMANHO_SLOT // 2
            if tabuleiro[linha][coluna] == "circulo":
                pygame.draw.circle(tela, CIRCULO_COR, (centro_x, centro_y), RAIO, CIRCULO_LARGURA)
            elif tabuleiro[linha][coluna] == "X":
                pygame.draw.line(tela, X_COR, (centro_x - RAIO, centro_y - RAIO), (centro_x + RAIO, centro_y + RAIO), X_LARGURA)
                pygame.draw.line(tela, X_COR, (centro_x + RAIO, centro_y - RAIO), (centro_x - RAIO, centro_y + RAIO), X_LARGURA)

# Função para verificar o vencedor
def verificar_vencedor():
    # Verifica linhas, colunas e diagonais para encontrar um vencedor
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] and tabuleiro[linha][0] is not None:
            return tabuleiro[linha][0]
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] is not None:
            return tabuleiro[0][coluna]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] is not None:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] is not None:
        return tabuleiro[0][2]
    return None

# Função para verificar se o tabuleiro está cheio
def verificar_empate():
    for linha in tabuleiro:
        if None in linha:
            return False
    return True

# Função para reiniciar o jogo
def reiniciar_jogo():
    global tabuleiro
    tabuleiro = [[None] * 3 for _ in range(3)]
    menu_superior.mensagem_inicial = ""

# Função para iniciar o jogo
def iniciar_jogo():
    # Escolhe aleatoriamente quem começa
    if random.choice([True, False]):
        menu_superior.mensagem_inicial = "Usuário começa"
    else:
        menu_superior.mensagem_inicial = "Computador começa"
    # Atualiza o menu superior para exibir a mensagem
    menu_superior.desenhar()
    pygame.display.update()
    # Aguarda 2 segundos antes de começar o jogo
    pygame.time.wait(2000)
    menu_superior.mensagem_inicial = ""
    # Inicia o jogo
    # Aqui você pode adicionar a lógica para o computador fazer sua jogada se ele começar

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Verifica se o clique foi no botão "Jogar"
            if menu_esquerdo.x < x < menu_esquerdo.x + menu_esquerdo.largura and menu_esquerdo.y < y < menu_esquerdo.y + 40:
                iniciar_jogo()

    # Desenha os elementos do jogo
    tela.fill(BG_COR)
    desenhar_menus()
    desenhar_tabuleiro()
    desenhar_formas()

    # Verifica se há um vencedor ou empate
    vencedor = verificar_vencedor()
    if vencedor:
        # Adiciona o ponto ao vencedor e reinicia o jogo
        placar[vencedor] += 1
        reiniciar_jogo()
    elif verificar_empate():
        reiniciar_jogo()

    pygame.display.update()
