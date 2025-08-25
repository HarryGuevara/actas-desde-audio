# Actas desde audio (Python + Whisper + DOCX)

Convierte **audios de reuniones** en **actas formales editables** en minutos.

## 🚀 Flujo
1. Audio (.m4a/.mp3) → 2. Transcripción (Whisper) → 3. Limpieza → 4. DOCX

## 📦 Requisitos
- Python 3.10+
- ffmpeg instalado
- Paquetes:
  ```bash
  pip install -r requirements.txt
  ```

## ▶️ Uso rápido
1. Coloca tu audio en `data/audio/reunion.m4a`
2. Ejecuta:
   ```bash
   python main.py
   ```
3. Obtendrás:
   - data/outputs/transcripcion.txt
   - data/outputs/transcripcion_corregida.txt
   - data/outputs/ACTA_15.docx
