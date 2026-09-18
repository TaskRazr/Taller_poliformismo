class Notificacion:
    def __init__(self, destinatario_id):
        if destinatario_id == "":
            print("Identificador vacío")
        self.destinatario_id = destinatario_id

    def enviar(self, destinatario, mensaje):
        pass


class CorreoElectronico(Notificacion):
    def __init__(self, destinatario_id, correo):
        super().__init__(destinatario_id)
        if "@" not in correo:
            print("Correo inválido")
        self.correo = correo

    def enviar(self, destinatario, mensaje):
        print("Correo electrónico para:", self.correo)
        print("Estimado", destinatario + ",", mensaje)


class SMS(Notificacion):
    def __init__(self, destinatario_id, telefono):
        super().__init__(destinatario_id)
        if len(telefono) < 10:
            print("Teléfono inválido")
        self.telefono = telefono

    def enviar(self, destinatario, mensaje):
        print("SMS para:", self.telefono)
        print(destinatario + ":", mensaje)


class NotificacionApp(Notificacion):
    def __init__(self, destinatario_id):
        super().__init__(destinatario_id)

    def enviar(self, destinatario, mensaje):
        print("Notificación en app para usuario:", self.destinatario_id)
        print(destinatario + ", tienes un nuevo aviso:", mensaje)


def enviar_aviso(notificacion, destinatario, mensaje):
    notificacion.enviar(destinatario, mensaje)


notificaciones = [
    CorreoElectronico("U001", "ana.torres@correo.com"),
    SMS("U002", "3001234567"),
    NotificacionApp("U003"),
]

nombres = ["Ana Torres", "Luis Pérez", "Marta Gómez"]
mensaje = "el examen final se realizará el próximo lunes a las 8:00 a.m."

for i in range(len(notificaciones)):
    enviar_aviso(notificaciones[i], nombres[i], mensaje)
    print()
