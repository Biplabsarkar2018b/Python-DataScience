import requests
# session = requests.Session()
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/result",methods= ["POST","GET"])
def result():
    web_url = request.form["web-url"]
    r = requests.get(web_url)
    print(web_url)
    web_url = r.cookies.get_dict()
    print(web_url)
    return render_template("index.html",web_url=web_url)

if __name__ == "__main__":
    app.run(debug=True,port=5555)



