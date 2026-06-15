import streamlit as st


def render_metrics(

    valuation,

    public_cap,

    sp_weight,

    day1_pop

):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "🚀 Valuation",

        f"${valuation:,} B"

    )

    c2.metric(

        "💰 Public Float",

        f"${public_cap:,.0f} B"

    )

    c3.metric(

        "📈 S&P Weight",

        f"{sp_weight:.2f}%"

    )

    c4.metric(

        "⚡ Day 1 Pop",

        f"+{day1_pop:.1f}%"

    )