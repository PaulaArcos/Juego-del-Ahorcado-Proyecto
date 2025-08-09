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

# Inicializa Pygame (necesario para usar sus funciones gráficas y de eventos)
pygame.init()

# =============================
# CONFIGURACIÓN INICIAL
# =============================

# Dimensiones de la ventana
ANCHO, ALTO = 850, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ahorcado")  # Título de la ventana

# Colores RGB
BEIGE = (245, 245, 220)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)

# Fuente para mostrar texto
fuente = pygame.font.SysFont("Comic Sans MS", 30)

# Diccionario con categorías y listas de palabras
palabras = {
    "Cocina": [
        "Refrigeradora", "Horno", "Sartenes", "Microondas", "Tostadora", "Licuadora"],
    "Animales": [
        "Elefante", "León", "Tigre", "Jirafa", "Cocodrilo", "Hipopótamo"],
    "País": [
        "Ecuador", "México", "Canada", "Argentina", "Brasil", "Colombia"],
    "Colores": [
        "Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Violeta"],
    "Deportes": [
        "Fútbol", "Baloncesto", "Tenis", "Natación", "Ciclismo", "Atletismo"],
    "Instrumentos": [
        "Guitarra", "Piano", "Batería", "Violín", "Saxofón", "Flauta" ]
}

# =============================
# FUNCIÓN: Reiniciar juego
# =============================
def reiniciar(cat):
    """
    Reinicia el juego seleccionando una palabra aleatoria
    de la categoría dada y revelando algunas letras como pistas.

    Parámetros:
        cat (str): nombre de la categoría elegida.
    Retorna:
        cat (str): categoría elegida.
        palabra (str): palabra secreta en mayúsculas.
        usadas (set): conjunto de letras ya usadas.
        7 (int): número de intentos disponibles.
        False (bool): estado inicial del fin de juego.
    """
    palabra = random.choice(palabras[cat]).upper()  # Escoge palabra aleatoria
    usadas = set()

    # Determinar cuántas letras mostrar al inicio como pistas
    if len(palabra) >= 5:
        num_pistas = 1  # Si es larga, menos pistas
    else:
        num_pistas = 2  # Si es corta, más pistas

    # Seleccionar posiciones al azar y agregarlas como letras usadas
    posiciones = random.sample(range(len(palabra)), num_pistas)
    for pos in posiciones:
        usadas.add(palabra[pos])

    return cat, palabra, usadas, 7, False

# =============================
# FUNCIÓN: Elegir categoría
# =============================
def elegir_categoria():
    """
    Muestra un menú para elegir la categoría antes de iniciar el juego.
    El jugador selecciona presionando el número correspondiente.
    """
    categorias = list(palabras.keys())
    seleccion = None

    while seleccion is None:
        ventana.fill(BEIGE)
        ventana.blit(fuente.render("Elige categoría:", True, NEGRO), (250, 50))

        # Mostrar lista numerada de categorías
        for i, cat in enumerate(categorias):
            texto = f"{i+1}. {cat}"
            ventana.blit(fuente.render(texto, True, NEGRO), (300, 100 + i*50))
        pygame.display.flip()

        # Manejo de eventos de selección
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN and e.unicode.isdigit():
                num = int(e.unicode)
                if 1 <= num <= len(categorias):
                    seleccion = categorias[num - 1]

    return seleccion

# =============================
# FUNCIÓN: Dibujar ahorcado
# =============================
def dibujar_ahorcado(superficie, intentos):
    """
    Dibuja el soporte y el ahorcado según el número de intentos restantes.
    A más errores, más partes se muestran.
    """
    base_x = 700
    base_y = 400

    # Estructura del soporte
    pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y), (base_x + 100, base_y), 5)   # Base
    pygame.draw.line(superficie, NEGRO, (base_x, base_y), (base_x, base_y - 300), 5)         # Poste vertical
    pygame.draw.line(superficie, NEGRO, (base_x, base_y - 300), (base_x - 100, base_y - 300), 5) # Barra superior
    pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 300), (base_x - 100, base_y - 250), 5) # Cuerda

    errores = 7 - intentos  # Calcular errores cometidos

    # Dibujar partes del cuerpo en orden
    if errores >= 1:  # Cabeza
        pygame.draw.circle(superficie, NEGRO, (base_x - 100, base_y - 220), 30, 3)
    if errores >= 2:  # Cuerpo
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 190), (base_x - 100, base_y - 120), 3)
    if errores >= 3:  # Brazo izquierdo
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 180), (base_x - 130, base_y - 150), 3)
    if errores >= 4:  # Brazo derecho
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 180), (base_x - 70, base_y - 150), 3)
    if errores >= 5:  # Pierna izquierda
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 120), (base_x - 130, base_y - 80), 3)
    if errores >= 6:  # Pierna derecha
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 120), (base_x - 70, base_y - 80), 3)  
    if errores >= 7:  # Cuerda final (simboliza derrota)
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 250), (base_x - 100, base_y - 280), 3)

# =============================
# FUNCIÓN PRINCIPAL
# =============================
def main():
    """
    Función principal del juego.
    Controla el flujo: elegir categoría, jugar, dibujar y reiniciar.
    """
    cat = elegir_categoria()
    cat, palabra, usadas, intentos, fin = reiniciar(cat)

    while True:
        ventana.fill(BEIGE)

        # Gestión de eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    # Cambiar categoría y reiniciar juego
                    cat = elegir_categoria()
                    cat, palabra, usadas, intentos, fin = reiniciar(cat)
                elif not fin:
                    # Convertir tecla en letra y validar
                    letra = pygame.key.name(e.key).upper()
                    if letra.isalpha() and len(letra) == 1 and letra not in usadas:
                        usadas.add(letra)
                        if letra not in palabra:
                            intentos -= 1
                            if intentos == 0:  # Sin intentos → perder
                                fin = True
                        elif all(l in usadas for l in palabra):  # Todas adivinadas → ganar
                            fin = True
                elif e.key == pygame.K_r:
                    # Reiniciar la misma categoría después de terminar
                    cat, palabra, usadas, intentos, fin = reiniciar(cat)

        # Mostrar palabra con guiones y letras acertadas
        texto = " ".join([l if l in usadas else "_" for l in palabra])
        ventana.blit(fuente.render(f"{cat}: {texto}", True, NEGRO), (20, 150))

        # Mostrar letras usadas
        ventana.blit(fuente.render(f"Usadas: {' '.join(sorted(usadas))}", True, NEGRO), (20, 50))

        # Mostrar intentos restantes
        ventana.blit(fuente.render(f"Intentos: {intentos}", True, NEGRO), (20, 400))

        # Instrucciones
        ventana.blit(fuente.render("Presiona ESPACIO para cambiar categoría", True, NEGRO), (20, 500))

        # Mostrar mensaje de fin de juego
        if fin:
            if intentos > 0:
                msg = "¡Ganaste! Presiona R para reiniciar"
            else:
                msg = f"¡Perdiste! Era: {palabra} | Presiona R para reiniciar"
            ventana.blit(fuente.render(msg, True, ROJO), (78, 300))
          
        # Dibujar ahorcado
        dibujar_ahorcado(ventana, intentos)

        # Actualizar pantalla
        pygame.display.flip()

# =============================
# EJECUCIÓN DEL JUEGO
# =============================
if __name__ == "__main__":
    main()
