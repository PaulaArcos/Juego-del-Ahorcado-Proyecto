# Quito, agosto 2025, Daniela Arcos
# PDA - Juego del Ahorcado en Pygame
# Este programa permite jugar al clásico "Ahorcado" con categorías.
# Incluye selección de categoría, pistas automáticas, y gráficos del ahorcado.
# Controles:
#  - Presiona una letra para adivinar.
#  - ESPACIO: cambiar de categoría y reiniciar.
#  - R: reiniciar la misma categoría después de ganar o perder.
import pygame
import random
import time

pygame.init()

# =============================
# CONFIGURACIÓN INICIAL
# =============================
ANCHO, ALTO = 950, 650
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ahorcado con Historial")

BEIGE = (245, 245, 220)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
GRIS = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100)
VERDE = (0, 180, 0)

fuente = pygame.font.SysFont("Comic Sans MS", 30)

palabras = {
    "Cocina": ["Refrigeradora", "Horno", "Sartenes", "Microondas", "Tostadora", "Licuadora"],
    "Animales": ["Elefante", "León", "Tigre", "Jirafa", "Cocodrilo", "Hipopótamo"],
    "País": ["Ecuador", "México", "Canadá", "Argentina", "Brasil", "Colombia", "Chile", "España", "Japón", "Italia"],
    "Colores": ["Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Violeta", "Blanco", "Negro", "Rosa", "Gris"],
    "Deportes": ["Fútbol", "Baloncesto", "Tenis", "Natación", "Ciclismo", "Atletismo", "Vóley", "Boxeo", "Golf", "Béisbol"],
    "Instrumentos": ["Guitarra", "Piano", "Batería", "Violín", "Saxofón", "Flauta", "Trompeta", "Arpa", "Acordeón", "Clarinete"],
    "Frutas": ["Manzana", "Banana", "Naranja", "Pera", "Sandía", "Uva", "Melón", "Kiwi", "Mango", "Fresa"],
    "Verduras": ["Zanahoria", "Brócoli", "Lechuga", "Tomate", "Cebolla", "Pepino", "Espinaca", "Pimiento", "Coliflor", "Ajo"],
    "Profesiones": ["Doctor", "Ingeniero", "Profesor", "Carpintero", "Arquitecto", "Abogado", "Policía", "Enfermera", "Chef", "Mecánico"]
}

historial = []

# =============================
# FUNCIONES
# =============================
def reiniciar(cat):
    palabra = random.choice(palabras[cat]).upper()
    usadas = set()
    num_pistas = 1 if len(palabra) >= 5 else 2
    posiciones = random.sample(range(len(palabra)), num_pistas)
    for pos in posiciones:
        usadas.add(palabra[pos])
    return cat, palabra, usadas, 7, False, time.time()

def dibujar_ahorcado(superficie, intentos):
    base_x, base_y = 700, 400
    pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y), (base_x + 100, base_y), 5)
    pygame.draw.line(superficie, NEGRO, (base_x, base_y), (base_x, base_y - 300), 5)
    pygame.draw.line(superficie, NEGRO, (base_x, base_y - 300), (base_x - 100, base_y - 300), 5)
    pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 300), (base_x - 100, base_y - 250), 5)
    errores = 7 - intentos
    if errores >= 1:
        pygame.draw.circle(superficie, NEGRO, (base_x - 100, base_y - 220), 30, 3)
    if errores >= 2:
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 190), (base_x - 100, base_y - 120), 3)
    if errores >= 3:
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 180), (base_x - 130, base_y - 150), 3)
    if errores >= 4:
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 180), (base_x - 70, base_y - 150), 3)
    if errores >= 5:
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 120), (base_x - 130, base_y - 80), 3)
    if errores >= 6:
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 120), (base_x - 70, base_y - 80), 3)
    if errores >= 7:
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 250), (base_x - 100, base_y - 280), 3)

def elegir_categoria():
    categorias = list(palabras.keys())
    seleccion = None
    boton_volver = pygame.Rect(50, 500, 150, 50)
    while seleccion is None:
        ventana.fill(BEIGE)
        ventana.blit(fuente.render("Elige categoría:", True, NEGRO), (250, 50))
        for i, cat in enumerate(categorias):
            ventana.blit(fuente.render(f"{i+1}. {cat}", True, NEGRO), (300, 100 + i*50))

        mouse_pos = pygame.mouse.get_pos()
        color_volver = GRIS_OSCURO if boton_volver.collidepoint(mouse_pos) else GRIS
        pygame.draw.rect(ventana, color_volver, boton_volver)
        pygame.draw.rect(ventana, NEGRO, boton_volver, 2)
        ventana.blit(fuente.render("VOLVER", True, NEGRO), (boton_volver.x + 20, boton_volver.y + 10))

        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if boton_volver.collidepoint(e.pos):
                    return None
            if e.type == pygame.KEYDOWN and e.unicode.isdigit():
                num = int(e.unicode)
                if 1 <= num <= len(categorias):
                    seleccion = categorias[num - 1]
    return seleccion

