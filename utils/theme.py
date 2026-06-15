import streamlit as st

COSMIC_CSS = """
<style>

:root{
    --bg:#04060c;
    --glass:rgba(255,255,255,.05);
    --border:rgba(255,255,255,.08);
    --blue:#7dd3fc;
    --purple:#a78bfa;
}

html,
body,
[data-testid="stAppViewContainer"]{

background:
radial-gradient(circle at 20% 10%,rgba(124,58,237,.20),transparent 40%),
radial-gradient(circle at 80% 0%,rgba(14,165,233,.15),transparent 40%),
#04060c;

color:white;

}

[data-testid="stHeader"]{

background:transparent;

}

section[data-testid="stSidebar"]{

background:rgba(8,12,20,.90);
backdrop-filter:blur(18px);

}

div[data-testid="stMetric"]{

background:rgba(255,255,255,.04);

border:1px solid rgba(255,255,255,.08);

border-radius:18px;

padding:15px;

}

</style>
"""

def load_theme():

    st.markdown(

        COSMIC_CSS,

        unsafe_allow_html=True

    )