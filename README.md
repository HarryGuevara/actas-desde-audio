# Actas desde audio (Python + Whisper + DOCX)

![Python](https://img.shields.io/badge/python-3.10-blue)
![MIT License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-working-success)

Convierte **audios de reuniones** en **actas formales editables** en minutos.


## 🚀 Flujo
1. Audio (.m4a/.mp3) → 2. Transcripción (Whisper) → 3. Limpieza → 4. DOCX

![Flujo del proyecto](docs/flujo.png)

## 📦 Requisitos
- Python 3.10+
- ffmpeg instalado
- Paquetes:
  ```bash
  pip install -r requirements.txt
