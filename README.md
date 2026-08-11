# Análisis de Eficiencia Financiera y ROI en LaLiga

## ¿En qué consiste el proyecto?
Este proyecto analiza la relación entre el rendimiento deportivo de los equipos de LaLiga EA Sports (Temporada 2023/2024) y su inversión económica en plantilla. Su objetivo es medir la eficiencia presupuestaria mediante el Financial Efficiency Index (FEI) y ofrecer un Simulador de Revalorización de Fichajes que evalúa el ROI futuro y el riesgo financiero de nuevos jugadores mediante Inteligencia Artificial.

## ¿Cómo se ha realizado?
El proyecto sigue un flujo de datos modular estructurado en tres fases:

1. **Extracción e Ingesta (Python)**: Recolección automatizada de datos deportivos y financieros oficiales de LaLiga 23/24 almacenados en formato JSON.
2. **Data Warehouse (BigQuery SQL)**: Transformación analítica mediante SQL para calcular el coste por punto (€/Punto) y clasificar el rendimiento de cada club (ej. Girona FC como líder de eficiencia con FEI 103.2%).
3. **Motor de IA y Simulador (Machine Learning)**: Modelo de regresión (*Gradient Boosting*) y simulador predictivo que estima la revalorización a 12 meses y el nivel de riesgo financiero de un fichaje evaluando el rendimiento individual del jugador y la eficiencia del equipo.

## Evaluación del Modelo de IA
* **Precisión (Coeficiente de Determinación R²)**: 0.8296
* **Error Medio Absoluto (MAE)**: ±5.30%
* **Variables Más Influyentes (Feature Importance)**:
  1. Minutos jugados (`minutes_played`): 34.0%
  2. Edad del jugador (`age`): 31.5%
  3. Goles marcados (`goals`): 22.0%
  4. Eficiencia del equipo (`team_fei`): 6.3%

## Tecnologías Utilizadas
* **Lenguajes**: Python 3.11, SQL
* **Librerías**: Pandas, Scikit-Learn, Requests, BeautifulSoup4
* **Conceptos de Nube / Infraestructura**: Data Lake Storage, BigQuery DW, Machine Learning

## Estructura del Repositorio
* `scraper/`: Extracción e ingesta de datos.
* `bigquery/`: Consultas SQL y vistas analíticas del Data Warehouse.
* `ml/`: Entrenamiento del modelo de IA y script del Simulador de Revalorización (`predict_custom_player.py`).
