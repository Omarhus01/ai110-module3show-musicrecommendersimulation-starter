"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs
from tabulate import tabulate


PROFILES = [
    ("High-Energy Pop", {
        "favorite_genre":          "pop",
        "favorite_mood":           "happy",
        "target_energy":           0.90,
        "target_valence":          0.80,
        "likes_acoustic":          False,
        "target_instrumentalness": 0.05,
    }),
    ("Chill Lofi", {
        "favorite_genre":          "lofi",
        "favorite_mood":           "chill",
        "target_energy":           0.38,
        "target_valence":          0.58,
        "likes_acoustic":          True,
        "target_instrumentalness": 0.50,
    }),
    ("Deep Intense Rock", {
        "favorite_genre":          "rock",
        "favorite_mood":           "intense",
        "target_energy":           0.91,
        "target_valence":          0.48,
        "likes_acoustic":          False,
        "target_instrumentalness": 0.04,
    }),
    # --- Adversarial profiles ---
    ("Conflicting: High Energy + Melancholic", {
        "favorite_genre":          "soul pop",
        "favorite_mood":           "melancholic",
        "target_energy":           0.90,
        "target_valence":          0.20,
        "likes_acoustic":          False,
        "target_instrumentalness": 0.05,
    }),
    ("Missing Genre: Jazz Fusion", {
        "favorite_genre":          "jazz fusion",
        "favorite_mood":           "relaxed",
        "target_energy":           0.37,
        "target_valence":          0.71,
        "likes_acoustic":          True,
        "target_instrumentalness": 0.70,
    }),
    ("Wants Instrumental but Likes Pop", {
        "favorite_genre":          "pop",
        "favorite_mood":           "happy",
        "target_energy":           0.80,
        "target_valence":          0.80,
        "likes_acoustic":          False,
        "target_instrumentalness": 0.95,
    }),
    ("Dead Center: All 0.5", {
        "favorite_genre":          "ambient",
        "favorite_mood":           "focused",
        "target_energy":           0.50,
        "target_valence":          0.50,
        "likes_acoustic":          True,
        "target_instrumentalness": 0.50,
    }),
]


def print_recommendations(profile_name: str, recommendations: list) -> None:
    """Prints a formatted table of recommendations for a given profile."""
    print("\n" + "=" * 60)
    print(f"  Profile: {profile_name}")
    print("=" * 60 + "\n")

    table_rows = []
    reasons_rows = []

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        table_rows.append([
            f"#{i}",
            song["title"],
            song["artist"],
            song["genre"],
            song["mood"],
            f"{score:.2f} / 6.5",
        ])
        reasons_rows.append((f"#{i} {song['title']}", explanation))

    print(tabulate(
        table_rows,
        headers=["Rank", "Title", "Artist", "Genre", "Mood", "Score"],
        tablefmt="outline"
    ))

    print("\n" + "-" * 60)
    print("  Why each song was recommended:")
    print("-" * 60)
    for title, reason in reasons_rows:
        print(f"\n{title}")
        print(f"  {reason}")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for profile_name, user_prefs in PROFILES:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(profile_name, recommendations)


if __name__ == "__main__":
    main()
