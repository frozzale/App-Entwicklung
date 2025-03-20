# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd

st.title("Grafische Darstellung des Kalorienverbrauchs")

data_df = st.session_state['data_df']
if data_df.empty:
    st.info("Keine Kalorienverbrauchsdaten vorhanden. Berechnen Sie Ihren Kalorienverbrauch auf der Startseite.")
    st.stop()

st.divider()
# Gewicht über Zeit
st.caption('Gewicht über Zeit (kg)')
st.line_chart(data_df.set_index('timestamp')['Gewicht (kg)'], 
                use_container_width=True)

# Kalorienverbrauch über Zeit
st.caption('Kalorienverbrauch über Zeit (kcal)')
st.line_chart(data=data_df.set_index('timestamp')['Kalorienverbrauch (kcal)'],
                use_container_width=True)

# Wie viele Nutzer in einem Aktivitätslevel sind
st.caption("Verteilung der Aktivitätslevel")
activity_counts = data_df['Aktivitaetslevel'].value_counts()
st.bar_chart(activity_counts)