import streamlit as st
import plotly.graph_objects as go
import numpy as np


def render_scenario_engine():

    st.subheader("🔮 Scenario Analysis")
    st.caption("Explore how different IPO outcomes could reshape market expectations.")

    bull, base, bear = st.tabs(

        [

            "🐂 Bull",

            "⚖️ Base",

            "🐻 Bear"

        ]

    )

    scenarios = {

        "Bull": {

            "valuation": 500,

            "week": "+18%",

            "demand": "Very High",

            "growth": 0.22,

            "color": "#22C55E"

        },

        "Base": {

            "valuation": 450,

            "week": "+8%",

            "demand": "High",

            "growth": 0.12,

            "color": "#38BDF8"

        },

        "Bear": {

            "valuation": 300,

            "week": "-6%",

            "demand": "Moderate",

            "growth": 0.04,

            "color": "#EF4444"

        }

    }

    tabs = [

        (bull, "Bull"),

        (base, "Base"),

        (bear, "Bear")

    ]

    for tab, name in tabs:

        with tab:

            data = scenarios[name]

            c1, c2, c3 = st.columns(3)

            c1.metric(

                "IPO Valuation",

                f"${data['valuation']}B"

            )

            c2.metric(

                "Expected Week 1",

                data["week"]

            )

            c3.metric(

                "Institutional Demand",

                data["demand"]

            )

            years = np.arange(0, 11)

            values = data["valuation"] * (

                (1 + data["growth"]) ** years

            )

            fig = go.Figure()

            fig.add_trace(

                go.Scatter(

                    x=years,

                    y=values,

                    mode="lines+markers",

                    line=dict(

                        width=4,

                        color=data["color"]

                    ),

                    fill="tozeroy"

                )

            )

            fig.update_layout(

                height=380,

                paper_bgcolor="rgba(0,0,0,0)",

                plot_bgcolor="rgba(0,0,0,0)",

                margin=dict(

                    l=0,

                    r=0,

                    t=20,

                    b=0

                ),

                xaxis_title="Years After IPO",

                yaxis_title="Projected Valuation ($B)",

                font=dict(

                    color="white"

                )

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

            st.info(

                f"""
**Scenario Summary**

• IPO Valuation: **${data['valuation']}B**

• Expected First Week Return: **{data['week']}**

• Institutional Demand: **{data['demand']}**

• 10-Year Projection: **${values[-1]:.0f}B**

"""
            )