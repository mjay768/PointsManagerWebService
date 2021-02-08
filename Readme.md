#Getting Started:




Please clone the repository and make sure you have the following libraries installed. If not, please read include guide on how to install Python libraries
1. Flask v1.1.2
2. Flask-RESTful 0.3.8
3. Python requests library
4. Python re (regular expressions library)

####How to install Python Libraries:
`pip install requests` to install **requests** library<br>
`pip install Flask` to install **Flask**. In case you have a problem installing Flask, 
Please visit https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask <br>
`pip install flask-restful` to install **Flask-RESTful**. Visit https://flask-restful.readthedocs.io/en/latest/installation.html for help.

##### GET

`/`

**Response**: Returns user points and data is unsorted

`/points` <br>
**Response**: Returns user points and data is sorted

`/deductions` <br>
**Response**: Returns points deducted while transactions are being added

`/transactions`<br>

**Response** : Returns all the transactions so far.

`/deduct/<points>` <br>

Parameters: points to be deducted

**Response**: Returns number of points deducted from each Payer

####POST
`/<payer>/<points>/<date>`

###### Parameters
Payer name, Points, and date in the format
`YY%MM%DD%%HH%MM%[AM/PM]`

### **What's working:**
1. Points balance is being updated properly
2. All transactions are being recorded
3. Deductions are being recorded.
4. Date can be sent as a string in the format 
