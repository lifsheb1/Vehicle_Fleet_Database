# general controller for the entire app
# Nicole Kondrk


#! /usr/bin/python3


import psycopg2
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows
 
# app.py
app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

#handle navigation to about page
@app.route('/about-page', methods=['GET','POST'])
def aboutPageRender():
    return render_template('about-page.html')

# handle make POST and serve result web page
@app.route('/make-handler', methods=['POST'])
def make_handler():
    rows = connect("SELECT Make, Model, Initial_Cost, Lifetime_Cost, Annual_Cost, GHG_Emissions FROM view1 WHERE make = '" + request.form['make'] + "';")
    heads = ['Make', 'Model', 'Initial Cost', 'Lifetime Cost', 'Annual Cost', 'GHG_Emissions']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle engine POST and serve result web page
@app.route('/engine-handler', methods=['POST'])
def engine_handler():
    rows = connect("SELECT Make, Model, Engine, Yearv, Initial_Cost, Lifetime_Cost, Annual_Cost, GHG_Emissions FROM view1 WHERE engine = '" + request.form['engine'] + "';")
    heads = ['Make', 'Model', 'Engine', 'Year', 'Initial Cost', 'Lifetime Cost', 'Annual Cost', 'GHG_Emissions']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle emissions POST and serve result web page
@app.route('/emissions-handler', methods=['POST'])
def emissions_handler():
    rows = connect("SELECT Make, Model, Initial_Cost, Lifetime_Cost, Annual_Cost, GHG_Emissions, Time_Line FROM view1 WHERE GHG_Emissions BETWEEN " + request.form['lowEmission'] + "AND " + request.form['highEmission'] + "ORDER BY GHG_Emissions;")
    heads = ['Make', 'Model', 'Initial Cost', 'Lifetime Cost', 'Annual Cost', 'GHG_Emissions', 'Timeline']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle year POST and serve result web page
@app.route('/year-handler', methods=['POST'])
def year_handler():
    rows = connect("SELECT Make, Model, Initial_Cost, Lifetime_Cost, Annual_Cost, GHG_Emissions, Yearv, Time_Line FROM view1 WHERE Yearv BETWEEN " + request.form['startYear'] + "AND " + request.form['endYear'] + "ORDER BY Yearv;")
    heads = ['Make', 'Model', 'Initial Cost', 'Lifetime Cost', 'Annual Cost', 'GHG_Emissions', 'Year', 'Timeline']
    return render_template('my-result.html', rows=rows, heads=heads)

if __name__ == '__main__':
    app.run(debug = True)
