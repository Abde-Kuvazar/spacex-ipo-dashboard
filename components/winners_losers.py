import streamlit as st

from services.sector_engine import calculate_sector_scores


def render_winners_losers():

    df = calculate_sector_scores()

    winners = df.head(5)

    losers = df.tail(5).sort_values(

        "Expected Change"

    )

    st.subheader(

        "🏆 Winners vs Potential Losers"

    )

    c1, c2 = st.columns(2)

    with c1:

        st.success(

            "Potential Winners"

        )

        for _, row in winners.iterrows():

            st.metric(

                row["Company"],

                f"+{row['Expected Change']:.1f}%"

            )

    with c2:

        st.error(

            "Potential Losers"

        )

        for _, row in losers.iterrows():

            st.metric(

                row["Company"],

                f"{row['Expected Change']:.1f}%"

            )