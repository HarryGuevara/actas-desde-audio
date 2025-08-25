import os
import whisper

def transcribir_audio(audio_path: str, modelo: str = "base", idioma: str = "es") -> str:
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"No se encontró el archivo de audio: {audio_path}")
    print(f"[Transcribir] Cargando modelo Whisper ({modelo})…")
    model = whisper.load_model(modelo)
    print(f"[Transcribir] Transcribiendo: {audio_path}")
    result = model.transcribe(audio_path, language=idioma)
    return result.get("text", "").strip()
