import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def train_laliga_player_revaluation_model():
    print("=" * 65)
    print(" 🧠 ENTRENANDO MODELO DE IA: PREDICCIÓN DE REVALORIZACIÓN ")
    print("=" * 65)
    
    np.random.seed(42)
    n_samples = 300
    
    # 1. Generar Dataset de entrenamiento (Rendimiento individual + FEI de equipo)
    ages = np.random.randint(17, 34, n_samples)
    minutes = np.random.randint(400, 3100, n_samples)
    goals = np.random.poisson(lam=5, size=n_samples)
    assists = np.random.poisson(lam=3, size=n_samples)
    team_fei = np.random.uniform(60.0, 140.0, n_samples)
    
    # Target: Revalorización % condicionada por juventud, minutos, goles y FEI de equipo
    youth_factor = np.maximum(0, (24 - ages) * 3.5)
    perf_factor = (goals * 2.8 + assists * 2.0) * (minutes / 1800.0)
    fei_boost = (team_fei - 100.0) * 0.35
    
    revaluation_pct = youth_factor + perf_factor + fei_boost + np.random.normal(0, 6.0, n_samples)
    revaluation_pct = np.clip(revaluation_pct, -25.0, 180.0)
    
    df = pd.DataFrame({
        "age": ages,
        "minutes_played": minutes,
        "goals": goals,
        "assists": assists,
        "team_fei": team_fei,
        "revaluation_pct": revaluation_pct
    })
    
    # 2. Separar características (X) y objetivo (y)
    X = df[["age", "minutes_played", "goals", "assists", "team_fei"]]
    y = df["revaluation_pct"]
    
    # Dividir 80% entrenamiento / 20% test
    split = int(0.8 * len(df))
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]
    
    # 3. Entrenar modelo Gradient Boosting
    model = GradientBoostingRegressor(n_estimators=80, learning_rate=0.08, max_depth=3, random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    
    print(f" 📊 Tamaño del Dataset: {len(df)} futbolistas")
    print(f" 🎯 Precisión del Modelo (R² Score): {r2:.4f}")
    print(f" 📉 Error Medio Absoluto (MAE): ±{mae:.2f}%")
    print("-" * 65)
    print(" 🔍 IMPORTANCIA DE LAS VARIABLES (FEATURE IMPORTANCE):")
    
    importances = pd.DataFrame({
        "Variable": X.columns,
        "Importancia (%)": (model.feature_importances_ * 100).round(2)
    }).sort_values("Importancia (%)", ascending=False)
    
    for _, row in importances.iterrows():
        print(f"   • {row['Variable']:<18}: {row['Importancia (%)']}%")
        
    print("=" * 65)
    
    # 4. Inferencia: Simulación de un fichaje real (Ejemplo: Joven promesa a un equipo de alto FEI)
    sample_candidate = pd.DataFrame([{
        "age": 20,
        "minutes_played": 2200,
        "goals": 8,
        "assists": 6,
        "team_fei": 103.2 # FEI del Girona FC
    }])
    
    pred_growth = model.predict(sample_candidate)[0]
    print("\n 🔮 SIMULACIÓN DE FICHAJE (EJEMPLO PROMESAS):")
    print(f" Candidate 20 años | 8 Goles | 6 Asistencias | Fichado por Girona FC (FEI 103.2%)")
    print(f" 📈 Predicción de Revalorización a 1 Año: +{pred_growth:.1f}%")
    print("=" * 65)

if __name__ == "__main__":
    train_laliga_player_revaluation_model()
