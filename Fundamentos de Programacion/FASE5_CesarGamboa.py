DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
CANTIDAD_RECURSOS = 4
UMBRAL_HORAS = 40.0


def leer_numero_no_negativo(mensaje: str) -> float:
    """Solicita un número >= 0 y reintenta ante entradas inválidas."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor < 0:
                print("Error: las horas no pueden ser negativas. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print("Error: ingresa un valor numérico válido (ejemplo: 8 o 7.5).")


def leer_horas_semana(nombre_recurso: str) -> list[float]:
    """Solicita las horas de lunes a viernes para un recurso."""
    horas = []
    print(f"\nIngresa las horas trabajadas por {nombre_recurso}:")
    for dia in DIAS_SEMANA:
        hora = leer_numero_no_negativo(f"  - {dia}: ")
        horas.append(hora)
    return horas


def crear_fila_recurso(indice: int) -> list:
    """Crea una fila con el formato [Nombre, Lun, Mar, Mié, Jue, Vie]."""
    while True:
        nombre = input(f"\nNombre del recurso #{indice}: ").strip()
        if nombre:
            break
        print("Error: el nombre no puede estar vacío.")

    horas = leer_horas_semana(nombre)
    return [nombre] + horas


def registrar_recursos() -> list[list]:
    """Registra la matriz inicial de 4 recursos."""
    matriz = []
    print("=== REGISTRO INICIAL DE RECURSOS (LUNES A VIERNES) ===")
    for i in range(1, CANTIDAD_RECURSOS + 1):
        fila = crear_fila_recurso(i)
        matriz.append(fila)
    return matriz


def modificar_recurso(matriz: list[list]) -> None:
    """Permite actualizar una fila puntual de la matriz por cambio o corrección."""
    while True:
        opcion = input("\n¿Deseas modificar algún recurso o sus horas? (s/n): ").strip().lower()
        if opcion in ("s", "n"):
            break
        print("Responde 's' para sí o 'n' para no.")

    if opcion == "n":
        return

    while True:
        print("\nRecursos registrados:")
        for idx, fila in enumerate(matriz, start=1):
            print(f"  {idx}. {fila[0]}")

        seleccion = input(f"Selecciona el número de recurso a modificar (1-{CANTIDAD_RECURSOS}): ").strip()
        if seleccion.isdigit():
            indice_pos = int(seleccion) - 1
            if 0 <= indice_pos < len(matriz):
                matriz[indice_pos] = crear_fila_recurso(indice_pos + 1)
                print("Registro actualizado correctamente.")
            else:
                print("Número fuera de rango.")
                continue
        else:
            print("Ingresa un número válido.")
            continue

        while True:
            continuar = input("¿Deseas modificar otro recurso? (s/n): ").strip().lower()
            if continuar in ("s", "n"):
                break
            print("Responde 's' para sí o 'n' para no.")

        if continuar == "n":
            break


def calcular_total_horas(fila_recurso: list) -> float:
    """Calcula el total de horas semanales de un recurso (índices 1 al 5)."""
    total = 0.0
    for horas_dia in fila_recurso[1:]:
        total += horas_dia
    return total


def clasificar_jornada(total_horas: float) -> str:
    """Clasifica la jornada según el umbral semanal de 40 horas."""
    if total_horas > UMBRAL_HORAS:
        return "Sobretiempo"
    return "Horario estándar"


def mostrar_reporte(matriz: list[list]) -> None:
    """Muestra el reporte final con nombre, total semanal y clasificación."""
    print("\n=== REPORTE SEMANAL DE JORNADAS ===")
    print(f"{'Recurso':<22} | {'Total Horas':>11} | {'Clasificación'}")
    print("-" * 58)
    for fila in matriz:
        nombre = fila[0]
        total_horas = calcular_total_horas(fila)
        clasificacion = clasificar_jornada(total_horas)
        print(f"{nombre:<22} | {total_horas:>11.2f} | {clasificacion}")


def main() -> None:
    matriz_horas = registrar_recursos()
    modificar_recurso(matriz_horas)
    mostrar_reporte(matriz_horas)


if __name__ == "__main__":
    main()