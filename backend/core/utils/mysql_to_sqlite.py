import re


def mysql_to_sqlite(sql_script: str) -> str:
    # 1. Eliminar sentencias de base de datos MySQL
    sql_script = re.sub(
        r"CREATE DATABASE.*?;|USE.*?;|SHOW DATABASES;?|SHOW TABLES;?",
        "",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 2. Convertir AUTO_INCREMENT → INTEGER PRIMARY KEY AUTOINCREMENT
    sql_script = re.sub(
        r"`?(\w+)`?\s+int\(\d+\)\s+NOT\s+NULL\s+AUTO_INCREMENT",
        r"`\1` INTEGER PRIMARY KEY AUTOINCREMENT",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 3. Eliminar TODAS las PRIMARY KEY que están al final de la tabla
    sql_script = re.sub(
        r",\s*PRIMARY\s+KEY\s*\([^)]+\)",
        "",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 4. Agregar PRIMARY KEY a las columnas que terminan en _pk y son CHAR/VARCHAR
    #    (estas son las que el paso 2 no tocó)
    def fix_char_pk(match):
        col_def = match.group(0)
        # Solo agregar PRIMARY KEY si aún no lo tiene
        if "PRIMARY KEY" not in col_def.upper():
            return col_def + " PRIMARY KEY"
        return col_def

    sql_script = re.sub(
        r"`((?:cod|id)_\w+_pk)`\s+(char|varchar)\(\d+\)\s+NOT\s+NULL",
        fix_char_pk,
        sql_script,
        flags=re.IGNORECASE,
    )

    # 5. Eliminar opciones de tabla MySQL
    sql_script = re.sub(
        r"ENGINE\s*=\s*\w+.*?;",
        ";",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 6. Eliminar índices KEY
    sql_script = re.sub(
        r",\s*(UNIQUE\s+)?KEY\s+`?\w+`?\s*\([^)]+\)",
        "",
        sql_script,
        flags=re.IGNORECASE,
    )

    # 7. INSERT OR IGNORE
    sql_script = re.sub(
        r"INSERT INTO",
        "INSERT OR IGNORE INTO",
        sql_script,
        flags=re.IGNORECASE,
    )

    return sql_script