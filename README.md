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
    3. [Part 2](https://github.com/alyssahondrade/sqlalchemy-challenge#part-2)
3. [References](https://github.com/alyssahondrade/sqlalchemy-challenge#references)

## Introduction

### Goal


### Repository Structure
Source code:
- [`app.py`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/app.py) contains...
- [`climate_starter.ipynb`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/climate_starter.ipynb) contains...

`Resources` directory contains:
- [`hawaii.sqlite`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) is the database.
- [`hawaii_measurements.csv`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/Resources/hawaii_measurements.csv) contains...
- [`hawaii_stations.csv`](https://github.com/alyssahondrade/sqlalchemy-challenge/blob/main/Resources/hawaii_stations.csv) contains...

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
2. Find the most recent date in the dataset using: `func.max()`
3. Parse the date string and create a datetime object.
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

### Part 2


## References
