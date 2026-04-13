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


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {
        "favorite_genre":         "alternative rock",
        "favorite_mood":          "epic",
        "target_energy":          0.85,
        "target_valence":         0.50,
        "likes_acoustic":         False,
        "target_instrumentalness": 0.10,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 60)
    print("  Top 5 Recommendations")
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
            f"{score:.2f} / 5.5",
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


if __name__ == "__main__":
    main()