def pantalla_historial():
    boton_volver = pygame.Rect(50, 500, 150, 50)
    while True:
        ventana.fill(BEIGE)
        ventana.blit(fuente.render("Historial de partidas:", True, NEGRO), (250, 50))
        for i, partida in enumerate(historial[-10:]):
            ventana.blit(fuente.render(
                f"{i+1}. {partida['categoria']}: {partida['palabra']} | {partida['resultado']} | +{int(partida['puntos'])} pts",
                True, NEGRO), (50, 120 + i*40))

        mouse_pos = pygame.mouse.get_pos()
        color_volver = GRIS_OSCURO if boton_volver.collidepoint(mouse_pos) else GRIS
        pygame.draw.rect(ventana, color_volver, boton_volver)
        pygame.draw.rect(ventana, NEGRO, boton_volver, 2)
        ventana.blit(fuente.render("VOLVER", True, NEGRO), (boton_volver.x + 20, boton_volver.y + 10))

        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if boton_volver.collidepoint(e.pos):
                    return

def pantalla_inicio():
    boton_iniciar = pygame.Rect(100, 200, 200, 50)
    boton_historial = pygame.Rect(100, 300, 200, 50)
    boton_salir = pygame.Rect(100, 400, 200, 50)
    while True:
        ventana.fill(BEIGE)
        ventana.blit(fuente.render("¡Bienvenido al Ahorcado!", True, NEGRO), (220, 100))
        dibujar_ahorcado(ventana, 0)

        mouse_pos = pygame.mouse.get_pos()
        color_iniciar = GRIS_OSCURO if boton_iniciar.collidepoint(mouse_pos) else GRIS
        color_historial = GRIS_OSCURO if boton_historial.collidepoint(mouse_pos) else GRIS
        color_salir = GRIS_OSCURO if boton_salir.collidepoint(mouse_pos) else GRIS

        pygame.draw.rect(ventana, color_iniciar, boton_iniciar)
        pygame.draw.rect(ventana, color_historial, boton_historial)
        pygame.draw.rect(ventana, color_salir, boton_salir)

        pygame.draw.rect(ventana, NEGRO, boton_iniciar, 2)
        pygame.draw.rect(ventana, NEGRO, boton_historial, 2)
        pygame.draw.rect(ventana, NEGRO, boton_salir, 2)

        ventana.blit(fuente.render("INICIAR", True, NEGRO), (boton_iniciar.x + 50, boton_iniciar.y + 10))
        ventana.blit(fuente.render("HISTORIAL", True, NEGRO), (boton_historial.x + 30, boton_historial.y + 10))
        ventana.blit(fuente.render("SALIR", True, NEGRO), (boton_salir.x + 60, boton_salir.y + 10))

        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if boton_iniciar.collidepoint(e.pos):
                    return
                elif boton_historial.collidepoint(e.pos):
                    pantalla_historial()
                elif boton_salir.collidepoint(e.pos):
                    pygame.quit()
                    exit()

# =============================
# FUNCION PRINCIPAL
# =============================
def main():
    puntos = 0
    pantalla_inicio()
    while True:
        cat = elegir_categoria()
        if cat is None:
            pantalla_inicio()
            continue

        cat, palabra, usadas, intentos, fin, inicio = reiniciar(cat)
        tiempo_limite = 30

        while True:
            ventana.fill(BEIGE)
            tiempo_restante = max(0, tiempo_limite - int(time.time() - inicio))
            volver_categorias = False

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        volver_categorias = True
                    elif not fin:
                        letra = pygame.key.name(e.key).upper()
                        if letra.isalpha() and len(letra) == 1 and letra not in usadas:
                            usadas.add(letra)
                            if letra not in palabra:
                                intentos -= 1
                                if intentos == 0:
                                    fin = True
                                    historial.append({"palabra": palabra, "categoria": cat, "resultado": "Perdió", "puntos": 0})
                            elif all(l in usadas for l in palabra):
                                puntos += 10 + tiempo_restante
                                fin = True
                                historial.append({"palabra": palabra, "categoria": cat, "resultado": "Ganó", "puntos": 10 + tiempo_restante})
                    elif e.key == pygame.K_r:
                        cat, palabra, usadas, intentos, fin, inicio = reiniciar(cat)

            if tiempo_restante <= 0 and not fin:
                fin = True
                historial.append({"palabra": palabra, "categoria": cat, "resultado": "Perdió", "puntos": 0})

            if volver_categorias:
                break

            ventana.blit(fuente.render(f"{cat}: {' '.join([l if l in usadas else '_' for l in palabra])}", True, NEGRO), (20, 150))
            ventana.blit(fuente.render(f"Usadas: {' '.join(sorted(usadas))}", True, NEGRO), (20, 50))
            ventana.blit(fuente.render(f"Intentos: {intentos}", True, NEGRO), (20, 400))
            ventana.blit(fuente.render(f"Puntos: {int(puntos)}", True, VERDE), (20, 450))
            ventana.blit(fuente.render(f"Tiempo: {tiempo_restante}s", True, ROJO), (20, 500))
            ventana.blit(fuente.render("Presiona ESPACIO para regresar a categorías", True, NEGRO), (20, 550))

            if fin:
                if intentos > 0:
                    msg = f"¡Ganaste! | Presiona R para reiniciar"
                else:
                    msg = f"¡Perdiste! Era: {palabra} | Presiona R para reiniciar"
                ventana.blit(fuente.render(msg, True, ROJO), (50, 300))

            dibujar_ahorcado(ventana, intentos)
            pygame.display.flip()

if __name__ == "__main__":
    main()
