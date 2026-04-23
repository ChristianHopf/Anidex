# Computes the average score of a given list of anime
# - anime_list: list of dicts
def get_average_score(anime_list):
    n = len(anime_list)
    score_sum = 0
    
    for i in range(n):
        score_sum += anime_list[i]["score"]
    
    average_score = score_sum / n
    # print(f"{average_score:.3f}")
    
    return round(average_score, 3)