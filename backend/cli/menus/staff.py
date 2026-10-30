"""
Menú del Funcionario - AgroFit
Conectado a la base de datos agrofit.
"""

from features.users.staff import (
    show_my_profile,
    consult_learners,
    view_physical_evaluations,
    generate_reports,
)


def staff_menu(user):
    """
    Menú principal del rol Funcionario.
    user: resultado de authenticate() — tupla con datos del usuario.
    """
    while True:
        print("""
===================================================
                MENÚ FUNCIONARIO
===================================================

        1. Mi perfil
        2. Consultar aprendices
        3. Evaluaciones físicas
        4. Reportes
        5. Cerrar sesión

===================================================
        """)

        option = input("\n¿Qué deseas hacer?: ").strip()

        if option == "1":
            show_my_profile(user)

        elif option == "2":
            consult_learners(user)

        elif option == "3":
            view_physical_evaluations(user)

        elif option == "4":
            generate_reports(user)

        elif option == "5":
            print("\n✓ Sesión cerrada.")
            break

        else:
            print("\n✕ Opción no válida.")

        input("\nPresione Enter para continuar...")
