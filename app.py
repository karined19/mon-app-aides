import streamlit as st

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background-color: #F7F9FC;
}
h1 {
    color: #6C63FF;
}
</style>
""", unsafe_allow_html=True)

# ---------- MENU ----------
page = st.sidebar.selectbox(
    "Navigation",
    ["Accueil", "Test CIPH", "Ressources"]
)

# ---------- PAGE ACCUEIL ----------
st.title("🧭 Votre guide des aides pour le handicap")

st.write("""
Les démarches peuvent être longues et complexes.
Cet outil vous aide à comprendre rapidement vos droits et les étapes à suivre.
""")

st.write("---")

st.write("### Ce que vous pouvez faire ici:")

st.write("""
✔ Vérifier votre admissibilité au CIPH  
✔ Comprendre les démarches administratives  
✔ Trouver des ressources et spécialistes  
""")

if st.button("Commencer mon évaluation"):
    st.session_state.page = "Test CIPH"

# ---------- PAGE TEST ----------
st.title("Test rapide CIPH")

score = 0

q1 = st.radio(
    "Tes limitations durent-elles depuis plus de 12 mois ?",
    ["Oui", "Non"]
)

if q1 == "Oui":
    score += 2

q2 = st.radio(
    "Tes limitations affectent-elles fortement tes activités quotidiennes ?",
    ["Oui", "Parfois", "Non"]
)

if q2 == "Oui":
    score += 2
elif q2 == "Parfois":
    score += 1

q3 = st.radio(
    "Ces limitations sont-elles présentes la majorité du temps ?",
    ["Oui", "Non"]
)

if q3 == "Oui":
    score += 2

st.write("---")

if st.button("Voir mon résultat"):
    
    if score >= 5:
        st.success("👉 Il est possible que tu sois admissible au CIPH.")
    elif score >= 3:
        st.warning("👉 Admissibilité incertaine. Un professionnel devra évaluer.")
    else:
        st.info("👉 Le CIPH pourrait être difficile à obtenir pour l'instant.")

# ---------- PAGE RESSOURCES ----------
elif page == "Ressources":

    st.title("Ressources utiles")

    st.write("""
Voici quelques exemples de ressources:

- Organismes d'aide
- Médecins spécialisés
- Informations IVAC
""")
