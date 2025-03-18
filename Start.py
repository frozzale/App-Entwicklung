import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_Kalorienverbrauch2.0")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

# ====== End Init Block ======

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

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
