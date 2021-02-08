# Getting Started:

Please clone the repository and make sure you have the following libraries installed. If not, please read include guide on how to install Python libraries
1. Flask v1.1.2
2. Flask-RESTful 0.3.8
3. Python requests library
4. Python re (regular expressions library)

#### How to install Python Libraries:
`pip install requests` to install **requests** library<br>
`pip install Flask` to install **Flask**. In case you have a problem installing Flask, Please visit https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask <br>
`pip install flask-restful` to install **Flask-RESTful**. Visit https://flask-restful.readthedocs.io/en/latest/installation.html for help.

Once the neccessary libraries are installed into the development environment,
1. Please run main.py to start the Flask server and app to start running the app
2. By default Flash runs on the local server at `localhost:5000` or ` http://127.0.0.1.5000` 
3. Please visit Flask documentation to know how to update the Base URL for the server.


Please pass parameters as a part of the URL.


##### GET

`/`

**Response**: Returns user points and data is unsorted

`/points` <br>
**Response**: Returns user points and data is sorted

`/deductions` <br>

**Response**: Returns points deducted while transactions are being added as Json

`/transactions`<br>

**Response** : Returns all the transactions so far as Json
<br>
Each value is a Key, Value pair of Transaction ID and List item as [Payer name, Points, Date]

`/deduct/<points>` <br>

Parameters: points to be deducted

**Response**: Returns number of points deducted from each Payer as a Json

#### POST
`/<payer>/<points>/<date>`

###### Parameters
Payer name, Points, and date<br>
Please pass the date as a string encoded in 
`YY%MM%DD%%HH%MM%[AM/PM]` format

### **What's working:**
1. Points balance is being updated properly
2. All transactions are being recorded
3. Deductions are being recorded.
4. Date can be sent as a string in the format 
