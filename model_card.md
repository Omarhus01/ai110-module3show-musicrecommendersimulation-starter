# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The most significant weakness discovered during testing is categorical score dominance. Even after reducing the genre weight from 2.0 to 1.0, the combined genre and mood match still adds up to +2.0 points out of a maximum of 6.5, which consistently overrides numerical feature alignment. In the conflicting profile test — a user wanting high energy (0.90) with a melancholic mood — Hello by Adele ranked #1 despite having an energy of only 0.45, because the genre and mood match outweighed the large energy mismatch entirely. This means the system effectively ignores how a song actually sounds in favor of how it is labeled, which could frustrate users whose emotional state does not align neatly with a single genre or mood tag. A second limitation is catalog imbalance — genres like rock and country have only one or two songs, so users with those preferences receive almost no variety in their results. Finally, because this is a pure content-based system with no collaborative filtering, it creates a filter bubble where users are never exposed to songs outside their declared preferences, removing any chance of serendipitous discovery.

---

## 7. Evaluation  

Seven user profiles were tested to evaluate how the recommender behaves across a range of preferences. Three were standard profiles — High-Energy Pop, Chill Lofi, and Deep Intense Rock — designed to match songs that clearly exist in the catalog. Four were adversarial profiles designed to expose weaknesses: a conflicting profile (high energy + melancholic mood), a missing genre profile (jazz fusion which does not exist in the catalog), a profile that wants instrumental music but declares pop as its genre, and a dead center profile where all numerical targets were set to 0.5.

The standard profiles all produced intuitive results. Storm Runner scored 5.45 out of 6.5 for the rock profile — nearly perfect — and Library Rain topped the lofi profile as expected. What was surprising was the conflicting profile: Hello by Adele ranked first despite the user wanting energy of 0.90, because the genre and mood label match (soul pop + melancholic) outweighed the large energy gap. This confirmed the categorical dominance bias. The missing genre profile degraded gracefully — no song scored above 3.44 — but still returned acoustically similar songs, which showed the numerical features work independently. A weight shift experiment was also run, doubling energy importance and halving genre importance, which improved diversity and pushed high-energy songs into the conflicting profile results.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
