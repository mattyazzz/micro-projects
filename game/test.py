import pygame

pygame.init ()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("test")

corriendo = True
color_fondo = (30, 30, 30)  # gris oscuro
color_cuadro = (113, 0, 251)  # morado

#variables

x = 100
y = 100
velocidad = 2

# límites horizontales
if x < 0:
    x = 0
if x > 800 - 100:
    x = 800 - 100

# límites verticales
if y < 0:
    y = 0
if y > 600 - 100:
    y = 600 - 100

jugador = pygame.Rect(x, y, 100, 100)
caja = pygame.Rect(300, 200, 100, 100)
meta = pygame.Rect(600, 400, 100, 100)

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # movimiento
    teclas = pygame.key.get_pressed()

    #contador the gref

    tiempo_inicio = None
    tiempo_transcurrido = 0

       
    # derecha
    if teclas[pygame.K_d]:
        jugador.x += velocidad
        if jugador.colliderect(caja):
            caja.x += velocidad
        
            if caja.right > 800:
                caja.right = 800
                jugador .x -= velocidad

    # izquierda
    if teclas[pygame.K_a]:
        jugador.x -= velocidad
        if jugador.colliderect(caja):
            caja.x -= velocidad

            if caja.left < 0:
                caja.left = 0
                jugador .x += velocidad

    # arriba
    if teclas[pygame.K_w]:
        jugador.y -= velocidad
        if jugador.colliderect(caja):
            caja.y -= velocidad

            if caja.top < 0:
                caja.top = 0
                jugador .y += velocidad

    # abajo
    if teclas[pygame.K_s]:
        jugador.y += velocidad
        if jugador.colliderect(caja):
            caja.y += velocidad

            if caja.bottom > 600:
                caja.bottom = 600
                jugador .y -= velocidad

    if jugador.left < 0:
        jugador.left = 0
    if jugador.right > 800:
        jugador.right = 800

    if jugador.top < 0:
        jugador.top = 0
    if jugador.bottom > 600:
        jugador.bottom = 600


    if caja.left < 0:
        caja.left = 0
    if caja.right > 800:
        caja.right = 800

    if caja.top < 0:
        caja.top = 0
    if caja.bottom > 600:
        caja.bottom = 600


    #ganar
    if caja.colliderect(meta):
        print("GANASTE 🎉")
        corriendo = False

    pantalla.fill((30, 30, 30))

    pygame.draw.rect(pantalla, (50, 150, 255), jugador)  # jugador
    pygame.draw.rect(pantalla, (200, 50, 50), caja)      # caja
    pygame.draw.rect(pantalla, (50, 200, 50), meta)      # meta

    pygame.display.flip()

pygame.quit()
