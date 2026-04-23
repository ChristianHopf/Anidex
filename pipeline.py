import time
import requests

def fetch_top_anime(pages):
    result = []
    
    # Fetch a page of information and add to the end of the list
    for page in range(pages):
        try:
            response = requests.get(f'https://api.jikan.moe/v4/top/anime?page={page+1}')
            response.raise_for_status()
            
            body = response.json()
            result.extend(body["data"])
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
        # Jikan limits usage to 60 requests per minute
        time.sleep(1)

    return result

# Fetches 25 anime per page with the given genre
# - genre: integer
# - pages: integer
def fetch_anime_by_genre(genre, pages):
    result = []
    # Fetch a page of information and add to the end of the list
    for page in range(pages):
        try:
            response = requests.get(f'https://api.jikan.moe/v4/anime?page={page+1}&genres={genre}')
            response.raise_for_status()
            
            body = response.json()
            result.extend(body["data"])
            
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
        # Jikan limits usage to 60 requests per minute
        time.sleep(1)

    return result

# Computes the average score of a given list of anime
# - anime_list: list of dicts
def get_average_score(anime_list):
    scored_list = [anime for anime in anime_list if anime["score"] is not None]
    n = len(anime_list)
    score_sum = 0
    
    for anime in scored_list:
        score_sum += anime["score"]
    
    average_score = score_sum / n
    # print(f"{average_score:.3f}")
    
    return round(average_score, 3)