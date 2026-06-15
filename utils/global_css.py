import streamlit as st


def load_global_css():

    st.markdown(
        """
<style>

/* ---------- Hide Streamlit ---------- */

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

/* ---------- App ---------- */

.stApp{

background:
radial-gradient(circle at center,#14183d 0%,#060812 40%,#03050c 100%);

color:white;

overflow-x:hidden;

}

/* ---------- Scroll ---------- */

::-webkit-scrollbar{
width:8px;
}

::-webkit-scrollbar-track{
background:#060812;
}

::-webkit-scrollbar-thumb{
background:#5B5DF8;
border-radius:20px;
}

/* ---------- Typography ---------- */

h1{

font-size:78px!important;

font-weight:800!important;

letter-spacing:-3px;

margin-bottom:0;

}

h2{

font-size:48px!important;

font-weight:700!important;

}

h3{

font-size:28px!important;

font-weight:600!important;

}

/* ---------- Containers ---------- */

[data-testid="stVerticalBlock"]{

border-radius:24px;

}

/* ---------- Cards ---------- */

div[data-testid="stMetric"]{

background:rgba(255,255,255,.04);

border:1px solid rgba(255,255,255,.08);

backdrop-filter:blur(18px);

border-radius:24px;

padding:18px;

transition:.35s;

}

div[data-testid="stMetric"]:hover{

transform:translateY(-6px);

box-shadow:0 0 35px rgba(105,92,255,.35);

}

/* ---------- Buttons ---------- */

.stButton button{

background:linear-gradient(90deg,#5B5DF8,#8B5CF6);

border:none;

border-radius:999px;

color:white;

font-weight:600;

padding:.7rem 1.8rem;

transition:.3s;

}

.stButton button:hover{

transform:scale(1.04);

box-shadow:0 0 25px rgba(91,93,248,.4);

}

/* ---------- DataFrames ---------- */

[data-testid="stDataFrame"]{

border-radius:24px;

overflow:hidden;

border:1px solid rgba(255,255,255,.06);

}

/* ---------- Plotly ---------- */

.js-plotly-plot{

border-radius:28px;

overflow:hidden;

}

/* ---------- Smooth ---------- */

*{

scroll-behavior:smooth;

transition:.2s;

}

</style>
""",
        unsafe_allow_html=True,
    )