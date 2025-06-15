
import requests

def fetch_cover(title):
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}"
    response = requests.get(url)
    try:
        data = response.json()
        return data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    except:
        return "https://via.placeholder.com/150"  # default fallback
