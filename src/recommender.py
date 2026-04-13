from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float
    instrumentalness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_valence: float = 0.5
    target_instrumentalness: float = 0.1

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k songs sorted by score for the given user profile."""
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a plain-language explanation of why a song was recommended."""
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns them as a list of dicts with correct types."""
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":               int(row["id"]),
                "title":            row["title"],
                "artist":           row["artist"],
                "genre":            row["genre"],
                "mood":             row["mood"],
                "energy":           float(row["energy"]),
                "tempo_bpm":        float(row["tempo_bpm"]),
                "valence":          float(row["valence"]),
                "danceability":     float(row["danceability"]),
                "acousticness":     float(row["acousticness"]),
                "instrumentalness": float(row["instrumentalness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Scores a single song against user preferences and returns (score, explanation)."""
    score = 0.0
    reasons = []

    # Genre match (+2.0)
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match (+1.0)
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy closeness (up to +1.0)
    energy_score = 1.0 * (1 - abs(song["energy"] - user_prefs["target_energy"]))
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    # Valence closeness (up to +0.5)
    valence_score = 0.5 * (1 - abs(song["valence"] - user_prefs["target_valence"]))
    score += valence_score
    reasons.append(f"valence closeness (+{valence_score:.2f})")

    # Acousticness (up to +0.5)
    if user_prefs["likes_acoustic"]:
        acoustic_score = 0.5 * song["acousticness"]
    else:
        acoustic_score = 0.5 * (1 - song["acousticness"])
    score += acoustic_score
    reasons.append(f"acousticness (+{acoustic_score:.2f})")

    # Instrumentalness closeness (up to +0.5)
    instr_score = 0.5 * (1 - abs(song["instrumentalness"] - user_prefs["target_instrumentalness"]))
    score += instr_score
    reasons.append(f"instrumentalness (+{instr_score:.2f})")

    return score, " | ".join(reasons)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs against user preferences and returns the top k sorted by score descending."""
    scored = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored.append((song, score, explanation))

    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
