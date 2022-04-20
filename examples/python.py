from requests import get

zekr = get('https://azkar.ml/zekr?json=true').json() # Type = dict
print(zekr['content'])