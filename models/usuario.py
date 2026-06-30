class Usuario:

    # Constructor
    def __init__(self, usuario_id, usuario_nombre, usuario_matricula, usuario_email, usuario_carrera):
        self.usuario_id = usuario_id
        self.usuario_nombre = usuario_nombre
        self.usuario_email = usuario_email
        self.usuario_carrera = usuario_carrera
        self.usuario_matricula = usuario_matricula
    
    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def mostrar_info(self):
        return f"Usuario ID: {self.id_usuario}, Nombre: {self.nombre}, Matricula: {self.matricula} ,Email: {self.email }, Carrera: {self.carrera}, Activo: {'Sí' if self.activo else 'No'}"
    
class Usuario_eliminar:

    # Constructor
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id