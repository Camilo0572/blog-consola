from blog.datos import estados_post


def validar_post(post):
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    claves_obligatorias = ("id", "titulo", "contenido", "autor", "tags", "estado")
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    titulo = post.get("titulo")
    if not isinstance(titulo, str) or not titulo.strip():
        return False, 'el campo "titulo" está vacío o no es texto'

    contenido = post.get("contenido")
    if not isinstance(contenido, str) or not contenido.strip():
        return False, 'el campo "contenido" está vacío o no es texto'

    autor = post.get("autor")
    if not isinstance(autor, dict):
        return False, 'el campo "autor" debe ser un diccionario'

    nombre_autor = autor.get("nombre")
    if not isinstance(nombre_autor, str) or not nombre_autor.strip():
        return False, 'el diccionario "autor" no tiene un "nombre" válido'

    tags = post.get("tags")
    if not isinstance(tags, list):
        return False, 'el campo "tags" debe ser una lista'

    estado = post.get("estado")
    if estado not in estados_post:
        return False, f'el estado "{estado}" no está permitido'

    return True, "válido"