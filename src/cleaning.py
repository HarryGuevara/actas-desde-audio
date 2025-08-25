def limpieza_basica(texto: str) -> str:
    if not texto:
        return ""
    texto = texto.replace("  ", " ").strip()
    return texto
