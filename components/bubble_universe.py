import streamlit as st


def bubble(name, value, color, size, left, top):

    return f"""
    <div
        class="bubble"
        style="
            width:{size}px;
            height:{size}px;
            left:{left}%;
            top:{top}%;
            background:radial-gradient(circle at 30% 30%, rgba(255,255,255,.45), {color});
            animation-delay:{left/12}s;
        "
    >
        <div class="bubble-label">
            <div class="bubble-title">{name}</div>
            <div class="bubble-value">${value}</div>
        </div>
    </div>
    """


def render_bubble_universe():

    st.markdown(
        """
<style>

.universe{

position:relative;

width:100%;

height:720px;

overflow:hidden;

border-radius:28px;

background:

radial-gradient(circle at center,
rgba(98,80,255,.12),
transparent 45%),

linear-gradient(135deg,#050816,#081426);

border:1px solid rgba(255,255,255,.08);

box-shadow:
0 0 80px rgba(0,0,0,.5);

}

.universe::before{

content:"";

position:absolute;

width:700px;

height:700px;

left:50%;

top:50%;

transform:translate(-50%,-50%);

border-radius:50%;

background:

radial-gradient(circle,
rgba(110,90,255,.12),
transparent);

filter:blur(40px);

}

.bubble{

position:absolute;

display:flex;

justify-content:center;

align-items:center;

border-radius:50%;

border:1px solid rgba(255,255,255,.15);

backdrop-filter:blur(30px);

box-shadow:

0 0 35px rgba(255,255,255,.08),

0 0 80px rgba(255,255,255,.04),

inset 0 0 70px rgba(255,255,255,.08);

animation:float 7s ease-in-out infinite;

transition:.35s;

cursor:pointer;

}

.bubble:hover{

transform:scale(1.06);

box-shadow:

0 0 70px rgba(255,255,255,.20),

0 0 120px rgba(255,255,255,.10);

}

.bubble::after{

content:"";

position:absolute;

width:24%;

height:24%;

left:18%;

top:16%;

border-radius:50%;

background:rgba(255,255,255,.55);

filter:blur(8px);

}

.bubble-label{

text-align:center;

color:white;

z-index:10;

}

.bubble-title{

font-size:22px;

font-weight:700;

}

.bubble-value{

font-size:18px;

opacity:.9;

margin-top:4px;

}

@keyframes float{

0%{

transform:translateY(0px);

}

50%{

transform:translateY(-18px);

}

100%{

transform:translateY(0px);

}

}

</style>
""",
        unsafe_allow_html=True,
    )

    html = '<div class="universe">'

    html += bubble(
        "Apple",
        "4.28T",
        "#9CA3AF",
        240,
        8,
        18,
    )

    html += bubble(
        "Microsoft",
        "2.90T",
        "#3B82F6",
        200,
        62,
        18,
    )

    html += bubble(
        "Nvidia",
        "4.97T",
        "#10B981",
        220,
        36,
        6,
    )

    html += bubble(
        "Alphabet",
        "4.39T",
        "#60A5FA",
        180,
        48,
        46,
    )

    html += bubble(
        "Amazon",
        "2.57T",
        "#F59E0B",
        170,
        72,
        58,
    )

    html += bubble(
        "Tesla",
        "1.53T",
        "#8B5CF6",
        130,
        22,
        68,
    )

    html += bubble(
        "🚀 SpaceX",
        "450B",
        "#7C3AED",
        95,
        18,
        10,
    )

    html += "</div>"

    st.markdown(
        html,
        unsafe_allow_html=True,
    )