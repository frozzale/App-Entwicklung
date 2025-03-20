# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import plotly.express as px

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

# Aktivitätslevel über Zeit
st.caption('Aktivitätslevel über Zeit')
# Aktivitätslevel in eine geordnete Kategorie umwandeln
activity_order = [
    "Wenig oder keine Bewegung",
    "Leichte Bewegung (1-3 Tage/Woche)",
    "Mäßige Bewegung (3-5 Tage/Woche)",
    "Starke Bewegung (6-7 Tage/Woche)",
    "Sehr starke Bewegung (2x pro Tag)"
]
data_df['Aktivitaetslevel'] = pd.Categorical(data_df['Aktivitaetslevel'], categories=activity_order, ordered=True)

# Plotly-Chart für Aktivitätslevel
fig = px.line(
    data_df,
    x='timestamp',
    y='Aktivitaetslevel',
    title='Aktivitätslevel über Zeit',
    labels={"Aktivitätslevel": "Aktivitätslevel", "timestamp": "Zeitpunkt"},
    category_orders={"Aktivitätslevel": activity_order}
)
st.plotly_chart(fig, use_container_width=True)

# Kalorienverbrauch über Zeit
st.caption('Kalorienverbrauch über Zeit (kcal)')
st.line_chart(data=data_df.set_index('timestamp')['Kalorienverbrauch (kcal)'],
                use_container_width=True)
