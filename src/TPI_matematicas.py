
# TPI 2 Matematicas - Diagrama de Venn para 3 conjuntos
# Autor: Mateo Fernández
# Comision : 19 
print("===============================================================================")
print("TPI 2 Matematicas - Diagrama de Venn para 3 conjuntos")
print("===============================================================================")
print("\nBienvenido al programa de Diagrama de Venn para 3 conjuntos")

# ============= FUNCIONES DE VALIDACION =============

def obtener_numero_positivo(mensaje, minimo=0, maximo=1000000):
    """
    Solicita un número al usuario con validación de tipo y rango.
    Valida: que sea un número (no texto), que sea >= minimo, y que sea <= maximo.
    Reintentos infinitos hasta obtener un valor válido.
    """
    while True:
        try:
            valor = int(input(mensaje))
            # Validación: número no negativo (o mayor al mínimo especificado)
            if valor < minimo:
                print(f"❌ Error: El valor debe ser >= {minimo}")
                continue
            # Validación: número dentro del límite máximo razonable
            if valor > maximo:
                print(f"❌ Error: El valor debe ser <= {maximo}")
                continue
            return valor
        except ValueError:
            # Validación: entrada debe ser un número entero válido
            print("❌ Error: Debe ingresar un número entero válido")

def obtener_nombres():
    """
    Solicita los nombres de los 3 conjuntos con validación.
    Valida: nombres no vacíos y sin duplicados.
    """
    nombres = []
    for i in range(3):
        while True:
            nombre = input(f"\nIngrese el nombre del sistema operativo para el conjunto {i+1} (ej: Windows, Linux, macOS): ").strip()
            # Validación: nombre no puede estar vacío
            if not nombre:
                print("❌ Error: El nombre no puede estar vacío")
                continue
            # Validación: no puede haber nombres duplicados
            if nombre in nombres:
                print(f"❌ Error: El nombre '{nombre}' ya fue utilizado")
                continue
            nombres.append(nombre)
            break
    return nombres

def validar_intersecciones(nombres, valores, intersecciones):
    """
    Valida la coherencia lógica de las intersecciones.
    Revisa que: AB <= min(A,B), AC <= min(A,C), BC <= min(B,C), ABC <= min(AB,AC,BC)
    """
    A, B, C = nombres
    
    # Validación: intersección AB no puede exceder los menores valores de A y B
    if intersecciones["AB"] > min(valores[A], valores[B]):
        print(f"❌ Error: A∩B ({intersecciones['AB']}) no puede ser mayor que min(A,B) = {min(valores[A], valores[B])}")
        return False
    
    # Validación: intersección AC no puede exceder los menores valores de A y C
    if intersecciones["AC"] > min(valores[A], valores[C]):
        print(f"❌ Error: A∩C ({intersecciones['AC']}) no puede ser mayor que min(A,C) = {min(valores[A], valores[C])}")
        return False
    
    # Validación: intersección BC no puede exceder los menores valores de B y C
    if intersecciones["BC"] > min(valores[B], valores[C]):
        print(f"❌ Error: B∩C ({intersecciones['BC']}) no puede ser mayor que min(B,C) = {min(valores[B], valores[C])}")
        return False
    
    # Validación: intersección triple no puede exceder las intersecciones dobles
    if intersecciones["ABC"] > min(intersecciones["AB"], intersecciones["AC"], intersecciones["BC"]):
        print(f"❌ Error: A∩B∩C ({intersecciones['ABC']}) no puede ser mayor que min(A∩B, A∩C, B∩C)")
        return False
    
    return True

def solicitar_datos():
    """
    Solicita datos del usuario con validaciones completas.
    Retorna: U, nombres, valores e intersecciones validadas.
    """
    # Validación: el universo debe ser > 0 y dentro de límites razonables
    U = obtener_numero_positivo("\nIngrese la cantidad total de empleados (Universo U): ", minimo=1)
    
    # Validación: nombres no vacíos y sin duplicados
    nombres = obtener_nombres()
    
    valores = {}
    for nombre in nombres:
        # Validación: cantidad de empleados en cada conjunto debe ser >= 0 y <= U
        cantidad = obtener_numero_positivo(
            f"\nIngrese la cantidad de empleados que usan {nombre}: ",
            minimo=0,
            maximo=U
        )
        valores[nombre] = cantidad
    
    print("\nAhora ingrese las intersecciones entre los conjuntos:\n")    
    intersecciones = {}
    
    # Validación: intersecciones no negativas y dentro de límites
    intersecciones["AB"] = obtener_numero_positivo(
        "Ingrese la cantidad en A ∩ B (Conjuntos 1 y 2): ",
        minimo=0,
        maximo=U
    )
    intersecciones["AC"] = obtener_numero_positivo(
        "Ingrese la cantidad en A ∩ C (Conjuntos 1 y 3): ",
        minimo=0,
        maximo=U
    )
    intersecciones["BC"] = obtener_numero_positivo(
        "Ingrese la cantidad en B ∩ C (Conjuntos 2 y 3): ",
        minimo=0,
        maximo=U
    )
    intersecciones["ABC"] = obtener_numero_positivo(
        "Ingrese la cantidad en A ∩ B ∩ C (Todos los conjuntos): ",
        minimo=0,
        maximo=U
    )
    
    # Validación: coherencia lógica de intersecciones
    while not validar_intersecciones(nombres, valores, intersecciones):
        print("\nPor favor, ingrese las intersecciones nuevamente:\n")
        intersecciones["AB"] = obtener_numero_positivo(
            "Ingrese la cantidad en A ∩ B (Conjuntos 1 y 2): ",
            minimo=0,
            maximo=U
        )
        intersecciones["AC"] = obtener_numero_positivo(
            "Ingrese la cantidad en A ∩ C (Conjuntos 1 y 3): ",
            minimo=0,
            maximo=U
        )
        intersecciones["BC"] = obtener_numero_positivo(
            "Ingrese la cantidad en B ∩ C (Conjuntos 2 y 3): ",
            minimo=0,
            maximo=U
        )
        intersecciones["ABC"] = obtener_numero_positivo(
            "Ingrese la cantidad en A ∩ B ∩ C (Todos los conjuntos): ",
            minimo=0,
            maximo=U
        )
    
    return U, nombres, valores, intersecciones


