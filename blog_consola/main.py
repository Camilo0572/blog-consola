from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import buscar_por_titulo, filtrar_por_tag, listar_posts
from blog.validaciones import validar_post


def main():
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            termino = input("Ingresá parte del título a buscar: ")
            buscar_por_titulo(posts, termino)
        elif opcion == 3:
            tag = input("Ingresá el tag a filtrar: ")
            filtrar_por_tag(posts, tag)
        elif opcion == 4:
            print("\nValidando posts:")
            for indice, post in enumerate(posts, start=1):
                es_valido, motivo = validar_post(post)
                titulo = post.get("titulo", "Sin título") if isinstance(post, dict) else "Post inválido"
                if es_valido:
                    print(f"- Post #{indice} ({titulo}): OK ({motivo})")
                else:
                    print(f"- Post #{indice} ({titulo}): ERROR ({motivo})")
        elif opcion == 5:
            print("Saliendo del sistema de blog. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Elegí un número del 1 al 5.")


if __name__ == "__main__":
    main()