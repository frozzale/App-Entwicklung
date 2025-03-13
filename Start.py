import streamlit as st
import pandas as pd

from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_Kalorienverbrauch")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Meine erste Streamlit App")

st.write("Diese App wurde von Alessia Frozzi und Alicia Cardoso entwickelt.")
st.write("- Alessia Frozzi: frozzale@students.zhaw.ch")
st.write("- Alicia Cardoso: cardoali@students.zhaw.ch")
# Beispiel-Datenstruktur
data = {
    'Name': ['Alessia Frozzi', 'Alicia Cardoso'],
    'Email': ['frozzale@students.zhaw.ch', 'cardoali@students.zhaw.ch']
}
st.divider()
# Erstellen eines DataFrame
df = pd.DataFrame(data)

# Anzeigen der Tabelle
st.write("Daten in einer Tabelle:")
st.dataframe(df)
