# Quito, agosto 2025, Daniela Arcos, pda este juego es el ahorcado
import pygame
import random

pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 850, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ahorcado")

# Colores 
BEIGE = (245, 245, 220)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
fuente = pygame.font.SysFont("Comic Sans MS", 30)

# Palabras por categoría
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

# Reiniciar juego con pistas, recibe categoría
def reiniciar(cat):
    palabra = random.choice(palabras[cat]).upper()
    usadas = set()

    # Determinar cuántas letras mostrar
    if len(palabra) >= 5:
        num_pistas = 1
    else:
        num_pistas = 2

    # Elegir posiciones aleatorias y agregarlas a usadas
    posiciones = random.sample(range(len(palabra)), num_pistas)
    for pos in posiciones:
        usadas.add(palabra[pos])

    return cat, palabra, usadas, 7, False

# Función para elegir categoría antes de jugar
def elegir_categoria():
    categorias = list(palabras.keys())
    seleccion = None
    while seleccion is None:
        ventana.fill(BEIGE)
        ventana.blit(fuente.render("Elige categoría:", True, NEGRO), (250, 50))
        for i, cat in enumerate(categorias):
            texto = f"{i+1}. {cat}"
            ventana.blit(fuente.render(texto, True, NEGRO), (300, 100 + i*50))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.unicode.isdigit():
                    num = int(e.unicode)
                    if 1 <= num <= len(categorias):
                        seleccion = categorias[num - 1]
    return seleccion


# Dibujo del ahorcado
def dibujar_ahorcado(superficie, intentos):
    base_x = 700
    base_y = 400

    # Soporte
    pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y), (base_x + 100, base_y), 5)
    pygame.draw.line(superficie, NEGRO, (base_x, base_y), (base_x, base_y - 300), 5)
    pygame.draw.line(superficie, NEGRO, (base_x, base_y - 300), (base_x - 100, base_y - 300), 5)
    pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 300), (base_x - 100, base_y - 250), 5)

    errores = 7 - intentos

    if errores >= 1:  # cabeza
        pygame.draw.circle(superficie, NEGRO, (base_x - 100, base_y - 220), 30, 3)
    if errores >= 2:  # cuerpo
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 190), (base_x - 100, base_y - 120), 3)
    if errores >= 3:  # brazo izquierdo
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 180), (base_x - 130, base_y - 150), 3)
    if errores >= 4:  # brazo derecho
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 180), (base_x - 70, base_y - 150), 3)
    if errores >= 5:  # pierna izquierda
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 120), (base_x - 130, base_y - 80), 3)
    if errores >= 6:  # pierna derecha
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 120), (base_x - 70, base_y - 80), 3)  
    if errores >= 7:  # cuerda
        pygame.draw.line(superficie, NEGRO, (base_x - 100, base_y - 250), (base_x - 100, base_y - 280), 3)

def main():
    cat = elegir_categoria()
    cat, palabra, usadas, intentos, fin = reiniciar(cat)

    while True:
        ventana.fill(BEIGE)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    # Cambiar categoría con la tecla espacio
                    cat = elegir_categoria()
                    cat, palabra, usadas, intentos, fin = reiniciar(cat)
                elif not fin:
                    letra = pygame.key.name(e.key).upper()
                    if letra.isalpha() and len(letra) == 1 and letra not in usadas:
                        usadas.add(letra)
                        if letra not in palabra:
                            intentos -= 1
                            if intentos == 0:
                                fin = True
                        elif all(l in usadas for l in palabra):
                            fin = True
                elif e.key == pygame.K_r:
                    cat, palabra, usadas, intentos, fin = reiniciar(cat)

        texto = " ".join([l if l in usadas else "_" for l in palabra])
        ventana.blit(fuente.render(f"{cat}: {texto}", True, NEGRO), (20, 150))
        ventana.blit(fuente.render(f"Usadas: {' '.join(sorted(usadas))}", True, NEGRO), (20, 50))
        ventana.blit(fuente.render(f"Intentos: {intentos}", True, NEGRO), (20, 400))

        ventana.blit(fuente.render("Presiona ESPACIO para cambiar categoría", True, NEGRO), (20, 500))


        if fin:
            if intentos > 0:
                msg = "¡Ganaste! Presiona R para reiniciar"
            else:
                msg = f"¡Perdiste! Era: {palabra} | Presiona R para reiniciar"
            ventana.blit(fuente.render(msg, True, ROJO), (78, 300))
          

        dibujar_ahorcado(ventana, intentos)
        pygame.display.flip()

if __name__ == "__main__":
    main()
