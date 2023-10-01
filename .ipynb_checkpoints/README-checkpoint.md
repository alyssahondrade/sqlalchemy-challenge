# sqlalchemy-challenge
Module 10 Challenge

Github repository at: [https://github.com/alyssahondrade/sqlalchemy-challenge.git](https://github.com/alyssahondrade/sqlalchemy-challenge.git)

## Table of Contents
1. [Introduction](https://github.com/alyssahondrade/sqlalchemy-challenge#introduction)
    1. [Goal](https://github.com/alyssahondrade/sqlalchemy-challenge#goal)
    2. [Repository Structure](https://github.com/alyssahondrade/sqlalchemy-challenge#repository-structure)
    3. [Dataset](https://github.com/alyssahondrade/sqlalchemy-challenge#dataset)
2. [Approach](https://github.com/alyssahondrade/sqlalchemy-challenge#approach)
    1. [Setup](https://github.com/alyssahondrade/sqlalchemy-challenge#setup)
    2. [Part 1](https://github.com/alyssahondrade/sqlalchemy-challenge#part-1)
       1. [Reflect Tables into SQLAlchemy ORM](https://github.com/alyssahondrade/sqlalchemy-challenge#reflect-tables-into-sqlalchemy-orm)
       2. [Exploratory Precipitation Analysis](https://github.com/alyssahondrade/sqlalchemy-challenge#exploratory-precipitation-analysis)
       3. [Exploratory Station Analysis](https://github.com/alyssahondrade/sqlalchemy-challenge#exploratory-station-analysis)
    3. [Part 2](https://github.com/alyssahondrade/sqlalchemy-challenge#part-2)
3. [References](https://github.com/alyssahondrade/sqlalchemy-challenge#references)

## Introduction

### Goal
The goal of this project is to conduct a climate analysis of Honolulu, Hawaii, and create a Flask API to return the analysis information.

### Repository Structure
Source code:
- [`app.py`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/app.py) contains the code that builds the Flask API.

- [`climate_starter.ipynb`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/climate_starter.ipynb) contains the exploratory analysis on the dataset.

`Resources` directory contains:
- [`hawaii.sqlite`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) is the database.

- [`hawaii_measurements.csv`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/Resources/hawaii_measurements.csv) contains the measurement dataset.

- [`hawaii_stations.csv`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/Resources/hawaii_stations.csv) contains the station dataset.

### Dataset
The dataset is provided by the bootcamp, sourced from:

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

## Approach
### Setup
1. Create a new repository on Github.

2. Copy the link: [https://github.com/alyssahondrade/sqlalchemy-challenge.git](https://github.com/alyssahondrade/sqlalchemy-challenge.git)

3. Open terminal and navigate to the folder that will contain the local repository.

4. Use `git clone <link_url.git>` to clone a copy of the repository to your local machine.

5. Add the starter code to the folder then use:

    `git add .`
   
    `git commit -m <commit_message>`
   
    `git push origin main`

### Part 1
#### Reflect Tables into SQLAlchemy ORM
1. Create the engine to the `hawaii.sqlite` using: `create_engine()`

2. Reflecting an existing database using: `automap_base()`

3. Reflect the tables using: `Base.prepare()`

4. View all the classes that automap found using: `inspect(engine).get_table_names()`

5. Save the references to each table using: `Base.classes.<table_name>`

6. Create the session link from Python to the database using: `Session()`

#### Exploratory Precipitation Analysis
1. Create a printout of the column names for `measurement` and `station`.

2. Find the most recent date in the dataset.
    - Use `func.max()` to get the latest date.
    - Use `.one()` since only expecting one result.

3. Parse the date string and create a datetime object.
    - Use `split()` string method.
    - Use `dt.datetime()` to convert to datetime object.

4. Perform a query to retrieve the `date` and `precipitation` scores ONLY.
    - Use the variable that calculates the date one year from the latest date: `year_ago`.
    - Pass a `timedelta(days=366)` to ensure the date lands on the same day and month, but one year prior (i.e. `2016-08-23` to `2017-08-23`).

5. Save the query results to a Pandas DataFrame, explicitly setting the column names.
    - Drop `NaN` values using: `dropna(how='any')`

6. Use Pandas plotting to plot the data.
    - Calculate the x-tick frequency to display `5` dates along the x-axis.
    - Calculate the corresponding x-tick labels.
    - Use `df.plot()` to create the plot
    - Set the x-tick labels using: `set_xticklabels()`
    - Relocate the legend using: `legend(loc='upper center')`

#### Exploratory Station Analysis
1. Design a query to calculate the total number of stations using: `func.count()`

2. Design a query to find the most active stations (most data points).
    - Use `group_by()` to get the results per station.
    - Use `order_by()` to display the results in descending order.

3. Using the most active station id, calculate the lowest, highest, and average temperature.
    - Use: `func.min()`, `func.avg()`, and `func.max()`
    - Use `filter()` given the most active station id.

4. Query the last 12 months of temperature observation and create a histogram.
    - Use the `year_ago` variable calculated earlier to minimise code repetition.
    - Create a histogram with `bins=12`.
    - Ensure correct title, labels, and legend.

### Part 2
1. SQLite Connection: as with __Reflect Tables into SQLAlchemy ORM__ in Part 1 above.

2. Create a helper function to minimise code repetition: `year_ago()` to calculate one year from the latest date.

3. API Static Routes: Use `jsonify()` in all return clauses.
    - __Homepage__: List all available routes.
    - __Precipitation Route__:
        - Query to retrieve the date and precipitation scores.
        - Convert to a dictionary, with the `date` as the key and `prcp` as the value.
    - __Stations Route__:
        - Query to get the data of all stations.
        - Convert query results to a dictionary - provide all columns.
    - __TOBS Route__:
        - Query to find the most active station for the previous year.
        - Convert to a dictionary, to return a list of temperature observations for the previous year.

4. API Dynamic Routes:
    - Define a global variable: `select_columns` to minimise code repetition.
    - __Start Route__:
        - Query to find the min, ave, and max TOBS given `<start>` as a parameter.
        - Convert query results to a dictionary, as with the __Stations Route__.
    - __Start/End Route__: As with the __Start Route__ with an additional parameter `<end>`.

## References
- [1] Python unpacking operators [https://hyperskill.org/learn/step/15401](https://hyperskill.org/learn/step/15401)

- [2] Python Programming Style: Module Comments [https://www.cs.cornell.edu/courses/cs1110/2022fa/materials/style/](https://www.cs.cornell.edu/courses/cs1110/2022fa/materials/style/)

- [3] Can Flask have optional URL parameters? [https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters](https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters)