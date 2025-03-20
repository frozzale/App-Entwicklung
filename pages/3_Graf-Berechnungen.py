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

# Aktivitätslevel über Zeit (geordnet)
st.caption('Aktivitätslevel über Zeit (geordnet)')
# Aktivitätslevel in eine geordnete Kategorie umwandeln
activity_order = [
    "Sehr starke Bewegung (2x pro Tag)",
    "Starke Bewegung (6-7 Tage/Woche)",
    "Mäßige Bewegung (3-5 Tage/Woche)",
    "Leichte Bewegung (1-3 Tage/Woche)",
    "Wenig oder keine Bewegung"
]
data_df['Aktivitaetslevel'] = pd.Categorical(
    data_df['Aktivitaetslevel'], categories=activity_order, ordered=True
)

# Balkendiagramm für Aktivitätslevel über Zeit
activity_over_time = data_df[['timestamp', 'Aktivitaetslevel']].copy()
activity_over_time['count'] = 1
activity_over_time = activity_over_time.pivot_table(
    index='timestamp',
    columns='Aktivitaetslevel',
    values='count',
    aggfunc='sum',
    fill_value=0
)
st.bar_chart(activity_over_time, use_container_width=True)

# Kalorienverbrauch über Zeit
st.caption('Kalorienverbrauch über Zeit (kcal)')
st.line_chart(data=data_df.set_index('timestamp')['Kalorienverbrauch (kcal)'],
                use_container_width=True)
