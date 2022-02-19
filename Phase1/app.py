#dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#9.5.1 set up database and flask

#SET UP DATABASE
#access database
engine = create_engine("sqlite:///hawaii.sqlite")
#reflect the db into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#save references to each table/class
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from python to database
session = Session(engine)

#SET UP FLASK
#create a flask app instance
app = Flask(__name__)

#to run flask:
#open anaconda powershell and type
#"set FLASK_APP=app.py" and hit enter then type
#"flask run" and hit enter
#and use address provided to view page

#create WELCOME route 
@app.route("/")

#create function to reference f strings of other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#create precipitation route and function
@app.route("/api/v1.0/precipitation")
def precipitation():
   
    #one year ago from most recent date
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   
    #get date and precip from prev year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()

    #create dict w date key : precip value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)    
    
#create stations route and function
@app.route("/api/v1.0/stations")
def stations():
    
    #query to get all stations
    results = session.query(Station.station).all()
    
    #convert to a list
    stations = list(np.ravel(results))
    
    #return list as json
    return jsonify(stations=stations)

#create temperature route and function
@app.route("/api/v1.0/tobs")
def temp_monthly():
    
    #one year ago from most recent date
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    #query primary station for temp observations from previous year
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    
    #unravel into list
    temps = list(np.ravel(results))
    
    #convert list to JSON
    return jsonify(temps=temps)

#create statistics route and function with start and end dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#add parameters to function set to none
def stats(start=None, end=None):

    #query to get stats with list called SELect
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    #use if-not to query with SEL list
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        #unravel
        temps = list(np.ravel(results))
        #convert list to JSON
        return jsonify(temps=temps)
    
    #calculate statistics with start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)   
    
