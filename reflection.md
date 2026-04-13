# Profile Comparisons and Reflections

---

## Pair 1: High-Energy Pop vs Chill Lofi

The High-Energy Pop profile returned Sunrise City and Gym Hero at the top — both fast, upbeat pop songs. The Chill Lofi profile returned Library Rain and Midnight Coding — slow, quiet, study-music type tracks. These two profiles produced completely opposite results, which makes sense. One user is looking for something to pump them up, the other wants background music to focus or relax. The system correctly separated them because genre, mood, and energy all pointed in opposite directions. This is the clearest example of the recommender working exactly as intended.

---

## Pair 2: Deep Intense Rock vs Conflicting (High Energy + Melancholic)

The Deep Intense Rock profile returned Storm Runner at #1 with a near-perfect score — high energy, intense mood, rock genre, everything aligned. The Conflicting profile — which wanted high energy but a melancholic mood — returned Hello by Adele at #1. This is where the system gets tricky. Adele is melancholic and matches the genre (soul pop), but her songs are not high-energy at all. The system chose the emotional label over the actual sound. For a real user who wants something that feels like an intense Adele-style emotional punch — think Rolling in the Deep — the system partially gets it right, but it still leans toward quiet ballads because "melancholic" and "soul pop" are the dominant signals. High-energy rock songs like Believer only appear lower in the list.

---

## Pair 3: Missing Genre (Jazz Fusion) vs Dead Center (All 0.5)

The Missing Genre profile asked for jazz fusion which does not exist in the catalog. The system still returned reasonable results — Coffee Shop Stories (jazz, relaxed) came first because its energy and mood were closest to what the user wanted. No song scored above 3.44, meaning the system clearly struggled but did not break. The Dead Center profile set all preferences to the middle (0.5). This exposed an interesting behavior — with no strong numerical preference, the genre match became the deciding factor again, and Spacewalk Thoughts won just from being the only ambient song. After the weight shift experiment, Focus Flow took over because energy alignment mattered more. This pair shows that when users have vague preferences, the system defaults to whatever categorical label matches rather than finding a truly average-sounding song.

---

## Pair 4: Wants Instrumental but Likes Pop vs High-Energy Pop

Both profiles declared pop as their favorite genre and happy as their mood. The only difference was that one wanted highly instrumental music (target_instrumentalness = 0.95) while the other just wanted energetic pop. Both returned Sunrise City at #1. This shows a weakness — the instrumentalness preference was essentially ignored because pop songs in the catalog are all vocal. The genre weight pulled pop songs to the top regardless of how instrumental the user wanted their music to be. Vivaldi appeared at #5 in the instrumental profile, which is the one moment the system responded to the instrumentalness preference. In a real app, wanting instrumental music should probably override genre entirely, but our scoring does not currently support that kind of priority logic.
