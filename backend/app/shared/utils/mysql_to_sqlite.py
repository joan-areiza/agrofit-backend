import re


def mysql_to_sqlite(sql_script: str) -> str:
    # 1. Eliminar sentencias de base de datos MySQL
    sql_script = re.sub(
        r"CREATE DATABASE.*?;|USE.*?;|SHOW DATABASES;?|SHOW TABLES;?",
        "",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 2. Convertir int AUTO_INCREMENT a INTEGER PRIMARY KEY AUTOINCREMENT
    sql_script = re.sub(
        r"`?(\w+)`?\s+int\(\d+\)\s+NOT\s+NULL\s+AUTO_INCREMENT",
        r"`\1` INTEGER PRIMARY KEY AUTOINCREMENT",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 3. Eliminar definiciones de PRIMARY KEY al final de las tablas (evita duplicados)
    sql_script = re.sub(
        r",\s*PRIMARY\s+KEY\s*\([^)]+\)", "", sql_script, flags=re.IGNORECASE
    )

    # 4. Eliminar opciones de tabla de MySQL (ENGINE=InnoDB, DEFAULT CHARSET, etc.)
    sql_script = re.sub(
        r"ENGINE\s*=\s*\w+.*?;", ";", sql_script, flags=re.IGNORECASE
    )

    # 5. Eliminar definición de índices KEY locales de MySQL
    sql_script = re.sub(
        r",\s*(UNIQUE\s+)?KEY\s+`?\w+`?\s*\([^)]+\)",
        "",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 6. Cambiar INSERT INTO por INSERT OR IGNORE INTO para evitar errores de claves duplicadas
    sql_script = re.sub(
        r"INSERT INTO", "INSERT OR IGNORE INTO", sql_script, flags=re.IGNORECASE
    )

    return sql_script