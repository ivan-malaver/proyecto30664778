def generar_llaves(equipos):
    # Verificar que el número de equipos sea válido (debe ser 16 para octavos de final)
    if len(equipos) != 16:
        raise ValueError("Debe haber exactamente 16 equipos para octavos de final.")

    # Inicializar el diccionario para almacenar las llaves
    llaves = {
        "Octavos de final": {},
        "Cuartos de final": {},
        "Semifinales": {},
        "Final": {},
        "Tercer lugar": {}
    }

    # Función para que el usuario introduzca los goles y determine el ganador
    def introducir_resultado(equipo1, equipo2):
        while True:
            try:
                goles_equipo1 = int(input(f"Ingresa los goles de {equipo1}: "))
                goles_equipo2 = int(input(f"Ingresa los goles de {equipo2}: "))
                if goles_equipo1 == goles_equipo2:
                    print("Error: No se permiten empates. Intenta de nuevo.")
                else:
                    ganador = equipo1 if goles_equipo1 > goles_equipo2 else equipo2
                    return goles_equipo1, goles_equipo2, ganador
            except ValueError:
                print("Error: Ingresa un número válido de goles.")
    import random  # Importa la librería para mezclar la lista

# Convertir las claves del diccionario en una lista y mezclarla
    equipos_list = list(equipos.keys())
    random.shuffle(equipos_list)
    # Generar los partidos de octavos de final
    ganadores_octavos = []
    for i in range(8):
        partido = f"Partido {i+1}"
        equipo1, equipo2 = list(equipos.keys())[i*2], list(equipos.keys())[i*2+1]
        print(f"\nOctavos de final - {partido}: {equipo1} vs {equipo2}")
        goles_equipo1, goles_equipo2, ganador = introducir_resultado(equipo1, equipo2)
        llaves["Octavos de final"][partido] = {
            "Equipo 1": equipo1,
            "Goles Equipo 1": goles_equipo1,
            "Equipo 2": equipo2,
            "Goles Equipo 2": goles_equipo2,
            "Ganador": ganador
        }
        ganadores_octavos.append(ganador)

    # Generar los partidos de cuartos de final
    ganadores_cuartos = []
    for i in range(4):
        partido = f"Partido {i+1}"
        equipo1, equipo2 = ganadores_octavos[i*2], ganadores_octavos[i*2+1]
        print(f"\nCuartos de final - {partido}: {equipo1} vs {equipo2}")
        goles_equipo1, goles_equipo2, ganador = introducir_resultado(equipo1, equipo2)
        llaves["Cuartos de final"][partido] = {
            "Equipo 1": equipo1,
            "Goles Equipo 1": goles_equipo1,
            "Equipo 2": equipo2,
            "Goles Equipo 2": goles_equipo2,
            "Ganador": ganador
        }
        ganadores_cuartos.append(ganador)

    # Generar los partidos de semifinales
    ganadores_semifinales = []
    for i in range(2):
        partido = f"Partido {i+1}"
        equipo1, equipo2 = ganadores_cuartos[i*2], ganadores_cuartos[i*2+1]
        print(f"\nSemifinales - {partido}: {equipo1} vs {equipo2}")
        goles_equipo1, goles_equipo2, ganador = introducir_resultado(equipo1, equipo2)
        llaves["Semifinales"][partido] = {
            "Equipo 1": equipo1,
            "Goles Equipo 1": goles_equipo1,
            "Equipo 2": equipo2,
            "Goles Equipo 2": goles_equipo2,
            "Ganador": ganador
        }
        ganadores_semifinales.append(ganador)

    # Generar la final
    equipo1, equipo2 = ganadores_semifinales[0], ganadores_semifinales[1]
    print(f"\nFinal: {equipo1} vs {equipo2}")
    goles_equipo1, goles_equipo2, campeon = introducir_resultado(equipo1, equipo2)
    subcampeon = equipo2 if campeon == equipo1 else equipo1
    llaves["Final"]["Partido 1"] = {
        "Equipo 1": equipo1,
        "Goles Equipo 1": goles_equipo1,
        "Equipo 2": equipo2,
        "Goles Equipo 2": goles_equipo2,
        "Ganador": campeon
    }

    # Generar el partido por el tercer lugar (entre los perdedores de las semifinales)
    perdedor_semifinal1 = equipo1 if campeon != equipo1 else equipo2
    perdedor_semifinal2 = ganadores_cuartos[2] if perdedor_semifinal1 == ganadores_cuartos[0] else ganadores_cuartos[3]
    print(f"\nTercer lugar: {perdedor_semifinal1} vs {perdedor_semifinal2}")
    goles_tercero1, goles_tercero2, tercer_lugar = introducir_resultado(perdedor_semifinal1, perdedor_semifinal2)
    llaves["Tercer lugar"]["Partido 1"] = {
        "Equipo 1": perdedor_semifinal1,
        "Goles Equipo 1": goles_tercero1,
        "Equipo 2": perdedor_semifinal2,
        "Goles Equipo 2": goles_tercero2,
        "Ganador": tercer_lugar
    }

    return llaves, campeon, subcampeon, tercer_lugar

# Diccionario de equipos (debe tener 16 equipos)
equipos = {
    "Países Bajos": 0,
    "Estados Unidos": 0,
    "Argentina": 0,
    "Australia": 0,
    "Japón": 0,
    "Croacia": 0,
    "Brasil": 0,
    "Corea del Sur": 0,
    "Inglaterra": 0,
    "Senegal": 0,
    "Francia": 0,
    "Polonia": 0,
    "Marruecos": 0,
    "España": 0,
    "Portugal": 0,
    "Suiza": 0
}

# Generar las llaves del torneo y obtener los resultados
llaves_torneo, campeon, subcampeon, tercer_lugar = generar_llaves(equipos)

print("\nResumen del torneo:")
for ronda, partidos in llaves_torneo.items():
    print(f"\n{ronda}:")
    for partido, resultado in partidos.items():
        print(f"  {partido}:")
        print(f"    {resultado['Equipo 1']} {resultado['Goles Equipo 1']} - {resultado['Goles Equipo 2']} {resultado['Equipo 2']}")
        print(f"    Ganador: {resultado['Ganador']}")

print("\nResultados finales:")
print(f"Campeón: {campeon}")
print(f"Subcampeón: {subcampeon}")
print(f"Tercer lugar: {tercer_lugar}")