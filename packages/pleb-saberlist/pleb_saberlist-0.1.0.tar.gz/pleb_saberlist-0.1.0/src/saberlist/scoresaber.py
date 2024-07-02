import json
import asyncio
from pyscoresaber import ScoreSaberAPI, ScoreSort
import requests

def filter_and_sort_scores_by_stars(scores, min_stars=0.1, max_stars=float('inf')):
    # Exclude scores outside the specified star range
    filtered_scores = [score for score in scores if min_stars <= score.leaderboard.stars < max_stars]
    # Sort the remaining scores by stars
    sorted_scores = sorted(filtered_scores, key=lambda x: x.leaderboard.stars)
    return sorted_scores

def scores_to_playlist(scores, playlist_title, playlist_author = "SaberList Tool"):
    playlist = {
        "playlistTitle": playlist_title,
        "playlistAuthor": playlist_author,
        "songs": []
    }

    for score in scores:
        song_entry = {
            "hash": score.leaderboard.song_hash,
            "songName": score.leaderboard.song_name,
            "difficulties": [
                {
                    "name": score.leaderboard.difficulty.difficulty.name.lower(),
                    "characteristic": score.leaderboard.difficulty.game_mode.name.lower()
                }
            ],
            "levelAuthorName": score.leaderboard.level_author_name
        }
        playlist["songs"].append(song_entry)
    

    playlist_json = json.dumps(playlist, indent=4)
    with open(f"{playlist_title}.json", 'w') as file:
        file.write(playlist_json)

    return playlist_json

async def async_replay_ranked():
    scoresaber = ScoreSaberAPI()
    try:
        await scoresaber.start()  # Initialize the API client
        
        score_sort = ScoreSort.TOP
        scores = []
        default_player_id = '76561199407393962'
        player_id = input(f"Enter the playerid (Default: {default_player_id}): ") or default_player_id
        default_min_stars = 5
        min_stars = float(input(f"Enter the minimum starlevel to include on the playlist (Default: {default_min_stars}): ") or default_min_stars)
        default_max_stars = min_stars + 1
        max_stars = float(input(f"Enter the maximum starlevel to include on the playlist (Default: {default_max_stars}): ") or default_max_stars)
        default_title = f"Replay SS {min_stars}★"
        playlist_title = input(f"Enter the filename for the playlist (Default: {default_title}): ") or default_title

        async for player_scores in scoresaber.player_scores_all(player_id, score_sort):
            scores.extend(player_scores)

        filtered_sorted_scores = filter_and_sort_scores_by_stars(scores, min_stars, max_stars)
        scores_to_playlist(filtered_sorted_scores, playlist_title)
    finally:
        await scoresaber._http_client.close()  # Ensure the session is closed

def replay_ranked():
    try:
        asyncio.run(async_replay_ranked())
    except Exception as e:
        print(f"An error occurred: {e}")
