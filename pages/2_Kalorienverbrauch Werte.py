import streamlit as st

st.title("Kalorienverbrauch Werte")

data_df = st.session_state['data_df']
if data_df.empty:
    st.info("Keine Kalorienverbrauchsdaten vorhanden. Berechnen Sie Ihren Kalorienverbrauch auf der Startseite.")
    st.stop()

data_df = data_df.sort_values('timestamp', ascending=False)

st.dataframe(data_df)
