import re
from collections import Counter
import pandas as pd

# دامنه‌های شناختی و کلمات کلیدی متناظر بر اساس کدبوک MMM
schema_lexicon = {
    'VERTICALITY': ['high', 'sky', 'down', 'fall', 'top', 'up', 'drop', 'space', 'climb'],
    'CONTAINER': ['in', 'inside', 'out', 'room', 'box', 'cage', 'closed', 'eyes', 'head'],
    'FORCE': ['push', 'pull', 'crash', 'smash', 'hit', 'break', 'run', 'drive', 'stop'],
    'PATH': ['way', 'road', 'walk', 'travel', 'ahead', 'line', 'track', 'lead']
}

sample_lyrics = """
Situation. We ought to be. I am loyal bitch I got ye.
Look in my eyes tell me a tale do you see the road?
Goin up high can you feel the fall out of the cold.
Friction against the wall sirens breaking through.
"""

tokens = re.findall(r'\b[a-zA-Z]+\b', sample_lyrics.lower())
counts = Counter(tokens)

findings = []
for schema, words in schema_lexicon.items():
    matched = {w: counts[w] for w in words if w in counts}
    total = sum(matched.values())
    findings.append({
        'schema': schema,
        'matched_words': ', '.join([f"{k} ({v})" for k, v in matched.items()]),
        'activation_count': total
    })

df_lyrics = pd.DataFrame(findings)
df_lyrics.to_csv("[/mnt/data/lyrics_schema_mapping.csv"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzN0KgjAYANB32XWT5ZS2bsOSQrqKEoLx9W06c_7OhIrePR_gnC95eTOSLZnDANLLbkoiLW9pfnanXGb2QNOE2Rk_tWueAz1eJe34kKHYb8qErAhamNTU1aZdikcRAcaaUc1ETCMuBAXBOZUMZagNX2vQiykqZ1QPk12Ie48VeuXRmgZUA31ftWWAfr4T8vsD6S4xtg:1xLunK:N8yAwAtLz3Qxf96HeBs5p4eUkykh7EVJourAmV854lI/lyrics_schema_mapping.csv%22), index=False)
print("Lyrics schema mapping saved to lyrics_schema_mapping.csv")
