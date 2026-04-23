from pipeline import fetch_anime_by_genre
from aggregator import get_average_score
from database import initialize_db

def main():
    initialize_db()
    
    genres = {"action": 1, "comedy": 4, "romance": 22}
    
    action_anime = fetch_anime_by_genre(genres["action"], 4)
    average_action_anime_score = get_average_score(action_anime)
    print("Average action anime score: ", average_action_anime_score)
    
    comedy_anime = fetch_anime_by_genre(genres["comedy"], 4)
    average_comedy_anime_score = get_average_score(comedy_anime)
    print("Average comedy anime score: ", average_comedy_anime_score)
    
    romance_anime = fetch_anime_by_genre(genres["romance"], 4)
    average_romance_anime_score = get_average_score(romance_anime)
    print("Average romance anime score: ", average_romance_anime_score)

if __name__ == "__main__":
    main()