# Esta función calcula las regiones exclusivas de cada conjunto, las intersecciones exclusivas entre pares de conjuntos, la intersección de los tres conjuntos, y la 
# cantidad de empleados que no pertenecen a ninguno de los conjuntos.
def calcular_exclusivos(U, nombres, valores, intersecciones):
    """
    Calcula las regiones del diagrama de Venn con validaciones finales.
    Valida que: todas las regiones sean >= 0 y que la unión <= U.
    """
    A, B, C = nombres
    
    # Cálculo de intersecciones exclusivas entre pares de conjuntos (restando la intersección triple)
    solo_AB = intersecciones["AB"] - intersecciones["ABC"]
    solo_AC = intersecciones["AC"] - intersecciones["ABC"]
    solo_BC = intersecciones["BC"] - intersecciones["ABC"]
    
    # Cálculo de exclusivos de cada conjunto (restando las intersecciones exclusivas y la intersección triple)
    solo_A = valores[A] - solo_AB - solo_AC - intersecciones["ABC"]
    solo_B = valores[B] - solo_AB - solo_BC - intersecciones["ABC"]
    solo_C = valores[C] - solo_AC - solo_BC - intersecciones["ABC"]
    
    # Validación: las regiones exclusivas no deben ser negativas
    if solo_A < 0 or solo_B < 0 or solo_C < 0 or solo_AB < 0 or solo_AC < 0 or solo_BC < 0:
        print("❌ Error crítico: Los datos ingresados producen regiones negativas.")
        print("Por favor, verifique que las intersecciones sean coherentes con los conjuntos.")
        return None
    
    # Unión de todos los conjuntos (sumando exclusivos e intersecciones)
    union = solo_A + solo_B + solo_C + solo_AB + solo_AC + solo_BC + intersecciones["ABC"]
    
    # Validación: la unión no debe exceder el universo
    if union > U:
        print(f"❌ Error crítico: La unión ({union}) excede el universo ({U})")
        print("Por favor, verifique que los datos sean coherentes.")
        return None
    
    # Fuera de todos / Ninguno (total del universo menos la unión de los conjuntos)
    fuera = U - union
    
    # Retornamos un diccionario con los resultados de cada región del diagrama de Venn para su posterior visualización.
    # Los nombres de las claves utilizan los nombres reales ingresados por el usuario (ej: Windows, Linux, macOS) en lugar de A, B, C
    return {  
        f"Solo {A}": solo_A,
        f"Solo {B}": solo_B,
        f"Solo {C}": solo_C,
        f"Solo {A} ∩ {B}": solo_AB,
        f"Solo {A} ∩ {C}": solo_AC,
        f"Solo {B} ∩ {C}": solo_BC,
        f"{A} ∩ {B} ∩ {C}": intersecciones["ABC"],
        "Ninguno": fuera
    }


def mostrar_resultados(resultados):
    """
    Muestra los resultados de manera clara y formateada.
    Valida que los resultados no sean None antes de mostrar.
    """
    if resultados is None:
        print("\n⚠️  No se pudieron calcular los resultados debido a errores en los datos.")
        return
    
    print("\n" + "="*50)
    print("--- RESULTADOS DEL DIAGRAMA DE VENN ---")
    print("="*50)
    for region, cantidad in resultados.items():
        print(f"{region:.<30} {cantidad}")
    print("="*50)

# con esta fucion se ejecuta el programa, se llama a la función solicitar_datos, que retorna los datos ingresados y los guardas en las variables U, nombres, valores e 
# intersecciones. Luego se llama a la función calcular_exclusivos, que procesa esos datos y retorna un DICCIONARIO con los resultados de cada región del diagrama de Venn. 
# Finalmente, se llama a la función mostrar_resultados para imprimir los resultados en pantalla.
def main():
    """
    Función principal que coordina todo el programa con manejo de errores.
    """
    try:
        U, nombres, valores, intersecciones = solicitar_datos()
        resultados = calcular_exclusivos(U, nombres, valores, intersecciones)
        mostrar_resultados(resultados)
    except KeyboardInterrupt:
        # Validación: permite que el usuario salga del programa con Ctrl+C
        print("\n\n⚠️  Programa interrumpido por el usuario.")
    except Exception as e:
        # Validación: captura cualquier error inesperado
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, intente nuevamente.")


# Punto de entrada del programa
main()
