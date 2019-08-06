from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return """
  <h1>Python Flask in Docker!</h1>
  <p>It is a Jenkins Test...BOOOOOMMMM</p>
  """
  
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='6000')

