from flask import Flask, render_template, request, redirect
from storage import storage, counter, completed_tasks, events, videos
import datetime
import requests
import re
import urllib




url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=fd4106558c6a414c9701aef360fc932f')
response = requests.get(url)

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/home')

@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/news')
def news():
  articles = response.json()["articles"]
  return render_template('news.html',articles= articles)



@app.route('/todo', methods = ['POST','GET'])
def todo():
  if request.method == 'GET':
    total = 0
    for value in counter:
      total += 1
    if len(completed_tasks) == 0:
      return render_template('todo.html',items = storage, counter_val = total, finished_items = ["You have not completed any tasks."] )
    return render_template('todo.html',items = storage, counter_val = total, finished_items = completed_tasks)
  if request.method == 'POST':
    result = request.form.items()
    x = datetime.datetime.now()
    for i, y in result:
      storage.append(y)
      event_data = {
      'id': len(events) + 1 ,
      'todo': y,
      'start': x.strftime("%Y-%m-%d"),
      'end': x.strftime("%Y-%m-%d")
    }
      events.append(event_data)
    total = 0
    for value in counter:
      total += 1
    print(storage)
    if len(completed_tasks) == 0:
      return render_template('todo.html',items = storage, counter_val = total, finished_items = ["You have not completed any tasks."] )
    return render_template('todo.html',items = storage, counter_val = total, finished_items = completed_tasks )

@app.route('/delete', methods = ['POST','GET'])
def delete():
  if request.method == 'GET':
    return redirect('/todo')
  if request.method == 'POST':
    result = request.form.items()
    for i, y in result:
      for value in events:
        if value["todo"] == y:
          storage.remove(y)
          id = int(value["id"])
          for i in range(len(events)):
            if events[i]['id'] == id:
              print(i)
              del events[i]
              break
    total = 0
    for value in counter:
      total += 1
    return redirect('/todo')

@app.route('/finished', methods = ['POST','GET'])
def finished():
  if request.method == 'GET':
    return redirect('/todo')
  if request.method == 'POST':
    result = request.form.items()
    

    for i, y in result:
      for value in events:
        if value["todo"] == y:
          storage.remove(y)
          id = int(value["id"])
          for i in range(len(events)):
            if events[i]['id'] == id:
              print(i)
              del events[i]
              completed_tasks.append(y)
              break
          
    counter.append(1)
    total = 0
    for value in counter:
      total += 1
    
    return redirect('/todo')


@app.route('/calendar', methods = ['POST','GET'])
def calender():
  if request.method == 'GET':
    return render_template("calendar.html", events = events)
  if request.method == 'POST':
    result = request.form
    event = result['event']
    start_date = result['start_date']
    end_date = result['end_date']
    event_data = {
      'id': len(events) + 1 ,
      'todo': event,
      'start': start_date,
      'end': end_date
    }
    events.append(event_data)

    return render_template("calendar.html", events = events)

@app.route('/event_delete', methods = ['POST','GET'])
def event_delete():
  if request.method == 'GET':
    return redirect('/calendar')
  if request.method == 'POST':
    result = request.form
    id = result["name"]
    id = int(id)
    print(events[0])
    for i in range(len(events)):
      if events[i]['id'] == id:
        print(i)
        del events[i]
        break

    print(events)
    return redirect('/calendar')




@app.route('/courses', methods = ['POST','GET'])
def courses():

  if request.method == "GET":
    return render_template("courses.html", videos = videos, listLen = len(videos))
  if request.method == "POST":
    videos.clear()
    result = request.form
    for i in result:

      result1 = result[i]
      
      html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + 
  result1)

      video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

      video_ids = sorted(set(video_ids))

      
      i = 0
      for id in video_ids:
          i+=1
          if i < 5:
              x =id
              videos.append(x)
          else:
              break

    
    return render_template("courses.html", videos = videos, listLen = len(videos))


@app.route('/course_delete', methods = ['POST','GET'] )
def course_delete():
  if request.method == 'GET':
    return redirect('/courses')
  if request.method == "POST":
    videos.clear()
    return redirect('/courses')
  













if __name__ == "__main__":
  app.run(port=3000)
