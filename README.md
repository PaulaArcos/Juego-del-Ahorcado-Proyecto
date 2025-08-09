# Juego del Ahorcado en Pygame
Descripción
Este proyecto es una implementación del clásico juego Ahorcado utilizando la biblioteca Pygame para Python. El juego permite elegir entre varias categorías de palabras y ofrece pistas automáticas para facilitar la experiencia. Se incluyen controles para cambiar categorías y reiniciar el juego.

El desarrollo se realizó utilizando Visual Studio como entorno de desarrollo integrado (IDE), aprovechando sus herramientas para depuración y gestión del proyecto.

# Características
Selección de categoría antes de comenzar a jugar.

Pistas automáticas al revelar algunas letras al inicio.

Gráficos dinámicos del ahorcado que se van dibujando con cada error.

Control por teclado:

Presiona una letra para adivinar.

Presiona ESPACIO para cambiar de categoría y reiniciar.

Presiona R para reiniciar la misma categoría después de ganar o perder.

Interfaz sencilla y clara con texto y gráficos.

# Categorías disponibles
Cocina

Animales

Países

Colores

Deportes

Instrumentos

Cada categoría contiene una lista de palabras relacionadas para adivinar.

# Requisitos
Python 3.x

Pygame

Visual Studio (opcional, para desarrollo y depuración)

Puedes instalar Pygame con:

pip install pygame
# Uso
Abre el proyecto en Visual Studio o ejecuta el archivo principal directamente con Python:

bash
Copiar
Editar
python ahorcado.py
En la pantalla inicial, selecciona una categoría presionando el número correspondiente.

Presiona letras en el teclado para adivinar la palabra oculta.

Observa cómo se dibuja el ahorcado con cada error.

Cambia de categoría en cualquier momento presionando ESPACIO.

Al ganar o perder, presiona R para reiniciar la misma categoría.

# Cómo funciona el juego
Al iniciar, se elige una categoría y una palabra secreta al azar.

Se revelan automáticamente algunas letras como pistas.

Cada letra incorrecta disminuye el número de intentos restantes.

El ahorcado se dibuja gradualmente conforme se cometen errores.

El juego termina si adivinas todas las letras o si se agotan los intentos.

Estructura del código
reiniciar(cat): Reinicia el juego con una nueva palabra de la categoría cat.

elegir_categoria(): Muestra el menú para seleccionar categoría.

dibujar_ahorcado(superficie, intentos): Dibuja el ahorcado según los errores cometidos.

main(): Controla el flujo general del juego, eventos, y actualización de pantalla.

# Autor
Daniela Arcos — Quito, agosto 2025
