import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

def run_interactive_simulation():
    print("=" * 70)
    print("  SIMULADOR INTERACTIVO DE FICHAJES E INTELIGENCIA ARTIFICIAL ")
    print("=" * 70)
    
    np.random.seed(42)
    n_samples = 300
    ages = np.random.randint(17, 34, n_samples)
    minutes = np.random.randint(400, 3100, n_samples)
    goals = np.random.poisson(lam=5, size=n_samples)
    assists = np.random.poisson(lam=3, size=n_samples)
    team_fei = np.random.uniform(60.0, 140.0, n_samples)
    
    youth_factor = np.maximum(0, (24 - ages) * 3.5)
    perf_factor = (goals * 2.8 + assists * 2.0) * (minutes / 1800.0)
    fei_boost = (team_fei - 100.0) * 0.35
    reval = np.clip(youth_factor + perf_factor + fei_boost + np.random.normal(0, 6.0, n_samples), -25.0, 180.0)
    
    X = pd.DataFrame({"age": ages, "minutes_played": minutes, "goals": goals, "assists": assists, "team_fei": team_fei})
    model = GradientBoostingRegressor(n_estimators=80, learning_rate=0.08, max_depth=3, random_state=42)
    model.fit(X, reval)
    
    teams_fei = {
        "Girona FC": 103.2,
        "Real Madrid": 100.0,
        "FC Barcelona": 92.7,
        "Athletic Club": 83.1,
        "Atlético de Madrid": 86.0,
        "Sevilla FC": 59.8
    }

    player_name = "Nico Williams"
    age = 22
    minutes_played = 2300
    goals = 10
    assists = 12
    transfer_fee_eur_m = 58.0
    target_team = "Girona FC"
    
    selected_fei = teams_fei.get(target_team, 100.0)
    
    input_data = pd.DataFrame([{
        "age": age,
        "minutes_played": minutes_played,
        "goals": goals,
        "assists": assists,
        "team_fei": selected_fei
    }])
    
    predicted_reval_pct = model.predict(input_data)[0]
    future_value_m = transfer_fee_eur_m * (1 + predicted_reval_pct / 100.0)
    value_gain_m = future_value_m - transfer_fee_eur_m
    
    if transfer_fee_eur_m > 50 or age > 29:
        risk_level = " RIESGO ALTO (Elevado Compromiso de Capital)"
    elif transfer_fee_eur_m > 25 or age > 27:
        risk_level = " RIESGO MEDIO (Inversión Moderada)"
    else:
        risk_level = " RIESGO BAJO (Alto Potencial Patrimonio)"

    print(f"  Jugador Evaluado: {player_name}")
    print(f"  Edad: {age} años |  Minutos: {minutes_played} |  Goles: {goals} |  Asistencias: {assists}")
    print(f"  Precio Fichaje: €{transfer_fee_eur_m:.1f}M")
    print(f"  Equipo Destino: {target_team} (Índice Eficiencia FEI: {selected_fei}%)")
    print("-" * 70)
    print(f"  Predicción Revalorización a 1 Año: {predicted_reval_pct:+.1f}%")
    print(f"  Valor Estimado Futuro: €{future_value_m:.1f}M (Ganancia Est: €{value_gain_m:+.1f}M)")
    print(f"  Perfil de Riesgo Financiero: {risk_level}")
    print("=" * 70)

if __name__ == "__main__":
    run_interactive_simulation()
