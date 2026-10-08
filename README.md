# Análisis de Eficiencia Financiera y ROI en LaLiga

## Contexto del Proyecto
Este proyecto analiza la relación entre el rendimiento deportivo de los equipos de LaLiga EA Sports (Temporada 2023/2024) y su inversión económica en plantilla. Su objetivo es medir la eficiencia presupuestaria mediante el Financial Efficiency Index (FEI) y ofrecer un Simulador de Revalorización de Fichajes que evalúa el ROI futuro y el riesgo financiero de nuevos jugadores mediante Inteligencia Artificial.

## Arquitectura y Metodología
El análisis se ha dividido en tres fases principales de manera secuencial:

- Extracción e Ingesta: Recolección automatizada de datos deportivos y financieros oficiales de LaLiga 23/24 almacenados en formato JSON usando Python.
- Data Warehouse: Transformación analítica mediante SQL en BigQuery para calcular el coste por punto (€/Punto) y clasificar el rendimiento de cada club (ej. Girona FC como líder de eficiencia con FEI 103.2%).
- Machine Learning predictivo: Desarrollo de un modelo de regresión (Gradient Boosting) y simulador predictivo que estima la revalorización a 12 meses y el nivel de riesgo financiero de un fichaje evaluando el rendimiento individual del jugador y la eficiencia del equipo.

## Resultados Clave
Los resultados obtenidos aportan valor para la toma de decisiones financieras y de fichajes en los clubes:

- Precisión predictiva: El modelo alcanzó un Coeficiente de Determinación (R²) de 0.8296 y un Error Medio Absoluto (MAE) de ±5.30%.
- Variables influyentes: Las métricas con mayor peso en el algoritmo son los minutos jugados (34.0%), la edad del jugador (31.5%), los goles marcados (22.0%) y la eficiencia del equipo (6.3%).

## Reproducibilidad
Para ejecutar este código en tu propio equipo, solo necesitas seguir estos pasos:
1. Clonar este repositorio.
2. Instalar las dependencias ejecutando el comando pip install -r requirements.txt.
3. Ejecutar los scripts que están dentro de la carpeta notebooks, empezando por la extracción de datos y finalizando con el modelo de IA.
