import requests
from utils.fileUtils import FileUtils

authToken = 'o6eTd3tQzWA1S5byrvYvSjvRjwX25fdSoMoNXkEQ'
url = 'https://ballchasing.com/api/'
replay1 = '68069a05-ab40-4129-a7f1-14001abb461c'

replays = '?player-name=Steam%3A76561198078218740&playlist=ranked-standard&season=f11'

headers = {
  'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, ' +
    'like Gecko) Chrome/102.0.5005.125 Safari/537.36',
  'Authorization': authToken
}

def get_replay(replayId: str) -> dict:
  response = requests.get(url + f'replays/{replayId}', headers=headers)
  FileUtils.save_replay_json(response.json(), replayId)

def get_replays(params: str):
  response = requests.get(url + f'replays/{params}', headers=headers)
  replaysJson = response.json()
  replayIds = [replay['id'] for replay in replaysJson['list']]
  [get_replay(replayId) for replayId in replayIds]



if __name__ == '__main__':
  #  ping_test()
  # get_replay(replay1)
  # get_replays(replays)

  # replay = FileUtils.load_replay('5b049348-3c6b-4062-a869-61aa9e009e0d')
  # print(type(replay))

  replays = FileUtils.load_replays()
  pass