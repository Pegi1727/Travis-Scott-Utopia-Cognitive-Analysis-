import os
import librosa
import numpy as np
import pandas as pd

audio_files = {
    "HYAENA": "[/mnt/data/HYAENA](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/eyJ1c2VyIjoidjIuYUhVQ3RFNGQ5WEhZT2xLWTlNaEctSEUwaHZjemtsbWpxLUpXOS1vM3FNYzhGN2dFIiwiY2hhdF90b2tlbiI6ImJmNGFjNWQwLWQwODUtNDM4OC1hODMzLTkwYzkyZGUzMWRhZCIsImZpbGVfcGF0aCI6IkhZQUVOQSJ9:1xLunJ:OW4wp1GRixEEaNpxA4s4E3-U50ZU5qniFW9Txwu8wRA/HYAENA) - Travis Scott (320).mp3",
    "SIRENS": "[/mnt/data/travis_scott_sirens](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzEEOgjAQAMC_9OyaSiG2Xk2VaIgno5yatS0WQRC6ctD4d3nAzJe9ox_Zhk3JEvPzlnTq1DUvT-2xVEXYQ655mOynaZ-PAQ4XBb0YCit367tmC2YDkqG-8d1c3KoUbeY4OC4zSIWUgFIIUNyqxHmxcuhmU9WtNy-kMBMacaqjibYnMrEefRfZ7w9mCC8l:1xLunJ:pX5NjUdECVKW2McMNZ1c3wOhVqzsyBJFMvYzP81iMGM/travis_scott_sirens) 128.mp3"
}

results = []

for track_name, path in audio_files.items():
    if not os.path.exists(path):
        continue
    y, sr = librosa.load(path, sr=22050, duration=180)  # تحلیل ۳ دقیقه اول
    
    # استخراج شاخص‌ها
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)[0]
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    zcr = librosa.feature.zero_crossing_rate(y=y)[0]
    
    results.append({
        "track": track_name,
        "estimated_tempo_bpm": float(tempo),
        "mean_rms_energy": float(np.mean(rms)),
        "std_rms_energy": float(np.std(rms)),
        "mean_spectral_centroid_hz": float(np.mean(centroid)),
        "std_spectral_centroid_hz": float(np.std(centroid)),
        "mean_zcr": float(np.mean(zcr))
    })

df = pd.DataFrame(results)
df.to_csv("[/mnt/data/extracted_acoustic_metrics.csv"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzNEKgjAUANB_2XOT5ZS2XsOSQnqKEgK53c1maqa7ShT9e37AOV82ejuwNZvCANLThpLI6EuaH5tDrjO342ki3ISfumkfPd-fNe9kn6Haru4JWzB0QAV1tX3Oxa2MAGMjuBEq5pFUioOSkmuBOjRWLg2Y2ZRVY4sXkJuJfdMASNYUgN3oqcKitTRU6AP005Wx3x_sPjPZ:1xLunJ:26-n__kdMHruqUeoXedlZRNpq0Lxg4PvspX_xqUJBS4/extracted_acoustic_metrics.csv%22), index=False)
print("Acoustic extraction complete. Saved to extracted_acoustic_metrics.csv")
