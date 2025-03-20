from utils import helpers

def calculate_calories(height, weight, age, gender, activity_level):
    """
    Berechnet den Kalorienverbrauch basierend auf der Harris-Benedict-Formel.

    Args:
        height (float): Größe in cm.
        weight (float): Gewicht in kg.
        age (int): Alter in Jahren.
        gender (str): Geschlecht ("Männlich" oder "Weiblich").
        activity_level (str): Aktivitätslevel.

    Returns:
        dict: Ein Dictionary mit den Eingaben, berechnetem Kalorienverbrauch und einem Zeitstempel.
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Größe, Gewicht und Alter müssen positive Werte sein.")

    # Berechnung des Grundumsatzes (BMR) nach der Harris-Benedict-Formel
    if gender == "Männlich":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "Weiblich":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Ungültiges Geschlecht. Bitte 'Männlich' oder 'Weiblich' angeben.")

    # Berechnung des Kalorienverbrauchs basierend auf dem Aktivitätslevel
    activity_multipliers = {
        "Wenig oder keine Bewegung": 1.2,
        "Leichte Bewegung (1-3 Tage/Woche)": 1.375,
        "Maessige Bewegung (3-5 Tage/Woche)": 1.55,
        "Starke Bewegung (6-7 Tage/Woche)": 1.725,
        "Sehr starke Bewegung (2x pro Tag)": 1.9,
    }

    if activity_level not in activity_multipliers:
        raise ValueError("Ungültiges Aktivitätslevel.")

    calories = bmr * activity_multipliers[activity_level]

    # Rückgabe der Ergebnisse als Dictionary
    result_dict = {
        "timestamp": helpers.ch_now(),
        "height": height,
        "weight": weight,
        "age": age,
        "gender": gender,
        "activity_level": activity_level,
        "calories": round(calories, 2),
    }

    return result_dict
