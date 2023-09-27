from flask import Flask, jsonify

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import datetime as dt

### SQLITE CONNECTION ###
# Create an engine for the hawaii.sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database into ORM classes
Base = automap_base()
Base.prepare(autoload_with = engine)

# Save references to the respective table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a database session object
session = Session(bind=engine)

### Precipitation Analysis ###
# Calculate the date one year from the last date in the dataset.
latest_date = session.query(func.max(Measurement.date)).one()
date_string = latest_date[0].split('-')

dt_date = dt.datetime(
    int(date_string[0]),
    int(date_string[1]),
    int(date_string[2]))

year_ago = dt_date - dt.timedelta(days=366)

# Query to retrieve the date and preceiptation scores
precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= year_ago).all()

# Convert the query results to a dictionary
# prcp_dict = [{'date': value[0], 'prcp': value[1]} for value in precipitation]
prcp_dict = [{value[0]: value[1]} for value in precipitation]

### Station Analysis ###
station_data = session.query(Station).all()
station_dict = [{
    'ID': value.id,
    'Station': value.station,
    'Name': value.name,
    'Latitude': value.latitude,
    'Longitude': value.longitude,
    'Elevation': value.elevation} for value in station_data]


### Flask Setup ###
app = Flask(__name__)

### Flask Routes ###
@app.route("/")
def homepage():
    return(
        f"Welcome to the Honolulu Climate API!<br/><br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation/<br/>"
        f"/api/v1.0/stations/<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<end><br/>"
    )

@app.route("/api/v1.0/precipitation/")
def precipitation():
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations/")
def stations():
    return jsonify(station_dict)

if __name__ == "__main__":
    app.run(debug=True)