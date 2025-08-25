import os
from src.transcribe import transcribir_audio
from src.cleaning import limpieza_basica
from src.generate_docx import crear_acta_docx

AUDIO_PATH = "data/audio/reunion.m4a"
TXT_PATH = "data/outputs/transcripcion.txt"
TXT_CORR = "data/outputs/transcripcion_corregida.txt"
DOCX_PATH = "data/outputs/ACTA_15.docx"

def ensure_dirs():
    os.makedirs("data/outputs", exist_ok=True)

def main():
    ensure_dirs()
    texto = transcribir_audio(AUDIO_PATH, modelo="base", idioma="es")
    with open(TXT_PATH, "w", encoding="utf-8") as f:
        f.write(texto)
    texto_corregido = limpieza_basica(texto)
    with open(TXT_CORR, "w", encoding="utf-8") as f:
        f.write(texto_corregido)
    out = crear_acta_docx(contenido=texto_corregido, output_path=DOCX_PATH)
    print(f"✅ Acta generada en: {out}")

if __name__ == "__main__":
    main()
