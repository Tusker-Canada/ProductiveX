from flask import Flask, render_template, request
from storage import storage
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=fd4106558c6a414c9701aef360fc932f')
response = requests.get(url)




app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/news')
def news():
  articles = response.json()["articles"]
  return render_template('news.html',articles= articles)

@app.route('/s')
def s():
  articles = response.json()["articles"]
  return render_template('sadasd.html')


@app.route('/todo', methods = ['POST','GET'])
def todo():
  if request.method == 'GET':
    return render_template('todo.html',items = storage)
  if request.method == 'POST':
    result = request.form.items()
    for i, y in result:
      storage.append(y)
    return render_template('todo.html',items = storage)

@app.route('/delete', methods = ['POST','GET'])
def delete():
  if request.method == 'GET':
    return render_template('todo.html')
  if request.method == 'POST':
    result = request.form.items()
    for i, y in result:
      storage.remove(y)
    return render_template('todo.html',items = storage)

@app.route('/finished', methods = ['POST','GET'])
def finished():
  if request.method == 'GET':
    return render_template('todo.html')
  if request.method == 'POST':
    result = request.form.items()
    for i, y in result:
      storage.remove(y)
    return render_template('todo.html',items = list)

if __name__ == "__main__":
  app.run(port=3000)
