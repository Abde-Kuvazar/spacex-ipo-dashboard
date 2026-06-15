import streamlit as st


def render_historical_timeline():

    st.subheader("📜 Historical Mega IPO Intelligence")
    st.caption("Compare the largest IPOs in history with the projected SpaceX IPO.")

    ipos = [

        {
            "company": "Meta",
            "year": "2012",
            "valuation": "$104B",
            "raised": "$16B",
            "week": "+0.6%",
            "year": "-30%"
        },

        {
            "company": "Alibaba",
            "year": "2014",
            "valuation": "$168B",
            "raised": "$25B",
            "week": "+38%",
            "year": "+55%"
        },

        {
            "company": "Saudi Aramco",
            "year": "2019",
            "valuation": "$1.7T",
            "raised": "$29.4B",
            "week": "+10%",
            "year": "-3%"
        },

        {
            "company": "Snowflake",
            "year": "2020",
            "valuation": "$70B",
            "raised": "$3.9B",
            "week": "+111%",
            "year": "+120%"
        },

        {
            "company": "🚀 SpaceX",
            "year": "2026 (Projected)",
            "valuation": "$450B",
            "raised": "$35B",
            "week": "+8%",
            "year": "Projected"
        }

    ]

    cols = st.columns(len(ipos), gap="medium")

    for col, ipo in zip(cols, ipos):

        with col:

            with st.container(border=True):

                st.markdown(
                    f"""
### {ipo['company']}

**{ipo['year']}**

---

**Valuation**

{ipo['valuation']}

**IPO Size**

{ipo['raised']}

**Week 1 Return**

{ipo['week']}

**1 Year Return**

{ipo['year']}
"""
                )

    st.info(
        "🚀 SpaceX figures are hypothetical projections used for simulation purposes."
    )