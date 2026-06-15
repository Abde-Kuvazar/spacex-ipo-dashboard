import streamlit as st

from utils.global_css import load_global_css
from utils.theme import load_theme

from components.sidebar import render_sidebar

from components.hero import render_hero

from components.metric_cards import render_metrics

from components.bubble_chart import render_bubble_chart

from components.valuation_simulator import render_valuation_simulator

from components.capital_flow import render_capital_flow

from components.sector_heatmap import render_sector_heatmap

from components.historical_timeline import render_historical_timeline

from components.winners_losers import render_winners_losers

from components.scenario_engine import render_scenario_engine

from services.index_engine import calculate_index_weights

from services.prediction_engine import predict_week1_return

from services.capital_flow_engine import estimate_capital_flow

st.set_page_config(

    page_title="SpaceX IPO Intelligence",

    page_icon="🚀",

    layout="wide"

)

load_theme()


load_global_css()
valuation, float_pct, market_regime = render_sidebar()

weights = calculate_index_weights(

    valuation,

    float_pct

)

prediction = predict_week1_return(

    valuation,

    market_regime

)

capital = estimate_capital_flow(

    weights["public_value"]

)
render_hero()

render_metrics(

    valuation,

    weights["public_value"],

    weights["sp_weight"],

    prediction

)

render_bubble_chart(valuation)

render_valuation_simulator(

    valuation,

    float_pct

)

render_capital_flow(
    valuation,
    float_pct
)

render_sector_heatmap(
    valuation
)

render_historical_timeline()

render_winners_losers()

render_scenario_engine()