from cli.menus.menu import show_menu

# Componentes
from core.components.loading import loading, typewriter
from core.components.clear import clear
from core.database.schema import init_db

# Crear estructura de BD en backend/data/agrofit.db
init_db()

clear()  # Limpia la pantalla
loading("Iniciando el programa AgroFit")

# Llamar a la función
typewriter(r"""
  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$ /$$$$$$$$
 /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$_____/|_  $$_/|__  $$__/
| $$  \ $$| $$  \__/| $$  \ $$| $$  \ $$| $$        | $$     | $$   
| $$$$$$$$| $$ /$$$$| $$$$$$$/| $$  | $$| $$$$$     | $$     | $$   
| $$__  $$| $$|_  $$| $$__  $$| $$  | $$| $$__/     | $$     | $$   
| $$  | $$| $$  \ $$| $$  \ $$| $$  | $$| $$        | $$     | $$   
| $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$       /$$$$$$   | $$   
|__/  |__/ \______/ |__/  |__/ \______/ |__/      |______/   |__/                                                                       
""")

show_menu()
