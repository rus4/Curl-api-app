import mysql.connector
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Connect to the MySQL database
database = mysql.connector.connect(
    host='localhost',
    user='user',
    password='password',
    database='database'
)
cursor = database.cursor()

@app.route('/submit_curl_command', methods=['POST'])
def submit_curl_command():
    # Get the curl command from the request body
    curl_command = request.form['curl_command']

    # Execute the curl command
    output = subprocess.check_output(curl_command, shell=True)

    # Insert the current date-time stamp into the database
    sql = 'INSERT INTO curl_commands (datetime) VALUES (NOW())'
    cursor.execute(sql)
    database.commit()

    # Return the output of the curl command in the response
    return output

if __name__ == '__main__':
    app.run()
