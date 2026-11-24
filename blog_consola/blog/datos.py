perfil_autor = {
    "nombre": "Camilo",
    "bio": "Estudiante de programación y entusiasta del desarrollo y la tecnología.",
    "especialidad": "Python y desarrollo web",
    "redes_sociales": ["@camilo_dev", "@camilo_py"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "Git", "Backend", "Bases de Datos", "Python"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "Post incompleto de prueba",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "publicado"
    }
]