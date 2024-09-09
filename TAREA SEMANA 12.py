# Clase Libro con atributos inmutables para título y autor
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla inmutable (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[0]} por {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario para gestionar los préstamos de libros
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros_prestados(self):
        if self.libros_prestados:
            return "\n".join([str(libro) for libro in self.libros_prestados])
        return "No tiene libros prestados."

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca que gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y Usuario como valor
        self.ids_usuarios = set()  # Conjunto para asegurarse de que los ID de usuario sean únicos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.datos[0]}' añadido.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está registrado.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")
        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.datos[0]}' prestado a {usuario.nombre}.")
        else:
            print(f"El usuario o el libro no existen.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = usuario.devolver_libro(isbn)
            if libro:
                self.libros[isbn] = libro
                print(f"Libro '{libro.datos[0]}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario no tiene prestado un libro con ISBN {isbn}.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def buscar_libros(self, filtro, valor):
        resultados = []
        for libro in self.libros.values():
            if (filtro == "titulo" and valor.lower() in libro.datos[0].lower()) or \
                    (filtro == "autor" and valor.lower() in libro.datos[1].lower()) or \
                    (filtro == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].listar_libros_prestados()
        else:
            return "Usuario no encontrado."


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Creación de una instancia de la clase Libro
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "001")
    print(libro1)

    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "002")
    print(libro2)

    libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", "003")
    print(libro3)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Carlos García", 101)
    usuario2 = Usuario("Lucía Pérez", 102)

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro(101, "001")  # Prestar Don Quijote a Carlos
    biblioteca.prestar_libro(102, "003")  # Prestar El Hobbit a Lucía

    # Listar libros prestados de un usuario
    print("\nLibros prestados a Carlos:")
    print(biblioteca.listar_libros_prestados_usuario(101))

    # Devolver un libro
    biblioteca.devolver_libro(101, "001")  # Carlos devuelve Don Quijote

    # Buscar libros por autor
    print("\nBuscar libros por autor 'George Orwell':")
    resultados = biblioteca.buscar_libros("autor", "George Orwell")
    for libro in resultados:
        print(libro)