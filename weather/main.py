from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/temp', methods=['POST'])
def temp():

    locate = request.form['city']

    url = 'https://www.worldweatheronline.com/'+locate+'-weather/new-jersey/us.aspx'

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')



    temp_f = soup.find('div', class_="report_text temperature").get_text()
    cond_f = soup.find('div', class_="report_text light_text").get_text()



    return render_template('temp.html', temp = temp_f, cond =cond_f)




@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
