🎮 Conecta-N en Python

El proyecto es una versión ampliada y configurable del clásico Conecta 4, permitiendo definir tanto el tamaño del tablero como el número de fichas necesarias para ganar la partida.

⸻

🧩 Descripción del juego

Conecta-N es un juego de tablero por turnos en el que dos jugadores colocan fichas en un tablero vertical.
Las fichas caen hasta la posición libre más baja de la columna seleccionada.

El objetivo es conseguir N fichas en línea, ya sea:
	•	Horizontal
	•	Vertical
	•	Diagonal

El juego finaliza cuando:
	•	Un jugador consigue N fichas en línea (victoria)
	•	No quedan casillas libres (empate)

⸻

⚙️ Características principales
	•	🧱 Tablero configurable
	•	Número de filas y columnas definidos por el usuario
	•	Tamaño mínimo: 6 × 7
	•	🏆 Número de fichas en línea configurable
	•	Mínimo 4
	•	Máximo permitido según el tamaño del tablero
	•	👥 Dos modos de juego
	•	Jugador vs Jugador
	•	Jugador vs IA
	•	🤖 IA con dos niveles de dificultad
	•	Nivel 1: movimientos aleatorios
	•	Nivel 2: IA con reglas de decisión estratégicas
	•	🎨 Representación en consola
	•	Tablero en modo texto
	•	Fichas representadas con O y X
	•	Última ficha colocada resaltada con un color distinto

⸻

🕹️ Modos de juego

👤 Jugador vs Jugador

Dos jugadores humanos se turnan para introducir la columna donde desean colocar su ficha.

🤖 Jugador vs IA

Nivel 1
La máquina coloca la ficha de forma aleatoria entre las columnas disponibles.

Nivel 2 (IA inteligente)
La IA aplica las siguientes reglas en orden de prioridad:
	1.	Colocar la ficha que le permita ganar la partida
	2.	Bloquear una jugada ganadora del jugador
	3.	Colocar la ficha que genere el mayor número de fichas en línea
	4.	Colocar una ficha aleatoria si no se cumple ninguna regla anterior

⸻

🛠️ Funcionamiento del programa

Al iniciar el juego, el programa solicita:
	1.	Tamaño del tablero (filas y columnas)
	2.	Número de fichas necesarias para ganar
	3.	Modo de juego
	4.	Nombre de los jugadores

Durante la partida:
	•	Se validan todas las entradas del usuario
	•	Se notifica si una columna no existe o está llena
	•	El tablero se muestra tras cada jugada
	•	El juego continúa hasta victoria o empate

⸻

Espero que lo disfruteis!
  
