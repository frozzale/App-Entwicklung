# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
from functions.kalorienverbrauch_calculator import calculate_calories

st.title("Kalorienverbrauchsrechner")

st.write("Autoren: Alessia Frozzi: frozzale@students.zhaw.ch, Alicia Cardoso: cardoali@students.zhaw.ch")
st.divider()
st.write("In diesem Rechner kannst du deinen täglichen, durchschnittlichen Kalorienverbrauch ganz einfach und unkompliziert berechnen. Verwendete Formel: Harris-Benedict-Formel.")
st.write("Dafür benötigen wir einige Informationen von dir. Bitte fülle die folgenden Felder aus:")


st.header("Rechner")

# Eingabefelder für Benutzerinformationen
gewicht = st.number_input("Gewicht (kg)", min_value=0.0, step=0.1)
groesse = st.number_input("Groesse (cm)", min_value=0.0, step=0.1)
alter = st.number_input("Alter (Jahre)", min_value=0, step=1)
geschlecht = st.selectbox("Geschlecht", ["Maennlich", "Weiblich"])

# Aktivitätslevel
aktivitaetslevel = st.selectbox("Aktivitätslevel", [
    "Wenig oder keine Bewegung",
    "Leichte Bewegung (1-3 Tage/Woche)",
    "Mäßige Bewegung (3-5 Tage/Woche)",
    "Starke Bewegung (6-7 Tage/Woche)",
    "Sehr starke Bewegung (2x pro Tag)"
])

# Berechnung des Kalorienverbrauchs bei Klick auf den "Submit"-Knopf
if st.button("Submit"):
    # Berechnung des Grundumsatzes (BMR) nach der Harris-Benedict-Formel
    if geschlecht == "Männlich":
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    else:
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)

    # Berechnung des Kalorienverbrauchs basierend auf dem Aktivitätslevel
    if aktivitaetslevel == "Wenig oder keine Bewegung":
        kalorienverbrauch = bmr * 1.2
    elif aktivitaetslevel == "Leichte Bewegung (1-3 Tage/Woche)":
        kalorienverbrauch = bmr * 1.375
    elif aktivitaetslevel == "Mäßige Bewegung (3-5 Tage/Woche)":
        kalorienverbrauch = bmr * 1.55
    elif aktivitaetslevel == "Starke Bewegung (6-7 Tage/Woche)":
        kalorienverbrauch = bmr * 1.725
    else:
        kalorienverbrauch = bmr * 1.9

    # Speichern der Ergebnisse
    result = {
        "timestamp": helpers.ch_now(),
        "Gewicht (kg)": gewicht,
        "Groeße (cm)": groesse,
        "Alter (Jahre)": alter,
        "Geschlecht": geschlecht,
        "Aktivitaetslevel": aktivitaetslevel,
        "Kalorienverbrauch (kcal)": kalorienverbrauch
    }  

    # Anzeige des Ergebnisses
    st.write(f"Ihr täglicher Kalorienverbrauch beträgt: {kalorienverbrauch:.2f} kcal")

    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)


st.divider()

st.write("Für weitere Informationen zur Harris-Benedict-Formel und den Aktivitätsleveln klicke folgenden Link:")
st.link_button("Harris-Benedict-Formel und Aktivitätslevel", "https://de.wikipedia.org/wiki/Grundumsatz")

st.write("Wenn du nicht weisst, wie du auf deine Kalorien kommen sollst, dann klicke hier:")
st.link_button("Easy recipes", "https://ch.pinterest.com/allrecipes/easy-recipes/")

st.divider()

st.write("Wie fandest du diesen Rechner? Lass es uns wissen!")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")

