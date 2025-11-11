# selector.py

def choisir_musique(scenario):
    """
    Sélectionne une playlist adaptée au scénario donné.
    :param scenario: dict avec les clés 'age', 'ambiance', 'evenement', 'duree'
    :return: liste de morceaux simulée
    """
    age = scenario.get("age", 18)
    ambiance = scenario.get("ambiance", "joyeuse")
    evenement = scenario.get("evenement", "soirée")
    duree = scenario.get("duree", 60)

    # Simuler une sélection (à remplacer par API musicale plus tard)
    playlist = []

    if ambiance == "joyeuse":
        playlist = ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake"]
    elif ambiance == "calme":
        playlist = ["Weightless - Marconi Union", "Clair de Lune - Debussy"]
    elif ambiance == "énergique":
        playlist = ["Titanium - David Guetta", "Levels - Avicii"]
    elif ambiance == "romantique":
        playlist = ["Perfect - Ed Sheeran", "All of Me - John Legend"]

    # Simuler une durée
    return playlist[:int(duree / 3)]
