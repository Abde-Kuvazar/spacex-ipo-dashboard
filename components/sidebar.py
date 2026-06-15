import streamlit as st


def render_sidebar():

    st.sidebar.markdown("# 🚀 Mission Control")

    valuation = st.sidebar.slider(

        "Hypothetical SpaceX Valuation ($B)",

        min_value=100,

        max_value=2000,

        value=450,

        step=25

    )

    float_pct = st.sidebar.slider(

        "Public Float (%)",

        min_value=5,

        max_value=50,

        value=15,

        step=1

    )

    market_regime = st.sidebar.selectbox(

        "Market Regime",

        [

            "Bull",

            "Neutral",

            "Bear"

        ]

    )

    st.sidebar.divider()

    st.sidebar.caption(

        "Hypothetical model • Educational use only"

    )

    return valuation, float_pct, market_regime