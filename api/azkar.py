from flask import Flask, request, redirect, session, url_for, render_template
from random import choice
from json import load, dump, loads, dumps
from requests import get

from load_azkar import load_azkar, get_zekr, get_zekr_handler

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://github.com/nawafalqari/azkar-api')


@app.route('/zekr')
def zekr():
    return get_zekr_handler(request.args)

app.run(debug=True)
