import datetime
from app.shared.database import connection

connect = connection.Connect_SQLite()
database = connect[0]
cursor = connect[1]

#cursor.execute("USE agrofit;")

class Message:

    def __init__(self, names, email, title, message):
        self.names = names
        self.email = email
        self.title = title
        self.message = message

    def send(self):

        send_date = datetime.datetime.now()

        sql = """
            INSERT INTO mensajes_contacto (
                nombres_remitente,
                correo_remitente,
                titulo_mensaje,
                contenido_mensaje,
                fecha_envio,
                id_estado_contacto_fk
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

        data = (
            self.names,
            self.email,
            self.title,
            self.message,
            send_date,
            1
        )

        try:
            cursor.execute(sql, data)
            database.commit()

            result = [cursor.rowcount, self]

        except Exception as error:
            database.rollback()
            print(f"\n✕ Error al enviar el mensaje: {error}")
            result = [0, self]

        return result