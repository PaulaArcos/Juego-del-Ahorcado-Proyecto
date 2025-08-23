Juego del Ahorcado en Pygame
# Descripción

Este proyecto es una implementación del clásico juego Ahorcado utilizando la biblioteca Pygame para Python.
El juego permite elegir entre varias categorías de palabras y ofrece pistas automáticas para facilitar la experiencia. Además, incluye un historial de partidas y controles para cambiar categorías o reiniciar el juego.

El desarrollo se realizó utilizando Visual Studio como entorno de desarrollo integrado (IDE), aprovechando sus herramientas para depuración y gestión del proyecto.
# ✨ Características

 ● Selección de categoría antes de comenzar a jugar.

 ● Pistas automáticas: algunas letras se revelan al inicio según la longitud de la palabra.

 ● Gráficos dinámicos del ahorcado que se dibujan con cada error.

 ● Control por teclado:

 ● Presiona una letra para adivinar.

 ● Presiona ESPACIO para cambiar de categoría y reiniciar.

 ● Presiona R para reiniciar la misma palabra después de ganar o perder.

 ● Interfaz sencilla y clara con texto y gráficos.

 ● Historial de partidas: registra últimas partidas mostrando palabra, categoría, resultado y puntos.

 ● Sistema de puntaje: 10 puntos base + tiempo restante por palabra acertada.

# 📂 Categorías disponibles

 ● Cocina

 ● Animales

 ● Países

 ● Colores

 ● Deportes

 ● Instrumentos

 ● Frutas

 ● Verduras

 ● Profesiones

Cada categoría contiene una lista de palabras relacionadas para adivinar.

# 🖥️ Requisitos

 ● Python 3.11.exe 

 ● Pygame

 ● Visual Studio (para desarrollo)

 ● Instalación de Pygame:

 ● pip install pygame

# ▶️ Uso

Abre el proyecto en Visual Studio o ejecuta el archivo principal directamente con Python:

python ahorcado.py


En la pantalla inicial, selecciona una opción:

INICIAR: comenzar nueva partida.

HISTORIAL: ver últimas partidas.

SALIR: cerrar el juego.

Al iniciar, elige una categoría presionando el número correspondiente.

Presiona letras en el teclado para adivinar la palabra oculta.

Observa cómo se dibuja el ahorcado con cada error.

Cambia de categoría en cualquier momento presionando ESPACIO.

Al ganar o perder, presiona R para reiniciar la misma palabra.

# ⚙️ Cómo funciona el juego

Se selecciona una categoría y una palabra secreta al azar.

Algunas letras se revelan automáticamente como pistas.

Cada letra incorrecta disminuye el número de intentos restantes.

El ahorcado se dibuja gradualmente conforme se cometen errores.

El juego termina si adivinas todas las letras o si se agotan los intentos.

Se registran los resultados en un historial, incluyendo puntos y categoría.

# 📜 Estructura del código

reiniciar(cat): Reinicia el juego con una nueva palabra de la categoría cat.

elegir_categoria(): Muestra el menú para seleccionar categoría.

dibujar_ahorcado(superficie, intentos): Dibuja el ahorcado según los errores cometidos.

pantalla_historial(): Muestra las últimas partidas jugadas con resultados y puntos.

pantalla_inicio(): Pantalla de bienvenida con botones para iniciar, historial o salir.

main(): Controla el flujo general del juego, eventos, actualización de pantalla y puntaje.

# 👩‍💻 Autor

Daniela Arcos — Quito, agosto 2025
