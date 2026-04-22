import requests

def fetch_top_anime(pages):
    result = []
    
    for page in range(pages):
        try:
            response = requests.get(f'https://api.jikan.moe/v4/top/anime?page={page+1}')
            body = response.json()
            result.extend(body["data"])
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
    for anime in result:
        print(anime["mal_id"])

def main():
    fetch_top_anime(2)

if __name__ == "__main__":
    main()