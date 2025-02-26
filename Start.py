import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

st.write("Diese App wurde von Alessia Frozzi und Alicia Cardoso entwickelt.")
st.write("Die dazugehörigen Emails lauten: frozzale@students.zhaw.ch und cardoali@students.zhaw.ch")
# Beispiel-Datenstruktur
data = {
    'Name': ['Alessia Frozzi', 'Alicia Cardoso'],
    'Email': ['frozzale@students.zhaw.ch', 'cardoali@students.zhaw.ch']
}

st.divier()

# Erstellen eines DataFrame
df = pd.DataFrame(data)

# Anzeigen der Tabelle
st.write("Daten in einer Tabelle:")
st.dataframe(df)