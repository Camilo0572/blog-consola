def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Elegí una opción (1-5): ").strip())
        return opcion
    except ValueError:
        print("Error: debés ingresar un número del 1 al 5.")
        return None