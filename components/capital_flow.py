import streamlit as st
import plotly.graph_objects as go


def render_capital_flow(valuation, float_pct):

    public_cap = valuation * float_pct / 100

    passive = public_cap * 0.18
    active = public_cap * 0.30
    retail = public_cap * 0.12
    hedge = public_cap * 0.22
    international = public_cap * 0.18

    labels = [

        "💵 Treasuries",
        "🏦 Cash",
        "📈 Mag 7",
        "👥 Retail",
        "🚀 SpaceX IPO",
        "🛰 Aerospace ETFs",
        "🛡 Defense Stocks"

    ]

    source = [

        0,
        1,
        2,
        3,
        4,
        4

    ]

    target = [

        4,
        4,
        4,
        4,
        5,
        6

    ]

    value = [

        passive,
        active,
        hedge,
        retail,
        public_cap * 0.60,
        public_cap * 0.40

    ]

    fig = go.Figure(

        go.Sankey(

            arrangement="snap",

            node=dict(

                pad=25,

                thickness=22,

                line=dict(

                    color="rgba(255,255,255,.2)",

                    width=1

                ),

                label=labels,

                color=[

                    "#4F46E5",
                    "#0EA5E9",
                    "#7C3AED",
                    "#EC4899",
                    "#F59E0B",
                    "#10B981",
                    "#EF4444"

                ]

            ),

            link=dict(

                source=source,

                target=target,

                value=value,

                color="rgba(125,211,252,.25)"

            )

        )

    )

    fig.update_layout(

        title="🌊 Capital Rotation",

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(

            color="white",

            size=13

        ),

        margin=dict(

            l=0,

            r=0,

            t=50,

            b=0

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )