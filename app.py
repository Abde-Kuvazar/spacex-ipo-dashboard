"""
SpaceX IPO Intelligence — Streamlit edition
A cinematic, dark-themed financial intelligence dashboard modeling the impact
of a hypothetical SpaceX IPO on US equity markets.

Run:
    pip install -r requirements.txt
    streamlit run app.py
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from services.index_engine import calculate_index_weights
from services.prediction_engine import predict_week1_return
from services.capital_flow_engine import estimate_capital_flow
from services.market_api import get_market_caps
from services.sector_engine import calculate_sector_scores
from components.bubble_universe import render_bubble_universe

# ---------------------------------------------------------------------------
# Page config + cosmic theme
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SpaceX IPO Intelligence",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

COSMIC_CSS = """
<style>
:root {
  --bg: #05070d;
  --panel: rgba(255,255,255,0.04);
  --border: rgba(255,255,255,0.08);
  --accent: #7dd3fc;
  --accent2: #a78bfa;
  --gold: #fbbf24;
}
html, body, [data-testid="stAppViewContainer"] {
  background:
    radial-gradient(ellipse at 20% -10%, rgba(124,58,237,0.25), transparent 50%),
    radial-gradient(ellipse at 80% 10%, rgba(14,165,233,0.20), transparent 55%),
    radial-gradient(ellipse at 50% 100%, rgba(236,72,153,0.12), transparent 60%),
    #04060c !important;
  color: #e6eefc !important;
}
[data-testid="stHeader"] { background: transparent; }
section[data-testid="stSidebar"] {
  background: rgba(6,10,20,0.85) !important;
  border-right: 1px solid var(--border);
  backdrop-filter: blur(18px);
}
h1, h2, h3, h4 {
  font-family: 'Inter','SF Pro Display',sans-serif;
  letter-spacing: -0.02em;
  background: linear-gradient(120deg,#fff 0%,#7dd3fc 50%,#a78bfa 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.glass {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 1.25rem 1.5rem;
  backdrop-filter: blur(14px);
  box-shadow: 0 10px 40px -10px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.04);
}
.kpi-label { font-size:.72rem; letter-spacing:.2em; text-transform:uppercase;
  color:#7891b8; margin-bottom:.4rem; }
.kpi-value { font-size:1.9rem; font-weight:600; color:#fff; }
.kpi-delta-up { color:#34d399; font-size:.85rem; }
.kpi-delta-down { color:#f87171; font-size:.85rem; }
.tag { display:inline-block; padding:.2rem .55rem; border-radius:999px;
  font-size:.7rem; border:1px solid var(--border); color:#a8c0e6; margin-right:.25rem;}
hr { border-color: rgba(255,255,255,0.06) !important; }
.stTabs [data-baseweb="tab-list"] { gap: .25rem; }
.stTabs [data-baseweb="tab"] {
  background: rgba(255,255,255,0.03); border-radius: 10px;
  padding: .5rem 1rem; color:#a8c0e6;
}
.stTabs [aria-selected="true"] {
  background: linear-gradient(120deg, rgba(125,211,252,.2), rgba(167,139,250,.2)) !important;
  color: #fff !important; border:1px solid rgba(125,211,252,.4);
}
.stSlider [data-baseweb="slider"] > div > div { background: linear-gradient(90deg,#7dd3fc,#a78bfa) !important; }
div[data-testid="stMetric"] {
  background: var(--panel); border:1px solid var(--border);
  border-radius:16px; padding:1rem 1.2rem; backdrop-filter: blur(14px);
}
</style>
"""
st.markdown(COSMIC_CSS, unsafe_allow_html=True)

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#cfe0ff", family="Inter, sans-serif"),
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis=dict(gridcolor="rgba(255,255,255,0.06)", zerolinecolor="rgba(255,255,255,0.1)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.06)", zerolinecolor="rgba(255,255,255,0.1)"),
)

def style(fig):
    fig.update_layout(**PLOTLY_LAYOUT)
    return fig

# ---------------------------------------------------------------------------
# Sidebar — global controls
# ---------------------------------------------------------------------------
st.sidebar.markdown("### 🚀  Mission Control")
valuation = st.sidebar.slider(
    "Hypothetical SpaceX Valuation ($B)",
    min_value=100, max_value=2000, value=400, step=25,
    help="Drives weights, inflows, sector impact and scenarios across the dashboard.",
)
float_pct = st.sidebar.slider("Public Float (%)", 5, 50, 15, 1)
market_regime = st.sidebar.selectbox("Market Regime", ["Bull", "Neutral", "Bear"], index=1)
st.sidebar.divider()
st.sidebar.caption("Hypothetical model · Educational use only · Not investment advice")

weights = calculate_index_weights(
    valuation,
    float_pct
)

SP500_MCAP = 55000
NASDAQ_MCAP = 30000
public_cap = weights["public_value"]

sp_weight = weights["sp500"]

nas_weight = weights["nasdaq"]

passive_inflows = estimate_capital_flow(
    valuation,
    float_pct
)

day1_pop = predict_week1_return(
    valuation,
    market_regime
)

# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
st.markdown("# SpaceX IPO Intelligence")
st.markdown(
    "<span class='tag'>LIVE MODEL</span><span class='tag'>HYPOTHETICAL</span>"
    "<span class='tag'>BLOOMBERG × APPLE × SPACEX</span>",
    unsafe_allow_html=True,
)
st.markdown(
    "#### A cinematic look at how a SpaceX listing would reshape US equity markets — "
    "valuation, capital rotation, sector winners, and long-term scenarios."
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Valuation", f"${valuation:,}B", f"{(valuation-400)/400*100:+.1f}% vs base")
c2.metric(

    "Public Float",

    f"${public_cap:.1f}B",

    f"{float_pct}% of valuation"

)
c3.metric("S&P 500 Weight", f"{sp_weight:.2f}%", f"Top {'5' if sp_weight>2 else '15'} constituent")
c4.metric("Est. Day-1 Pop", f"+{day1_pop:.1f}%", market_regime + " regime")

st.divider()

# # ---------------------------------------------------------------------------
# # MARKET BUBBLES
# # ---------------------------------------------------------------------------
st.markdown("## 🪐  Market Universe")
st.caption("Bubble size = market cap. SpaceX enters as a new gravitational body.")

mega = get_market_caps()

layout = pd.read_csv(
    "data/bubble_layout.csv"
)

mega = mega.merge(
    layout,
    on="Company",
    how="left"
)

spacex = pd.DataFrame({

    "Company":["SpaceX"],

    "Ticker":["SPACEX"],

    "Sector":["Aerospace"],

    "Market Cap":[f"${valuation}B"],

    "Raw Market Cap":[valuation*1_000_000_000],

    "x":[50],

    "y":[35]

})

mega = pd.concat(
    [mega,spacex],
    ignore_index=True
)

mega["ticker"] = mega["Company"]

mega["sector"] = mega["Sector"]

mega["mcap"] = mega["Raw Market Cap"]/1_000_000_000


fig = px.scatter(
    mega, x="x", y="y", size="mcap", color="sector", text="ticker",
    size_max=90, 
    color_discrete_map={

        "Technology":"#7dd3fc",

        "Consumer":"#a78bfa",

        "Automotive":"#fbbf24",

        "Communication":"#34d399",

        "Aerospace":"#22c55e"

    },
    hover_data={"mcap":":.0f","x":False,"y":False},
)
fig.update_traces(textposition="middle center",
                  textfont=dict(color="white", size=11, family="Inter"))
fig.update_xaxes(visible=False); fig.update_yaxes(visible=False)
fig.update_layout(height=480, legend=dict(bgcolor="rgba(0,0,0,0)"))
st.plotly_chart(style(fig), width="stretch")

st.divider()



# ---------------------------------------------------------------------------
# SIMULATOR
# ---------------------------------------------------------------------------

st.markdown("## 🎛 Valuation Simulator")

left, right = st.columns([1.2, 1])

with left:

    st.markdown("##### Real-time Index Impact")

    sweep = np.linspace(100, 2000, 60)

    sw_sp = (
        (sweep * float_pct / 100)
        / (SP500_MCAP + sweep * float_pct / 100)
        * 100
    )

    sw_nas = (
        (sweep * float_pct / 100)
        / (NASDAQ_MCAP + sweep * float_pct / 100)
        * 100
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=sweep,
            y=sw_sp,
            name="S&P 500 weight %",
            line=dict(color="#7dd3fc", width=3),
            fill="tozeroy",
            fillcolor="rgba(125,211,252,.15)",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=sweep,
            y=sw_nas,
            name="Nasdaq weight %",
            line=dict(color="#a78bfa", width=3, dash="dot"),
        )
    )

    fig.add_vline(
        x=valuation,
        line=dict(
            color="#fbbf24",
            width=2,
            dash="dash",
        ),
    )

    fig.update_layout(

        height=320,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(l=10, r=10, t=20, b=10),

        legend=dict(
            orientation="h",
            y=1.08,
        ),

    )

    st.plotly_chart(

        style(fig),

        width="stretch",

        config={

            "displayModeBar": False,

            "displaylogo": False,

        },

    )

with right:

    st.markdown("##### Capital Required")

    st.metric(

        "Passive Inflows (ETF rebalance)",

        f"${passive_inflows:.1f}B",

    )

    st.metric(

        "Active Manager Demand",

        f"${passive_inflows*1.6:.1f}B",

    )

    st.metric(

        "Total Day-1 Liquidity Need",

        f"${passive_inflows*2.6:.1f}B",

    )

    st.progress(

        min(passive_inflows / 120, 1.0),

        text=f"S&P weight saturation: {sp_weight:.2f}% of 5%",

    )

# ---------------------------------------------------------------------------
# SECTORS + WINNERS/LOSERS
# ---------------------------------------------------------------------------

st.markdown("## 🛰 Sector Impact Map")

sectors = calculate_sector_scores()

fig = px.treemap(

    sectors,

    path=["Sector"],

    values="Expected Change",

    color="Expected Change",

    color_continuous_scale=["#f87171", "#1e293b", "#34d399"],

    color_continuous_midpoint=0

)

fig.update_layout(

    height=420,

    margin=dict(l=10, r=10, t=20, b=10),

    paper_bgcolor="rgba(0,0,0,0)",

    font=dict(color="white")

)

st.plotly_chart(

    fig,

    width="stretch"

)

winners = sectors.sort_values(

    "Expected Change",

    ascending=False

).head(4)

losers = sectors.sort_values(

    "Expected Change",

    ascending=True

).head(4)

w, l = st.columns(2)

with w:

    st.markdown("### 🟢 Likely Winners")

    for _, row in winners.iterrows():

        st.markdown(

            f"""

<div class='glass' style='margin-bottom:.5rem'>

<b>{row['Company']}</b>

<span style='float:right;color:#34d399'>

+{row['Expected Change']:.1f}%

</span>

</div>

""",

            unsafe_allow_html=True,

        )

with l:

    st.markdown("### 🔴 Likely Losers")

    for _, row in losers.iterrows():

        st.markdown(

            f"""

<div class='glass' style='margin-bottom:.5rem'>

<b>{row['Company']}</b>

<span style='float:right;color:#f87171'>

{row['Expected Change']:.1f}%

</span>

</div>

""",

            unsafe_allow_html=True,

        )

st.divider()

# ---------------------------------------------------------------------------
# HISTORICAL ANALOGUES
# ---------------------------------------------------------------------------

st.markdown("## 📜 Historical Mega-IPO Analogues")

hist = pd.read_csv("data/historical_ipos.csv")

# Remove previous simulated row
hist = hist[hist["Company"] != "SpaceX"]

# Add simulated SpaceX
hist.loc[len(hist)] = {

    "Company": "SpaceX",

    "Year": 2026,

    "Valuation_B": valuation,

    "IPO_Size_B": public_cap,

    "Week1_Return": day1_pop,

    "Year1_Return": day1_pop * 0.6,

    "Sector": "Aerospace"

}

fig = px.bar(

    hist,

    x="Company",

    y=["Week1_Return", "Year1_Return"],

    barmode="group",

    color_discrete_sequence=["#7dd3fc", "#a78bfa"]

)

fig.update_layout(

    height=380,

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(color="white"),

    legend_title="Returns (%)"

)

st.plotly_chart(

    style(fig),

    width="stretch"

)
# ---------------------------------------------------------------------------
# SENTIMENT
# ---------------------------------------------------------------------------
st.markdown("## 🧠  Market Sentiment")
sc1, sc2, sc3 = st.columns(3)
gauge = lambda title, val, color: go.Figure(go.Indicator(
    mode="gauge+number", value=val, title={"text":title,"font":{"color":"#cfe0ff"}},
    gauge={"axis":{"range":[0,100],"tickcolor":"#456"},
           "bar":{"color":color},
           "bgcolor":"rgba(0,0,0,0)",
           "steps":[{"range":[0,33],"color":"rgba(248,113,113,.2)"},
                    {"range":[33,66],"color":"rgba(251,191,36,.2)"},
                    {"range":[66,100],"color":"rgba(52,211,153,.2)"}]},
)).update_layout(height=260, paper_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))

retail = min(95, 55 + (valuation-400)/30)
inst   = min(90, 45 + (valuation-400)/40)
fear   = max(10, 60 - (valuation-400)/25)
sc1.plotly_chart(gauge("Retail Hype", retail, "#a78bfa"), width="stretch")
sc2.plotly_chart(gauge("Institutional Appetite", inst, "#7dd3fc"), width="stretch")
sc3.plotly_chart(gauge("Fear / Greed", fear, "#fbbf24"), width="stretch")

st.divider()

# ---------------------------------------------------------------------------
# SCENARIOS + LONG TERM
# ---------------------------------------------------------------------------
st.markdown("## 🔮  Scenario Engine")
tabs = st.tabs(["🐂  Bull", "⚖️  Base", "🐻  Bear"])
years = np.arange(0, 11)
base  = valuation * (1.12 ** years)
bull  = valuation * (1.22 ** years)
bear  = valuation * (1.02 ** years)

for tab, label, series, color in zip(
    tabs, ["Bull","Base","Bear"], [bull, base, bear], ["#34d399","#7dd3fc","#f87171"]
):
    with tab:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=series, name=label,
            line=dict(color=color, width=4), fill="tozeroy",
            fillcolor=color.replace(")", ",0.15)").replace("rgb","rgba") if color.startswith("rgb") else "rgba(125,211,252,0.12)"))
        fig.update_layout(height=380, xaxis_title="Years post-IPO", yaxis_title="Valuation $B")
        st.plotly_chart(style(fig), width="stretch")
        st.metric(f"Year-10 {label}", f"${series[-1]:,.0f}B",
                  f"{(series[-1]/valuation-1)*100:+.0f}%")

st.divider()

# ---------------------------------------------------------------------------
# AI ANALYST
# ---------------------------------------------------------------------------
st.markdown("## 🤖  AI Analyst")
preset = st.selectbox("Ask the model:", [
    "What sectors benefit most from the IPO?",
    "How does float size change index weight?",
    "Compare to Saudi Aramco's listing.",
    "Risks to the bull scenario?",
])
if st.button("Generate analysis", type="primary"):
    with st.spinner("Crunching orbital mechanics..."):
        import time; time.sleep(0.6)
    responses = {
        "What sectors benefit most from the IPO?":
            f"At ${valuation}B, aerospace and satellite names see the strongest pull "
            f"(+{valuation/100*1.2:.1f}% modeled). Legacy telcos face -{valuation/300:.1f}% "
            "pressure as Starlink narrative compounds.",
        "How does float size change index weight?":
            f"A {float_pct}% float yields ${public_cap:.0f}B public cap → {sp_weight:.2f}% S&P / "
            f"{nas_weight:.2f}% Nasdaq weight. Doubling the float roughly doubles passive demand.",
        "Compare to Saudi Aramco's listing.":
            f"""
        Saudi Aramco debuted at roughly $1.7T with a very limited public float (~1.5%),
        reducing passive index impact.

        The modeled SpaceX IPO assumes a valuation of ${valuation}B with a {float_pct}% public float,
        creating an estimated public market capitalization of ${public_cap:.0f}B and
        an S&P 500 weight of {sp_weight:.2f}%, making it substantially more influential
        for passive fund rebalancing.
        """,
        "Risks to the bull scenario?":
            "Execution risk on Starship cadence, regulatory drag on Starlink spectrum, "
            "and Mag-7 capital crowding-out remain the dominant tail risks.",
    }
    st.markdown(f"<div class='glass'>{responses[preset]}</div>", unsafe_allow_html=True)

st.markdown("<br><center style='color:#5d75a0;font-size:.8rem'>"
            "SpaceX IPO Intelligence · Hypothetical model for educational use · Not investment advice"
            "</center>", unsafe_allow_html=True)
