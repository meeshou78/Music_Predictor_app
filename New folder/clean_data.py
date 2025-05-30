# File: clean_data.py
import pandas as pd

# Load raw dataset
sdata = pd.read_csv("raw_songs.csv")  # Replace with your actual raw file name

# 1. Standardize text columns
sdata['track_genre'] = sdata['track_genre'].str.strip().str.lower()

# 2. Convert popularity to binary label (top 25% = popular)
sdata['popularity_label'] = (sdata['popularity'] > 75).astype(int)

# 3. Drop rows with missing critical values
sdata = sdata.dropna()

# 4. Normalize loudness (convert from dB to [0-1])
sdata['loudness'] = (sdata['loudness'] - sdata['loudness'].min()) / (sdata['loudness'].max() - sdata['loudness'].min())

# 5. Normalize tempo
sdata['tempo'] = (sdata['tempo'] - sdata['tempo'].min()) / (sdata['tempo'].max() - sdata['tempo'].min())

# 6. Drop track_id
sdata = sdata.drop(columns=['track_id'])

# 7. Drop songs with popularity of 0
sdata = sdata[sdata['popularity'] != 0]

# 8. Convert duration from milliseconds to minutes
sdata['duration'] = sdata['duration_ms'] / 60000

# 9. Remove duplicates
sdata = sdata.drop_duplicates()

# 10. Drop non-numeric / unused columns
sdata_clean = sdata.drop(columns=[
    'artists', 'album_name', 'track_name',
    'popularity_bin', 'track_genre', 'duration_ms', 'time_signature'
], errors='ignore')

# 11. Save to file
sdata_clean.to_csv("cleaned_songs.csv", index=False)
print("✅ cleaned_songs.csv saved!")
print("Columns:", list(sdata_clean.columns))
