from app.cli.menus.menu import show_menu

# Componentes
from app.shared.components.loading import loading, typewriter
from app.shared.components.clear import clear
from app.shared.database.schema import init_db

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
