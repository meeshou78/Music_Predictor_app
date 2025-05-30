# File: test_post.py
import requests

url = "http://127.0.0.1:5000/"

# Construct complete feature dictionary (matching features.pkl order)
data = {
    "danceability": 0.6,
    "energy": 0.7,
    "valence": 0.5,
    "speechiness": 0.4,
    "acousticness": 0.3,
    "tempo": 0.8,
    "duration": 0.6
}

response = requests.post(url, data=data)
print("Status Code:", response.status_code)
print("Response Snippet:\n", response.text[:500])  # Print a preview
