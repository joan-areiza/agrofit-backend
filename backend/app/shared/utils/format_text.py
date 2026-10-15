import unicodedata


def format_text(text: str) -> str:
    """Limpia el texto quitando tildes, mayúsculas y espacios iniciales/finales."""
    if not text:
        return ""

    # 1. Normalizar Unicode a NFD (separa la letra base del acento)
    decomposed_text = unicodedata.normalize("NFD", text)

    # 2. Filtrar caracteres de categoría 'Mn' (Non-Spacing Mark / Tildes)
    unaccented_text = "".join(
        c for c in decomposed_text if unicodedata.category(c) != "Mn"
    )

    # 3. Pasar a minúsculas y quitar espacios en los extremos
    return unaccented_text.lower()