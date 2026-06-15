import pandas as pd
import plotly.express as px
import streamlit as st

from services.market_api import get_market_caps


def render_bubble_chart(valuation):

    # -----------------------------
    # Live market data
    # -----------------------------

    df = get_market_caps()

    # -----------------------------
    # Simulated SpaceX IPO
    # -----------------------------

    spacex = pd.DataFrame(

        {

            "Company": ["SpaceX"],

            "Ticker": ["SPACEX"],

            "Sector": ["Space"],

            "Market Cap": [f"${valuation}B"],

            "Raw Market Cap": [valuation * 1_000_000_000]

        }

    )

    # -----------------------------
    # Combine
    # -----------------------------

    df = pd.concat(

        [

            df,

            spacex

        ],

        ignore_index=True

    )

    # -----------------------------
    # Bubble Layout
    # -----------------------------

    layout = pd.read_csv(

        "data/bubble_layout.csv"

    )

    df = df.merge(

        layout,

        on="Company",

        how="left"

    )

    st.write(df)

    # -----------------------------
    # Bubble Plot
    # -----------------------------

    fig = px.scatter(

        df,

        x="x",

        y="y",

        size="Raw Market Cap",

        color="Sector",

        text="Company",

        hover_name="Company",

        hover_data={

            "Ticker": True,

            "Sector": True,

            "Raw Market Cap": ":,.0f",

            "x": False,

            "y": False

        },

        size_max=120

    )

    fig.update_traces(

        textposition="middle center",

        textfont_size=13,

        marker=dict(
            opacity=0.82,
            sizemode="area",
            line=dict(
                width=3,
                color="rgba(255,255,255,.25)"
            )
        )

    )

    fig.update_layout(

        height=700,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        showlegend=True,

        margin=dict(

            l=0,

            r=0,

            t=20,

            b=0

        ),

        transition=dict(

            duration=700

        )

    )

    fig.update_xaxes(

        visible=False,

        range=[0, 100]

    )

    fig.update_yaxes(

        visible=False,

        range=[0, 100]

    )

    st.subheader("🪐 Market Universe")

    st.caption(

        "Bubble size represents live market capitalization. SpaceX is simulated."

    )

    st.plotly_chart(

        fig,

        width="stretch"

    )