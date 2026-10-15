import app.features.contact.model as model
from app.shared.utils import validators as val

class contact:

    def send_message(self):
        print("\n========================================================")
        print("                   CONTÁCTANOS                          ")
        print("========================================================")
        print("""
Servicio Nacional de Aprendizaje (SENA)
Popayán, Regional Cauca, Sede Centro Agropecuario.

Teléfono : +57 987-6543-120
Horario  : Lunes a Viernes, 10AM a 6PM
Correo   : gimnasio.agrofit@sena.edu.co

Escríbenos a nuestro correo y con gusto te ayudaremos.
========================================================
        """)

        print("\n--- Formulario de Contacto ---\n")

        # 1. Nombres
        names = val.validate_text("\n¿Cuáles son tus nombres?: ")

        # 2. Email
        email = val.validate_email(
        message="\nDigita tu email: ",
        required_domain=False)

        # 3. Título del mensaje
        title = input("\nDigita el título del mensaje: ").strip()
        while not title:
            print("\n✕ El título no puede estar vacío.")
            title = input("\nDigita el título del mensaje: ").strip()

        # 4. Mensaje
        message = input("\nDigita el mensaje: ").strip()
        while not message:
            print("\n✕ El mensaje no puede estar vacío.")
            message = input("\nDigita el mensaje: ").strip()

        # Crear objeto y enviar
        msg = model.Message(names, email, title, message)
        result = msg.send()

        if result[0] >= 1:
            print("\n========================================================")
            print("              MENSAJE ENVIADO CON ÉXITO                 ")
            print("========================================================")
            print(f"""
✓ Nombres : {result[1].names}
✓ Email   : {result[1].email}
✓ Título  : {result[1].title}
✓ Mensaje : {result[1].message}

¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.
========================================================
            """)
        else:
            print("\n✕ No se pudo enviar el mensaje. Inténtalo más tarde...")

        input("\nPresione Enter para continuar...")
