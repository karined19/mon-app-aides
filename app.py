import streamlit as st

# ----- CSS -----
st.markdown("""
<style>

body {
    background-color: #f7f9fc;
}

h1 {
    color: #6C63FF;
    text-align: center;
}

.stButton > button {
    border-radius: 12px;
    background-color: #6C63FF;
    color: white;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ----- APP -----
st.title("🧭 Mon assistant d'aides")

st.write("Bienvenue dans ton prototype 🙂")

name = st.text_input("Ton prénom")

if name:
    st.success(f"Bonjour {name} !")

