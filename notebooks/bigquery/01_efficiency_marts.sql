-- ====================================================================
-- BigQuery Analytics Mart: Financial Efficiency Index (FEI) & ROI
-- ====================================================================

-- 1. Calcular el Ranking Financiero de Presupuesto (1 = Mayor plantilla)
WITH financial_ranking AS (
    SELECT
        team_id,
        team_name,
        rank AS sporting_rank,
        points,
        goals_for,
        goals_against,
        squad_market_value_eur,
        -- Asigna el puesto financiero del 1 al 20 según el valor del equipo
        DENSE_RANK() OVER (ORDER BY squad_market_value_eur DESC) AS budget_rank
    FROM `laliga_raw.raw_standings`
),

-- 2. Calcular los Puntos Esperados según la inversión/presupuesto
expected_performance AS (
    SELECT
        *,
        (budget_rank - sporting_rank) AS rank_delta, -- Positivo = Sobre-rendimiento respecto a presupuesto
        ROUND(95.0 - (budget_rank - 1) * 3.3, 1) AS expected_points_by_budget
    FROM financial_ranking
)

-- 3. Calcular Métricas de Eficiencia e Índice FEI
SELECT
    team_id,
    team_name,
    sporting_rank,
    budget_rank,
    rank_delta,
    points,
    expected_points_by_budget,
    (points - expected_points_by_budget) AS points_above_expected,
    squad_market_value_eur,
    
    -- Coste por Punto en Euros (€/Punto)
    ROUND(squad_market_value_eur / NULLIF(points, 0), 2) AS cost_per_point_eur,
    
    -- Financial Efficiency Index (FEI): Base 100 = Rendimiento exacto según presupuesto
    ROUND((points / NULLIF(expected_points_by_budget, 0)) * 100, 1) AS financial_efficiency_index,
    
    -- Clasificación en Cuadrantes Ejecutivos
    CASE 
        WHEN points >= 65 AND squad_market_value_eur <= 300000000 THEN 'Bargain Overperformer (High ROI)'
        WHEN points >= 75 AND squad_market_value_eur > 500000000 THEN 'Elite Heavyweight (Expected High)'
        WHEN points < 55 AND squad_market_value_eur > 150000000 THEN 'Underperforming Wasteful (Low ROI)'
        ELSE 'Modest Balanced Competitor'
    END AS efficiency_quadrant
FROM expected_performance
ORDER BY financial_efficiency_index DESC;
