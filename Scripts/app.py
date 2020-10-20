from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
import json
from sqlalchemy import create_engine

app = Flask(__name__)

mongo = PyMongo(app, uri = "mongodb://localhost:27017/star_wars_app")

p_csv = "static/data/planets.csv"

###### mongo db ##########
p_df = pd.read_csv(p_csv)
p_df.to_json("p.json")
jdf = open("p.json").read()
p_data = json.loads(jdf)
mongo.db.collection.update({}, p_data, upsert = True)

### sqlite ####

sqlite_engine = create_engine('sqlite:///star_wars_db.sqlite')

# p_df.to_sql("planets", sqlite_engine)



@app.route("/")
def home():

    star = mongo.db.collection.find_one()
    return render_template("index.html", star = star)


@app.route("/planets")
def planets():
    return render_template("planets.html")

@app.route("/species")
def species():
    return render_template("species.html")

@app.route("/starships")
def starships():
    return render_template("starships.html")

@app.route("/vehicles")
def vehicles():
    return render_template("vehicles.html")

@app.route('/api/v1.0/data')
def apiV10():

    return mongo.db.collection.find_one()


if __name__ == "__main__":
    app.run(debug=True)

