"""
Menú del Entrenador - AgroFit
Conectado a la base de datos agrofit.
"""

from features.users.coach import (
    show_my_profile,
    my_learners,
    manage_routines,
    manage_physical_evaluations,
    learner_progress,
)


def coach_menu(user):
    """
    Menú principal del rol Entrenador.
    user: resultado de authenticate() — tupla con datos del usuario.
    """
    while True:
        print("""
===================================================
                 MENÚ ENTRENADOR
===================================================

        1. Mi perfil
        2. Mis aprendices
        3. Rutinas de entrenamiento
        4. Evaluaciones físicas
        5. Progreso de aprendices
        6. Cerrar sesión

===================================================
        """)

        option = input("\n¿Qué deseas hacer?: ").strip()

        if option == "1":
            show_my_profile(user)

        elif option == "2":
            my_learners(user)

        elif option == "3":
            manage_routines(user)

        elif option == "4":
            manage_physical_evaluations(user)

        elif option == "5":
            learner_progress(user)

        elif option == "6":
            print("\n✓ Sesión cerrada.")
            break

        else:
            print("\n✕ Opción no válida.")

        input("\nPresione Enter para continuar...")
