import random
import pygame
#o primeiro erro que vi foi que não tinha a linha de código import pygame escrito. 
# isso foi facil de arrumar só escrever "import pygame" parece facil mas na real me senti hacker 


# Inicialização do Pygame
pygame.init()

# Definição das cores
COR_FUNDO = (0, 0, 0)
COR_COMIDA = (255, 0, 0)

# Dimensões da tela
largura_tela = 640
altura_tela = 480

# Tamanho da cobra e da comida
tamanho = 20

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Snake")

# Carregamento da imagem do Snake
snake_img = pygame.image.load("snake.png")
snake_img = pygame.transform.scale(snake_img, (tamanho, tamanho))

# Relógio para controle de atualizações
relogio = pygame.time.Clock()

# Função para gerar uma posição aleatória para a comida
def gerar_comida():
    x = random.randint(0, largura_tela - tamanho)
    y = random.randint(0, altura_tela - tamanho)
    return x // tamanho * tamanho, y // tamanho * tamanho

# Função principal do jogo
def jogo_snake():
    sair = False
    game_over = False

    # Posição inicial da cobra
    x_cobra = largura_tela // 2
    y_cobra = altura_tela // 2

    # Velocidade inicial da cobra
    velocidade_x = 0
    velocidade_y = 0

    # Geração da comida
    comida_x, comida_y = gerar_comida()

    # Lista para armazenar as partes da cobra
    cobra = []
    comprimento_inicial = 1

    while not sair:
        while game_over:
            # Tela de fim de jogo
            tela.fill(COR_FUNDO)
            fonte = pygame.font.Font(None, 36)
            mensagem = fonte.render("Fim de jogo! Pressione C para continuar ou Q para sair.", True, (255, 255, 255))
            tela.blit(mensagem, (largura_tela // 2 - mensagem.get_width() // 2, altura_tela // 2 - mensagem.get_height() // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo_snake()
                    elif event.key == pygame.K_q:
                        sair = True
                        game_over = False
                elif event.type == pygame.QUIT:
                    sair = True
                    game_over = False

        # Movimentação da cobra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_x = -tamanho
                    velocidade_y = 0
                elif event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_x = tamanho
                    velocidade_y = 0
                elif event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                elif event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

        # Atualização da posição da cobra
        x_cobra += velocidade_x
        y_cobra += velocidade_y

        # Verificação de colisões
        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            game_over = True
        if (x_cobra, y_cobra) in cobra[1:]:
            game_over = True

        # Criação do fundo
        tela.fill(COR_FUNDO)

        # Desenho da comida
        pygame.draw.rect(tela, COR_COMIDA, (comida_x, comida_y, tamanho, tamanho))

        # Atualização da posição da cobra
        cobra.append((x_cobra, y_cobra))
        if len(cobra) > comprimento_inicial:
            del cobra[0]

        # Desenho da cobra
        for parte in cobra:
            tela.blit(snake_img, (parte[0], parte[1]))

        pygame.display.update()

        # Verificação de colisão com a comida
        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x, comida_y = gerar_comida()
            comprimento_inicial += 1

        relogio.tick(10)

    pygame.quit()

# Execução do jogo
jogo_snake()