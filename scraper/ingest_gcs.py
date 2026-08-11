import json
import os
from datetime import datetime, timezone
from scraper import extract_laliga_pipeline

def upload_to_data_lake_emulator():
    payload = extract_laliga_pipeline()
    
    # Estructura del Data Lake particionada por fecha: data_lake/raw/YYYY-MM-DD/
    date_folder = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    timestamp_str = int(datetime.now(timezone.utc).timestamp())
    
    base_data_lake_dir = os.path.expanduser("~/laliga-gcp-proyecto/data_lake")
    target_dir = os.path.join(base_data_lake_dir, "raw", date_folder)
    os.makedirs(target_dir, exist_ok=True)
    
    file_name = f"laliga_standings_{timestamp_str}.json"
    full_path = os.path.join(target_dir, file_name)
    
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        
    print("=" * 65)
    print(" 🚀 INGESTA A DATA LAKE COMPLETADA CON ÉXITO ")
    print("=" * 65)
    print(f" 📍 Ruta Local Data Lake: {full_path}")
    print(f" 📊 Tamaño del Snapshot: {os.path.getsize(full_path)} bytes")
    print("=" * 65)

if __name__ == "__main__":
    upload_to_data_lake_emulator()
