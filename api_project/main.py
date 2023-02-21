from flask import Flask , render_template , request
from apifetch import fetch_current
app = Flask(__name__)

@app.route('/' , methods =["GET", "POST"])
def fetch():
    if request.method == "POST":
        query = request.form.get("city")
        print(query)
        data = fetch_current(query)
        # print(data)
        return render_template("index.html" , data = data)
    data = fetch_current("london")
    return render_template("index.html",data = data)
app.run(debug = True)