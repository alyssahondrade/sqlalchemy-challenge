'''
Module Comment here
'''

#################################################
# Imports
#################################################
from flask import Flask, jsonify

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import datetime as dt

#################################################
# SQLITE CONNECTION
#################################################
# Create an engine for the hawaii.sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database into ORM classes
Base = automap_base()
Base.prepare(autoload_with = engine)

# Save references to the respective table
measurement_ref = Base.classes.measurement
station_ref = Base.classes.station

# Create a database session object
session = Session(bind=engine)

#################################################
# HELPER FUNCTION: year_ago()
#################################################
# Calculate one year from the latest date
def year_ago():
    # Find the most recent date in the dataset
    latest_date = session.query(func.max(measurement_ref.date)).one()

    # Parse the latest date, to create a datetime object
    date_string = latest_date[0].split('-')
    dt_date = dt.datetime(
        int(date_string[0]),
        int(date_string[1]),
        int(date_string[2]))

    # Calculate the date one year from the last date in the dataset
    year_from_latest = dt_date - dt.timedelta(days=366)

    return year_from_latest

#################################################
# GLOBAL VARIABLE: select_columns
#################################################
# Used in dynamic routes to minimise repetition (unpacking operator).
select_columns = [func.min(measurement_ref.tobs),
                  func.avg(measurement_ref.tobs),
                  func.max(measurement_ref.tobs)]

#################################################
# Flask Setup
app = Flask(__name__)
#################################################

#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    return(
        f"Welcome to the Honolulu Climate API!<br/><br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&ltstart&gt<br/>"
        f"/api/v1.0/&ltstart&gt/&ltend&gt<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query to retrieve the date and preceiptation scores
    precipitation = session.query(
        measurement_ref.date, measurement_ref.prcp).\
        filter(measurement_ref.date >= year_ago()).all()

    # Convert the query results to a dictionary
    prcp_dict = [{value[0]: value[1]} for value in precipitation]

    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Query to get data of all the stations in the database
    station_data = session.query(station_ref).all()

    # Convert query results to a dictionary
    station_dict = [{
        'ID': value.id,
        'Station': value.station,
        'Name': value.name,
        'Latitude': value.latitude,
        'Longitude': value.longitude,
        'Elevation': value.elevation} for value in station_data]

    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query to find the most active station for the previous year
    active_stations = session.query(
        measurement_ref.station, func.count(measurement_ref.id)).\
        group_by(measurement_ref.station).\
        order_by(func.count(measurement_ref.id).desc()).all()

    # Return the most active station id
    most_active = session.query(
        measurement_ref.date, measurement_ref.tobs).\
        filter(measurement_ref.station == active_stations[0][0]).\
        filter(measurement_ref.date >= year_ago()).all()

    # Convert the query results to a dictionary
    tobs_dict = [{value[0]: value[1]} for value in most_active]

    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>")
def start_only(start):
    # Query to find the min, ave, and max TOBS
    start_query = session.query(*select_columns).\
        filter(measurement_ref.date >= start).all()

    # Convert query results to a dictionary
    start_dict = [{
        'TMIN': start_query[0][0],
        'TAVG': start_query[0][1],
        'TMAX': start_query[0][2]}]

    return jsonify(start_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Query to find the min, ave, and max TOBS
    end_query = session.query(*select_columns).\
        filter(measurement_ref.date >= start).\
        filter(measurement_ref.date <= end).all()

    # Convert query results to a dictionary
    end_dict = [{
        'TMIN': end_query[0][0],
        'TAVG': end_query[0][1],
        'TMAX': end_query[0][2]}]
    
    return jsonify(end_dict)

if __name__ == "__main__":
    app.run(debug=True)