from flask import Flask
from flask_restful import Api, Resource, abort
import datetime
import re

# Defining a Flask app
app = Flask(__name__)
api = Api(app)



# Stores user points data
user_data = {}

# Used to track transactions as they are happening
tracker = {}

# Dictionary to keep track of the deductions happening during POST transactions
deduct_track = {}

# Retrieves the list of all transactions
@app.route('/transactions')
def getTransactions():
    tr = PointsManager()
    tr_dict = tr.setTransactions()
    del tr
    return tr_dict


# Updates balance after points are deducted
def updateBalance(new_points_balance):

    for payer in (user_data):
        user_data[payer] = new_points_balance[payer]
    print("UD from updateBal: ",user_data)
    return True

# Retrieves user points balance
@app.route('/points')
def getBalance():
    return user_data

class PointsManager(Resource):

    transactions = []
    # Retrieves user points balance
    def get(self):
        return user_data

    def post(self,payer,points,date):
        self.addPoints(payer, points, date)

        return self.transactions

    def addPoints(self, payer, points, date):
        date = self.parseDate(date)
        points = int(points)
        if payer not in user_data:
            if points < 0:
                abort(404, message='User does not exist')
            else:
                user_data[payer] = points
                self.transactions += [[payer, int(points), date]]
                tracker[payer] = 0
        else:
            if (points + user_data[payer]) >= 0:
                user_data[payer] += points
                self.transactions += [[payer, int(points), date]]
                if points < 0:
                    tracker[payer] += points
            else:
                abort(404, message="Insufficient points to deduct")
    # Deducts points specified
    @app.route('/deduct/<pts_deduct>')
    def deduct(pts_deduct):
        # Type casting points from str to int
        pts_deduct = int(pts_deduct)
        temp_user_points = getBalance()
        # Return in case given points to deduct is negative, and returning user points data
        if int(pts_deduct) <= 0:
            return {404,"Error: Please check the amount"}

        # Initializing the dictionary values to 0
        for payer in user_data:
            deduct_track[payer] = 0

        # Getting transactions from the Class object
        transactions = getTransactions()
        for t in range(len(transactions) - 1):
            if pts_deduct <= 0:
                updateBalance(deduct_track)

            else:

                # tr has current transaction
                tr = transactions[t]

                # Unpacking the [payee, points] values
                tr_payee, tr_points = tr[0], tr[1]

                # Proceed if points to deduct is greater than the transaction points
                if pts_deduct >= tr_points:

                    # If the transaction points are between zero and actual points balance
                    if tr_points >= 0 and tr_points <= temp_user_points[tr_payee]:
                        pts_deduct -= tr_points
                        deduct_track[tr_payee] -= tr_points
                        temp_user_points[tr_payee] -= tr_points

                    # If the points are negative and Actual points are less than or equal to zero
                    elif tr_points < 0 and temp_user_points[tr_payee] <= 0:
                        continue

                    # If the transactions are negative and Actual points are positive
                    elif tr_points < 0 and temp_user_points[tr_payee] > 0:
                        diff = deduct_track[tr_payee] - tr_points
                        deduct_track[tr_payee] = diff
                        pts_deduct += abs(tr_points)
                        temp_user_points[tr_payee] += abs(tr_points)

                    # If the transaction points are positive & greater than the Actual points,
                    # and the Actual points are not zero
                    elif tr_points > 0 and tr_points > temp_user_points[tr_payee] and temp_user_points[tr_payee] != 0:
                        pts_deduct -= temp_user_points[tr_payee]
                        deduct_track[tr_payee] -= temp_user_points[tr_payee]
                        temp_user_points[tr_payee] = 0

                    # If the transaction points are positive and Actual user points are zero
                    elif tr_points > 0 and temp_user_points[tr_payee] == 0:
                        continue
                # If the points to be deducted are less than transaction points
                elif pts_deduct < tr_points:

                    #If the points to be deducted are less than Actual points
                    if pts_deduct < temp_user_points[tr_payee]:
                        deduct_track[tr_payee] -= pts_deduct
                        temp_user_points[tr_payee] -= pts_deduct
                        pts_deduct = 0

                    # If the points to be deducted are greater than Actual user points
                    elif pts_deduct > temp_user_points[tr_payee]:
                        pts_deduct -= temp_user_points[tr_payee]
                        temp_user_points[tr_payee] = 0

        print("Points to deduct: ", pts_deduct)
        print("User data: ", user_data)
        # Update balance if points are positive, which means there are points left after deducting
        # from all the transactions
        if pts_deduct > 0:
            updateBalance(temp_user_points)
        return deduct_track

    # Transaction setter
    def setTransactions(self):
        tr_dict = {}
        for i in range(len(self.transactions)):
            tr_dict[i] = self.transactions[i]
        return tr_dict

    # Retrieves the deductions happened from transactions
    @app.route('/deductions')
    def deductions():
        return tracker

    # Date parser from the arguments
    def parseDate(self,date):
        pattern = "%"
        string = re.sub("%", ' ', date)
        #print(string)
        string = string[3:5] + '/' + string[6:8] + " " + string[10:12] + ":" + string[13:]
        return string

api.add_resource(PointsManager,"/<string:payer>/<string:points>/<string:date>","/","/deductions")

if __name__ == '__main__':
    app.run(debug = True)

