from app.cli.menus.learner import learner_menu
from app.cli.menus.coach import coach_menu
from app.cli.menus.staff import staff_menu
from app.cli.menus.admin import admin_menu


def show_role_menu(role, user):

    menus = {1: learner_menu, 2: coach_menu, 3: staff_menu, 4: admin_menu}

    menu = menus.get(role)

    if menu:
        menu(user)
    else:
        print("\n✕ El usuario no tiene un rol válido.")
