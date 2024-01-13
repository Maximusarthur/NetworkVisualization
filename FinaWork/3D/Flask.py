from flask import render_template, Flask
import pandas as pd

app = Flask(__name__)


@app.route("/")
def show():
    data = pd.read_csv("3D.csv")
    data = data.to_dict(orient="records")
    return render_template("3D.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
