import numpy as np
import plotly.graph_objects as go
import streamlit as st


def render_valuation_simulator(valuation, float_pct):

    SP500 = 50000
    NASDAQ = 25000

    sweep = np.linspace(100, 2000, 100)

    sp_weight = (
        sweep * float_pct / 100
    ) / (
        SP500 + sweep * float_pct / 100
    ) * 100

    nasdaq_weight = (
        sweep * float_pct / 100
    ) / (
        NASDAQ + sweep * float_pct / 100
    ) * 100

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=sweep,

            y=sp_weight,

            name="S&P 500",

            line=dict(

                width=4

            )

        )

    )

    fig.add_trace(

        go.Scatter(

            x=sweep,

            y=nasdaq_weight,

            name="Nasdaq",

            line=dict(

                width=4,

                dash="dash"

            )

        )

    )

    fig.add_vline(

        x=valuation,

        line_dash="dash",

        line_width=2

    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=420,

        margin=dict(

            l=0,

            r=0,

            t=20,

            b=0

        )

    )

    st.subheader("📈 IPO Impact Simulator")

    st.plotly_chart(

        fig,

        use_container_width=True

    )