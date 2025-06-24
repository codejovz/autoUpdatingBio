import requests
import os
from datetime import datetime
from pytz import timezone

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
  
def update_bio():
  madrid_tz = timezone('Europe/Madrid')
  baseBio = 'Cross-Platform Development (DAM) dev. I have a verifiable B2 level of English and the High School Diploma.'
  hora_actual = datetime.now(madrid_tz).hour
  if 6 <= hora_actual < 14:
    biog = baseBio + ' Full of energies!'
  elif 14 <= hora_actual < 21:
    biog = baseBio + ' Probably crafting some code rn!'
  else:
    biog = baseBio + ' Sleeping rn...'
  print(biog)
  url = 'https://api.github.com/user'
  headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
  }
  data = {'bio': biog}
  response = requests.patch(url, headers=headers, json=data)
  if response.status_code == 200:
    print('Biography updated successfully.')
  else:
    print(f'Error while trying to change biography: {response.status_code} - {response.text}')
  
update_bio()
