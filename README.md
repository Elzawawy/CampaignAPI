# CampaignAPI 

Being online business requires special marketing skills. Creating campaigns, managing
campaigns and making sure that the money spent to get traffic from different advertising
platforms became more challenging and time consuming.
Being an online businesses you need to focus on the core functionality they do instead of
wasting time, money and effort managing your digital campaigns.

![](https://3.bp.blogspot.com/-TeW-jsT2v-8/W6578p-iJBI/AAAAAAAAAOw/SaQh5QkIPz4oDrJj9haWyyfP9Q8DOXEkwCLcBGAs/s1600/rest.png)

## About Task 
To create a RESTful campaign resource. Campaign data will be (Name, Country,....). If category is not provided you need to extract it from the *dummy* category extraction service. [Here](https://ngkc0vhbrl.execute-api.eu-west-1.amazonaws.com/api/?url=https://arabic.cnn.com/) 

Also, to visulaize the data based on some paramters passed on in the query and show it up in a UI generated.

## Using my RESTful API
To run the API server. 
execute the command "python api_server.py"

There is 5 Endpoints in the Server:

['Get'] http://127.0.0.1:5000/campaign/api/<string:name> 

['Post'] http://127.0.0.1:5000/campaign/api/<string:name> 

['Put'] http://127.0.0.1:5000/campaign/api/<string:name> 

['Delete'] http://127.0.0.1:5000/campaign/api/<string:name> 

The fifth is for visualizing part: ['Post'] http://127.0.0.1:5000/campaign/visualize/

### Notes:

1- This <string:name> is a paarmeter input for the name of the campagin. (The ID of the database)

2- For Post and Put you enter your params in the body of request using Postman or any other utility as a JSON object including the columns of data. 

E.g
{
"name": "n6",
"country": "USA",
"budget": 149,
"goal": "Success",
"category": "Sports"
}

3- For Visualizing Endpoint: 

E.g:
{
	"dimensions": "country",
	"fields": ["goal","name"]
}

where, Dimensions and Fields both can be an array of data colns and Dimensions are used to group data by these fields
while Fields is the array of fields to return in each campaign.
