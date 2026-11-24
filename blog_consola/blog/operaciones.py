def listar_posts(lista):
    print("\nPosts disponibles:")
    for post in lista:
        if not isinstance(post, dict):
            print("- [Post inválido]")
            continue

        titulo = post.get("titulo") or "Sin título"
        estado = post.get("estado") or "sin estado"
        autor = post.get("autor")

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre") or "Autor desconocido"
        else:
            nombre_autor = str(autor) if autor else "Autor desconocido"

        print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado}")


def buscar_por_titulo(lista, termino):
    termino_limpio = termino.strip().lower()
    if not termino_limpio:
        print("La búsqueda no puede estar vacía.")
        return []

    resultados = []
    for post in lista:
        if isinstance(post, dict):
            titulo = post.get("titulo")
            if isinstance(titulo, str) and termino_limpio in titulo.lower():
                resultados.append(post)

    if resultados:
        print("\nResultados de la búsqueda:")
        for post in resultados:
            autor = post.get("autor") if isinstance(post.get("autor"), dict) else {}
            nombre_autor = autor.get("nombre", "Autor desconocido")
            estado = post.get("estado", "sin estado")
            print(f"- {post.get('titulo')} | Autor: {nombre_autor} | Estado: {estado}")
    else:
        print("No se encontraron posts con ese título.")

    return resultados


def filtrar_por_tag(lista, tag):
    tag_limpio = tag.strip().lower()
    if not tag_limpio:
        print("El tag no puede estar vacío.")
        return []

    filtrados = []
    for post in lista:
        if isinstance(post, dict):
            tags = post.get("tags")
            if isinstance(tags, list):
                for item_tag in tags:
                    if isinstance(item_tag, str) and item_tag.lower() == tag_limpio:
                        filtrados.append(post)
                        break

    if filtrados:
        print(f"\nPosts con el tag '{tag.strip()}':")
        for post in filtrados:
            print(f"- {post.get('titulo', 'Sin título')}")
    else:
        print("No hay posts con ese tag.")

    return filtrados