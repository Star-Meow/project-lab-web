# core.py
from flask import Flask, render_template, jsonify,request
from fakedata import test,fakedata
import sqlite3

DB_File = "player_db.db"
app = Flask(__name__)

frame_counter = 0
data_cache = None

@app.route('/')
def index():
    return render_template('index.html')

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
    number = []
    has_ball = []
    x_coor = []
    y_coor = []
    frame = []
    data = []
    conn = sqlite3.connect(DB_File)
    c = conn.cursor()
    cursor =c.execute("SELECT round(number),round(has_ball),round(x_coor),round(y_coor),substr(Frame,1,16)FROM players ORDER BY Frame DESC LIMIT 10")
    result = cursor.fetchall()
    for result in result:
        data.append(result)
    
    conn.commit()
    cursor.close()
    conn.close()
    for i in range(10):
        try:
            number.append(int(data[i][0]))
        except:
            number.append("none")
        try:
            has_ball.append(int(data[i][1]))
        except:
            has_ball.append("none")
        try:
            x_coor.append(int(data[i][2]))
        except:
            x_coor.append("none")
        try:
            y_coor.append(int(data[i][3]))
        except:
            y_coor.append("none")
        try:
            frame.append(str(data[i][4]))
        except:
            frame.append("none")
    
    ans = {'number':number,"has_ball":has_ball,"x_coor":x_coor,"y_coor":y_coor,"frame":frame}
    
    return jsonify(ans)




@app.route('/data2')
def data2():
    global frame_counter
    frame_counter += 1
    if frame_counter > 296:
        frame_counter = 0
    data = fakedata(frame_counter)
    ans = {'number': data[0], "has_ball": data[1], "x_coor": data[2],
           "y_coor": data[3], "frame": data[4]}
    print(frame_counter)
    return jsonify(ans)

@app.route('/check')  #確認ajax有沒有抓到/data的json
def check():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
