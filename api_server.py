from flask import Flask,render_template
from flask_restful import Api, Resource, reqparse
import requests
import pandas as pd
#Defining App !
app = Flask(__name__)
api = Api(app)
# My Datastore
campaigns = pd.read_csv("./data_store.csv").to_dict('records')
# Saving data to CSV format file each update.
def save_data():
    pd.DataFrame(campaigns).to_csv("./data_store.csv",index=False)
# Endpoint for Visulaizing the Data.
def visualize():
    parser = reqparse.RequestParser()
    parser.add_argument("dimensions", action='append')
    parser.add_argument("fields", action='append')
    args = parser.parse_args()
    fields = args["fields"]
    df = pd.DataFrame(campaigns).groupby(args["dimensions"])[fields].count()
    pie = df.plot.bar()
    fig = pie.get_figure()
    fig.savefig("myplot.png")
    return render_template('response.html'),200

# Main Four Endpoints to API supported: {GET,POST,PUT,DELETE}
class Campaign(Resource):
    # Endpoint to Get a Campaign already created in my datastore.
    def get(self, name):
        for campaign in campaigns:
            if(name == campaign["name"]):
                return campaign, 200
        return "Campaign not found", 404
    # Endpoint to create a Campaign in the datastore.
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("country")
        parser.add_argument("budget")
        parser.add_argument("goal")
        parser.add_argument("category")
        args = parser.parse_args()

        for campaign in campaigns:
            if(name == campaign["name"]):
                return "Campaign with name {} already exists".format(name), 400

        new_campaign = {
            "name": name,
            "country": args["country"],
            "budget": args["budget"],
            "goal": args["goal"],
            "category": args["category"]
        }

        if(args["category"] == None):
            req_url = "https://ngkc0vhbrl.execute-api.eu-west-1.amazonaws.com/api/?url=https://arabic.cnn.com/"
            response = requests.get(req_url)
            new_campaign["category"] = response.json()["category"]["name"]

        campaigns.append(new_campaign)
        save_data()
        return new_campaign, 201
    # Endpoint to create or update a Campaign in the datastore.
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("country")
        parser.add_argument("budget")
        parser.add_argument("goal")
        parser.add_argument("category")
        args = parser.parse_args()

        for campaign in campaigns:
            if(name == campaign["name"]):
                campaign["country"] = args["country"]
                campaign["budget"] = args["budget"]
                campaign["goal"] = args["goal"]
                campaign["category"] = args["category"]
                return campaign, 200

        new_campaign = {
            "name": name,
            "country": args["country"],
            "budget": args["budget"],
            "goal": args["goal"],
            "category": args["category"]
        }

        if(args["category"] == None):
            req_url = "https://ngkc0vhbrl.execute-api.eu-west-1.amazonaws.com/api/?url=https://arabic.cnn.com/"
            response = requests.get(req_url)
            new_campaign["category"] = response.json()["category"]["name"]

        campaigns.append(new_campaign)
        save_data()
        return new_campaign, 201
    # Endpoint to delete a Campaign in the datastore.
    def delete(self, name):
        global campaigns
        campaigns = [campaign for campaign in campaigns if campaign["name"] != name]
        save_data()
        return "{} is deleted.".format(name), 200
# Adding routes to the Application and Endpoints to App.
api.add_resource(Campaign, "/campaign/api/<string:name>")
app.add_url_rule('/campaign/visualize', 'visulaize',visualize, methods = ["POST"])
# Run this baby server !
app.run(debug=True)
