import streamlit as st

# ----- CSS -----
st.markdown("""
<style>

.stApp {
    background-color: #FFF6F8;
}
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
if st.button("Je ne sais pas par où commencer"):
    st.write("➡️ Première étape: vérifier ton admissibilité au CIPH.")
age = st.number_input("Quel âge as-tu ?", 0, 120)

if age >= 18:
    st.write("Tu es majeur.")

