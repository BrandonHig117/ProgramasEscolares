import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Videojuego con pygame")

# Son los colores que usaremos para poder modificar nuestros objetos
WHITE = (255, 255, 255)
RED = (231, 76, 60)      
GREEN = (46, 204, 113)    
GRAY = (52, 73, 94)        
BLACK = (0, 0, 0)
BLUE = (55,118,171)

fuente = pygame.font.SysFont(None, 40)#el tipo de letra

# Variables del jugador (Círculo)
jugador_x = 100
jugador_y = 400
radio = 20                 # Tamaño de la pelota
jugador_vel_x = 5

# Física de salto y gravedad
jugador_vel_y = 0
gravedad = 0.5
fuerza_brinco = -12
en_suelo = False

# Meta (un cuadrado simple)
meta_rect = pygame.Rect(700, 360, 40, 90)
juego_ganado = False

reloj = pygame.time.Clock()

def reiniciar():
    global jugador_x, jugador_y, jugador_vel_y, en_suelo, juego_ganado
    jugador_x = 100
    jugador_y = 600
    jugador_vel_y = 0
    en_suelo = False
    juego_ganado = False

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Se crea una funcion donde se llama para volver a repetir cuando el usuario seleccione s
        if evento.type == pygame.KEYDOWN:
            # Si ganamos: S para reiniciar, N para salir
            if juego_ganado:
                if evento.key == pygame.K_s:
                    reiniciar()
                elif evento.key == pygame.K_n or evento.key == pygame.K_ESCAPE:#Al seleccionar n (no) se usa pygame.quit() que es donde cierra el juego
                    pygame.quit()
                    sys.exit()
            
            # Brincar con W (solo si estamos en el suelo y no hemos ganado)
            if not juego_ganado and evento.key == pygame.K_w and en_suelo:
                jugador_vel_y = fuerza_brinco
                en_suelo = False

    # Si no hemos ganado, el juego avanza
    if not juego_ganado:
        # Movimiento con A y D
        teclas = pygame.key.get_pressed() #Al usar pygame.key.get_pressed se refiere al teclado a que pieza fue seleccionada en este caso es a o d para mover izquierda o derecha
        if teclas[pygame.K_a]: #Si presiona a izquierda
            jugador_x -= jugador_vel_x
        if teclas[pygame.K_d]:#Si presiona d derecha
            jugador_x += jugador_vel_x

        # Aplicar gravedad
        jugador_vel_y += gravedad
        jugador_y += jugador_vel_y

        # Colisión con el suelo (Y = 450)
        suelo_y = 450
        if jugador_y + radio >= suelo_y:
            jugador_y = suelo_y - radio
            jugador_vel_y = 0
            en_suelo = True

        # Límites de la pantalla para que no se salga por los lados
        if jugador_x - radio < 0:
            jugador_x = radio
        elif jugador_x + radio > ANCHO:
            jugador_x = ANCHO - radio

        # El siguiente codigo es para detectar si la pelota toca la meta
        # Creamos una caja invisible alrededor del círculo para medir el choque fácil
        pelota_rect = pygame.Rect(jugador_x - radio, jugador_y - radio, radio * 2, radio * 2)
        if pelota_rect.colliderect(meta_rect):
            juego_ganado = True

    #Es para mostrar lo que salga en la ventanilla
    pantalla.fill(WHITE)

    # Dibujar suelo
    pygame.draw.rect(pantalla, RED, (0, 450, ANCHO, 150))

    # Dibujar meta
    pygame.draw.rect(pantalla, BLUE, meta_rect)

    # Dibujar jugador como CÍRCULO
    pygame.draw.circle(pantalla, GREEN, (int(jugador_x), int(jugador_y)), radio)

    # Si ganamos, mostrar mensaje en pantalla
    if juego_ganado:
        texto = fuente.render("¡Ganaste! ¿Otra vez? (S = Sí / N = No)", True, BLACK)
        pantalla.blit(texto, (ANCHO // 2 - 210, ALTO // 2 - 40))

    pygame.display.flip() #Este comando muestra en pantalla lo que acabamos de hacer los colores, textos y figura
    reloj.tick(60) #Se pone asi para que vaya fluido a 60fps