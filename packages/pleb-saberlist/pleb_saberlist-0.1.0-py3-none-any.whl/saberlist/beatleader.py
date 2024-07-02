import requests
import json

# Specify the URL
blee_id = '76561199407393962'
#url = f'https://api.beatleader.xyz/player/{blee_id}/rankedMaps'
url = f'https://api.beatleader.xyz/player/{blee_id}/scores'

response = requests.get(url)

response_content = json.loads(response.content)
