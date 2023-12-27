# core.py
from flask import Flask, render_template, jsonify,request
from fakedata import *
from demodata import *
import sqlite3

DB_File = "player_db.db"
app = Flask(__name__)

frame_counter = 0
field_ct = 0
pic_ct = 1
data_cache = None

@app.route('/')
def index():
    return render_template('info.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/field')
def field():

    return render_template('field.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/about')
def about_us():
    return render_template('aboutus.html')

@app.route('/use')
def use():
    return render_template('use.html')

@app.route('/data')  #直接確認json
def data():
    global field_ct
    field_ct += 1
    if field_ct > 6:
        field_ct = 0
    fieldans = {'pic_ct': field_ct}
    return jsonify(fieldans)

@app.route('/data2')
def data2():
    global frame_counter
    frame_counter += 1
    if frame_counter > 294:
        frame_counter = 0
    data = demo(frame_counter)
    ans = {'number': data[0], "has_ball": data[1], "x_coor": data[2],
           "y_coor": data[3], "frame": data[4]}
    print(frame_counter)
    return jsonify(ans)


@app.route('/check')  #確認ajax有沒有抓到/data的json
def check():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
