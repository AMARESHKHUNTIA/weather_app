from flask import Flask ,render_template, request
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/submit',methods=['GET','POST'])
def weather_report():
    url='https://api.openweathermap.org/data/2.5/weather'
    param={
        'q':request.form.get('city'),
        'appid':"beb88d95997583a59b470c1ddbddce0e",
        'units':request.form.get('unit')
    }
    response=requests.post(url=url,params=param)
    data=response.json()
    return f'data: {data}'

if __name__==('__main__'):
    app.run(host='0.0.0.0',port=5002)


