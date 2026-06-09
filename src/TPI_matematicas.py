def solicitar_datos():
    U = int(input("Ingrese la cantidad total de empleados (Universo U): "))
    nombres = []
    for i in range(3):
        nombres.append(input(f"Ingrese el nombre del conjunto {i+1} (ej: Windows, Linux, macOS): "))
    
    valores = {}
    for nombre in nombres:
        valores[nombre] = int(input(f"Ingrese la cantidad de empleados que usan {nombre}: "))
    
    intersecciones = {}
    intersecciones["AB"] = int(input("Ingrese la cantidad en A ∩ B: "))
    intersecciones["AC"] = int(input("Ingrese la cantidad en A ∩ C: "))
    intersecciones["BC"] = int(input("Ingrese la cantidad en B ∩ C: "))
    intersecciones["ABC"] = int(input("Ingrese la cantidad en A ∩ B ∩ C: "))
    
    return U, nombres, valores, intersecciones


def calcular_exclusivos(U, nombres, valores, intersecciones):
    # Desempaquetar nombres
    A, B, C = nombres
    
    # Intersecciones exclusivas
    solo_AB = intersecciones["AB"] - intersecciones["ABC"]
    solo_AC = intersecciones["AC"] - intersecciones["ABC"]
    solo_BC = intersecciones["BC"] - intersecciones["ABC"]
    
    # Exclusivos de cada conjunto
    solo_A = valores[A] - solo_AB - solo_AC - intersecciones["ABC"]
    solo_B = valores[B] - solo_AB - solo_BC - intersecciones["ABC"]
    solo_C = valores[C] - solo_AC - solo_BC - intersecciones["ABC"]
    
    # Unión
    union = solo_A + solo_B + solo_C + solo_AB + solo_AC + solo_BC + intersecciones["ABC"]
    
    # Fuera de todos
    fuera = U - union
    
    return {
        "Solo A": solo_A,
        "Solo B": solo_B,
        "Solo C": solo_C,
        "Solo A∩B": solo_AB,
        "Solo A∩C": solo_AC,
        "Solo B∩C": solo_BC,
        "A∩B∩C": intersecciones["ABC"],
        "Ninguno": fuera
    }


def mostrar_resultados(resultados):
    print("\n--- Resultados ---")
    for region, cantidad in resultados.items():
        print(f"{region}: {cantidad}")


def main():
    U, nombres, valores, intersecciones = solicitar_datos()
    resultados = calcular_exclusivos(U, nombres, valores, intersecciones)
    mostrar_resultados(resultados)


if __name__ == "__main__":
    main()
