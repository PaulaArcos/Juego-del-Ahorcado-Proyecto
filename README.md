# Juego-del-Ahorcado-Proyecto
Este es un juego clásico del Ahorcado desarrollado en Python usando la librería Pygame. Permite al jugador elegir categorías y adivinar palabras ocultas, mostrando un dibujo del ahorcado conforme se cometen errores. Cuenta con pistas automáticas, cambio de categorías y reinicio del juego para una experiencia dinámica y entretenida.

# Características
Elección de categoría entre varias opciones (Cocina, Animales, Países, Colores, Deportes, Instrumentos).

Pistas automáticas mostrando 1 o 2 letras según la longitud de la palabra.

Visualización gráfica del ahorcado conforme se van perdiendo intentos.

Interfaz sencilla y clara con mensajes para ganar o perder.

Posibilidad de cambiar la categoría con la tecla ESPACIO.

Reinicio del juego con la tecla R.

# Requisitos
Python 3.x

Pygame (se puede instalar con pip install pygame)

# Uso
Ejecutar el script:

poner en la terminal python ahorcado.py
En la pantalla inicial, elegir una categoría presionando el número correspondiente (1-6).

Comenzar a adivinar letras presionando las teclas del teclado.

Puedes cambiar la categoría en cualquier momento presionando ESPACIO.

Cuando el juego termine (ganes o pierdas), presiona R para reiniciar.

# Controles
Letras: para adivinar.

ESPACIO: cambiar categoría y reiniciar con una nueva palabra.

R: reiniciar la partida con la misma categoría.

Cerrar ventana: salir del juego.

# Estructura del código
palabras: Diccionario con categorías y listas de palabras.

reiniciar(cat): Inicializa el juego con una palabra nueva de la categoría seleccionada y pistas.

elegir_categoria(): Permite seleccionar la categoría antes de empezar.

dibujar_ahorcado(): Dibuja el ahorcado en la pantalla según los intentos fallidos.

main(): Bucle principal que controla la lógica del juego y la interacción.
