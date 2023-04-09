
from flask import Flask, render_template

app = Flask(__name__, template_folder='Template', static_folder="static")

travel_buddy= [{"location":"Rishikesh","budget":"RS-25000","start_date":"25-nov-2023"},
               {"location": "badrinath","budget":"RS-35000","start_date":"26-nov-2023"},
               {"location": "somanth","budget":"RS-10000","start_date":"17-nov-2023"}]


@app.route('/')
def index():
    return render_template("first.html",travel_buddy=travel_buddy)

if __name__ == '__main__':
    app.run(debug=True)

