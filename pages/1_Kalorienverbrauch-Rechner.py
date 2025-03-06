import streamlit as st

st.title("Kalorienverbrauchsrechner")

st.write("Autoren: Alessia Frozzi: frozzale@students.zhaw.ch, Alicia Cardoso: cardoali@students.zhaw.ch")
st.divider()
st.write("In diesem Rechner kannst du deinen täglichen, durchschnittlichen Kalorienverbrauch ganz einfach und unkompliziert berechnen. Verwendete Formel: Harris-Benedict-Formel.")
st.write("Dafür benötigen wir einige Informationen von dir. Bitte fülle die folgenden Felder aus:")

import streamlit as st

st.header("Rechner")

# Eingabefelder für Benutzerinformationen
gewicht = st.number_input("Gewicht (kg)", min_value=0.0, step=0.1)
groesse = st.number_input("Größe (cm)", min_value=0.0, step=0.1)
alter = st.number_input("Alter (Jahre)", min_value=0, step=1)
geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])

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

    # Anzeige des Ergebnisses
    st.write(f"Ihr täglicher Kalorienverbrauch beträgt: {kalorienverbrauch:.2f} kcal")

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

