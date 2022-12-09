from flask import Flask

app = Flask(__name__)

# route
@app.route('/')
# route function
def home():
  # send 'hey!'
  return 'hey!'

# listen
if __name__ == "__main__":
  app.run(port=3000)
  # if you need to make it live debuging add 'debug=True'
  # app.run(port=3000, debug=True)
  
 # Hope you enjoyed ;)
