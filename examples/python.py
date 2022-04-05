from requests import get

zekr = get('https://azkar-api.nawafhq.repl.co/zekr?json=true').json() # Type = dict
print(zekr['content'])