TRANSLATIONS = {
    "currentVolumeInCubicMetres": "Aktuelles Volumen",
    "reverseVolumeInCubicMetres": "Rückwärtsvolumen",
    "isFlagCurrentLeak": "Leckage aktuell",
    "isFlagLast24HoursReverseFlow": "Rückfluss letzte 24h",
    "isFlagCurrentLowBattery": "Batterie niedrig",
}

def translate(key):
    return TRANSLATIONS.get(key, key.replace("_", " ").lower())
