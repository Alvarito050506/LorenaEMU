#!/usr/bin/env python3

import os

print("Binvenido a Lorena SO EMU!")
print("Sobre el sistema: ");
print("Lorena es un sistema operativo escrito en C, C++, Ensablador y Bash basado en NextDivel.");
print("Lorena es desarrollado actualmente, este es su tercer lanzamiento.");
print("Comandos:");
print("echo: Imprime el eco de un texto en la pantalla.");
print("clear: Limpia la pantalla.");
print("version: Muestra la version del sistema.");

for i in range (1, 100000):
	shell= input("Shell$ ");
	if shell == "echo":
		echo= input("");
		print(echo);
	elif shell == "clear":
		os.system("clear");
	elif shell == "version":
		print("Lorena emu 0.4.0 - Lorena Shell 0.2.0");
	else:
		print("No se pudo encontrar el comando.")
else:
	exit();
