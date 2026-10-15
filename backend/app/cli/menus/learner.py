"""
Menú del Aprendiz - AgroFit
Conectado a la base de datos agrofit.
"""

from app.features.modules.learner import (
    show_my_profile,
    my_physical_evaluations,
    my_routines,
    my_progress,
)


def learner_menu(user):
    """
    Menú principal del rol Aprendiz.
    user: resultado de authenticate() — tupla con datos del usuario.
    """
    while True:
        print("""
===================================================
                 MENÚ APRENDIZ
===================================================

        1. Mi perfil
        2. Evaluaciones físicas
        3. Rutinas de entrenamiento
        4. Mi progreso
        5. Cerrar sesión

===================================================
        """)

        option = input("\n¿Qué deseas hacer?: ").strip()

        if option == "1":
            show_my_profile(user)

        elif option == "2":
            my_physical_evaluations(user)

        elif option == "3":
            my_routines(user)

        elif option == "4":
            my_progress(user)

        elif option == "5":
            print("\n✓ Sesión cerrada.")
            break

        else:
            print("\n✕ Opción no válida.")

        input("\nPresione Enter para continuar...")
