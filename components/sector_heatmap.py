import streamlit as st
import pandas as pd
import plotly.express as px


def render_sector_heatmap(valuation):

    multiplier = valuation / 450

    sectors = pd.DataFrame({

        "Sector": [

            "Aerospace",
            "Defense",
            "Satellite",
            "AI",
            "Technology",
            "Telecom",
            "EV",
            "Legacy Aero"

        ],

        "Impact": [

            18 * multiplier,
            11 * multiplier,
            22 * multiplier,
            8 * multiplier,
            6 * multiplier,
            -4 * multiplier,
            -2 * multiplier,
            -9 * multiplier

        ],

        "Reason": [

            "Commercial launch boom",

            "Government partnerships",

            "Starlink expansion",

            "AI infrastructure demand",

            "Capital inflows",

            "Subscriber pressure",

            "Capital rotation",

            "Disruption risk"

        ]

    })

    fig = px.treemap(

        sectors,

        path=["Sector"],

        values=abs(sectors["Impact"]),

        color="Impact",

        color_continuous_scale=[

            "#EF4444",

            "#1E293B",

            "#10B981"

        ],

        color_continuous_midpoint=0,

        hover_data=[

            "Reason"

        ]

    )

    fig.update_layout(

        height=500,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(

            color="white",

            size=13

        ),

        margin=dict(

            l=0,

            r=0,

            t=40,

            b=0

        )

    )

    st.subheader("🛰 Sector Impact Map")

    st.caption(

        "Projected impact across major US sectors"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )