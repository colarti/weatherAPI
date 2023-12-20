from flask import Flask, render_template
import pandas
from extract import extractZip
import os
from datetime import datetime


def getFile(id, dir):
    for file in os.listdir(dir):
        name = file.split('.')[0]
        try:
            name = name.split('TG_STAID')[1]
            idx = str(int(name))
            if idx == id:
                return f'{dir}{file}'
        except:
            pass
    return None

def checkDate(date):
    try:
        status = bool(datetime.strptime(date, '%Y%m%d'))
    except:
        status = False

    return status

def getTemp(file, date, cel=True):
    df = pandas.read_csv(file, skiprows=20, parse_dates=['    DATE'])
    
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    if cel:
        pass
    else:
        temp = temp * (9/5) + 32
    
    print(f'TEMP: {temp}')
    return temp

#-------------------------------------------------------------------------------



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    file = getFile(station, 'data_small\\')
    dateCheck = checkDate(date)
    print(f'FILE: {file}   DATE: {date}')


    if file is None:
        print(f'Station {station}  -- doesnt exist')
        return {'station':None, 'date':date, 'temp':None}
    
    if dateCheck is False:
        print(f'Date {date} in invalid')
        return {'station':station, 'date':None, 'temp':None}
    
    temp = getTemp(file, date)
    return {'station':station, 'date':date, 'temp':temp}
        


if __name__ == '__main__':
    if os.path.exists('data_small'):
        pass
    else:
        extractZip('data_small.zip', '.\\data_small\\')


    app.run(debug=True, port=5002)