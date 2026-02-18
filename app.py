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
if page == "Accueil":

    st.title("🧭 Assistant des aides pour le handicap")

    st.write("""
Bienvenue dans ton assistant.

Cet outil t'aidera à:
- comprendre les aides disponibles
- vérifier ton admissibilité
- trouver des ressources
""")

# ---------- PAGE TEST ----------
elif page == "Test CIPH":

    st.title("Test rapide CIPH")

    reponse = st.radio(
        "Tes limitations durent-elles depuis plus de 12 mois ?",
        ["Oui", "Non"]
    )

    if reponse == "Oui":
        st.success("Tu pourrais être admissible au CIPH.")
    else:
        st.warning("Ce critère pourrait être un obstacle.")

# ---------- PAGE RESSOURCES ----------
elif page == "Ressources":

    st.title("Ressources utiles")

    st.write("""
Voici quelques exemples de ressources:

- Organismes d'aide
- Médecins spécialisés
- Informations IVAC
""")
