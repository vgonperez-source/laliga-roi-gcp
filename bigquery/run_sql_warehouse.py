import os
import glob
import json
import sqlite3
import pandas as pd

def run_bigquery_sql_pipeline():
    # 1. Localizar el último snapshot JSON guardado en el Data Lake
    data_lake_dir = os.path.expanduser("~/laliga-gcp-proyecto/data_lake/raw/*/*.json")
    files = glob.glob(data_lake_dir)
    
    if not files:
        print("❌ No se encontraron archivos JSON en el Data Lake. Ejecuta primero ingest_gcs.py")
        return
        
    latest_file = max(files, key=os.path.getctime)
    print(f"📖 Leyendo snapshot del Data Lake: {latest_file}")
    
    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    df_teams = pd.DataFrame(data["standings"])
    
    # 2. Iniciar motor SQL (Simulador de BigQuery)
    conn = sqlite3.connect(":memory:")
    df_teams.to_sql("raw_standings", conn, if_exists="replace", index=False)
    
    # 3. Cargar y ejecutar la consulta SQL de 01_efficiency_marts.sql
    with open("01_efficiency_marts.sql", "r", encoding="utf-8") as f:
        raw_sql = f.read()
        
    # Adaptación de sintaxis para motor SQL
    clean_sql = raw_sql.replace("`laliga_raw.raw_standings`", "raw_standings")
    
    print("⚡ Ejecutando transformaciones analíticas en SQL...")
    df_results = pd.read_sql(clean_sql, conn)
    
    print("\n" + "=" * 80)
    print(" 🏆 RANKING DE EFICIENCIA FINANCIERA EN LALIGA (DATA WAREHOUSE) ")
    print("=" * 80)
    
    # Formatear columnas para visualización en pantalla
    df_show = df_results[["team_name", "sporting_rank", "budget_rank", "rank_delta", "points", "cost_per_point_eur", "financial_efficiency_index", "efficiency_quadrant"]].copy()
    df_show["cost_per_point_m€"] = (df_show["cost_per_point_eur"] / 1e6).round(2)
    df_show = df_show.drop(columns=["cost_per_point_eur"])
    
    print(df_show.to_string(index=False))
    print("=" * 80)

if __name__ == "__main__":
    run_bigquery_sql_pipeline()
