from flask import Flask, request, redirect, session, url_for, render_template
from random import choice
from json import load, dump, loads, dumps
from requests import get

app = Flask(__name__)

with open('azkar.json', 'r', encoding='utf-8') as file:
  file_data = load(file)

def get_zekr(type:str='random'):
  types = list(file_data.keys())
  if type == 'random':
    return choice(file_data[choice(types)])
  if type in types:
    return choice(file_data[types[types.index(type)]])

  return choice(file_data[choice(types)])

@app.route('/')
def index():
  return 'zkr'

@app.route('/zekr')
def zekr():
  # zkr = dumps(get_zekr(), ensure_ascii=False)
  args = request.args

  if len(args) != 0:
    if len(args) == 1 and args.get('json') == 'true':
      return f'{dumps(get_zekr(), ensure_ascii=False)}'

    # morning  
    elif len(args) == 1 and (args.get('m') == 'true' or args.get('morning') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('أذكار الصباح'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('m') == 'true' or args.get('morning') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("أذكار الصباح"), ensure_ascii=False)}'

    # evening
    elif len(args) == 1 and (args.get('e') == 'true' or args.get('evening') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('أذكار المساء'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('e') == 'true' or args.get('evening') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("أذكار المساء"), ensure_ascii=False)}'

    # after salah
    elif len(args) == 1 and (args.get('as') == 'true' or args.get('aftersalah') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('أذكار بعد السلام من الصلاة المفروضة'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('as') == 'true' or args.get('aftersalah') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("أذكار بعد السلام من الصلاة المفروضة"), ensure_ascii=False)}'

    # tsabeh
    elif len(args) == 1 and (args.get('t') == 'true' or args.get('tsabeh') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('تسابيح'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('t') == 'true' or args.get('tsabeh') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("تسابيح"), ensure_ascii=False)}'
    
    # before sleeping
    elif len(args) == 1 and (args.get('bs') == 'true' or args.get('beforesleeping') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('أذكار النوم'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('bs') == 'true' or args.get('beforesleeping') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("أذكار النوم"), ensure_ascii=False)}'
    
    # after sleeping
    elif len(args) == 1 and (args.get('wu') == 'true' or args.get('wakingup') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('أذكار الاستيقاظ'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('wu') == 'true' or args.get('wakingup') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("أذكار الاستيقاظ"), ensure_ascii=False)}'
    
    # quranic duas
    elif len(args) == 1 and (args.get('qd') == 'true' or args.get('quranicduas') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('أدعية قرآنية'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('qd') == 'true' or args.get('quranicduas') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("أدعية قرآنية"), ensure_ascii=False)}'

    # prophets duas
    elif len(args) == 1 and (args.get('pd') == 'true' or args.get('prophetsduas') == 'true'):
      return render_template('zekr.html', zekr=loads(dumps(get_zekr('أدعية الأنبياء'), ensure_ascii=False)))
    elif len(args) == 2 and ((args.get('pd') == 'true' or args.get('prophetsduas') == 'true') and (args.get('json') == 'true')):
      return f'{dumps(get_zekr("أدعية الأنبياء"), ensure_ascii=False)}'
    
    else:
      return f'"ERROR" Unknown parameter'
    
  return render_template('zekr.html', zekr=loads(dumps(get_zekr(), ensure_ascii=False)))
  
app.run(debug=True)
