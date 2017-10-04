
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Potato1234'
app.config['MYSQL_DB'] = 'STUDENTBOOK'
app.config['MYSQL_HOST'] = '35.195.111.210'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
# @app.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM STUDENTS''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/view_name")
def view_name():
    cur1 = mysql.connection.cursor()
    cur1.execute('''SELECT studentName FROM STUDENTS''')
    rv1 = cur1.fetchall()
    return str(rv1)

@app.route("/new_user/<name>")
def add_new(name): # add a new record
    cur3 = mysql.connection.cursor()
    cur3.execute('''INSERT INTO STUDENTS (studentName) VALUES (%s)''' % name)
    rv3 = cur3.fetchall()
    return str(rv3)


if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

