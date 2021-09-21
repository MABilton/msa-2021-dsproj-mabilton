from flask import Flask, render_template, request as flask_req, make_response
from http.client import responses as http_responses
import requests
import json

app = Flask(__name__)

# Azure endpoint of API:
API_ENDPOINT = 'http://d7cd4e84-d0f9-4d93-8de7-aba2c62ef9bb.australiaeast.azurecontainer.io/score'

# Number of decimal places to print output of BERT model to user:
OUTPUT_DP = 4
FORMAT_STR = f".{OUTPUT_DP}f" 

@app.route('/', methods=['POST', 'GET'])
def home():
    if flask_req.method=="POST":
        return post_req(flask_req)
    elif flask_req.method=="GET":
        return render_template("main.html")

# Function which deals with post requests made to web app:
def post_req(request):
    # If user has sent POST request from home page:
    if hasattr(request, 'form'):
        text_input = request.form['text_from_page']
        response = call_bert_api(text_input)
        if response.status_code==200:
            msg="The Readability Score of your Text is:"
            pred = response.json()[0]
            output = f'{pred:{FORMAT_STR}}'
        else:
            msg = "Sorry - An Error has Occurred:"
            output = f"Error Code {response.status_code} : {http_responses[response.status_code]}"
        return render_template("main.html", text_input=text_input, msg=msg, output=output)
    # If user has sent POST request directly to API - note that errors handled by Azure API:
    else:
        req_json = json.loads(request)
        text_input = request['text']
        response = call_bert_api(text_input)
        return response

# Function to send POST request to Azure BERT api:
def call_bert_api(text):
    # Create input text data to POST to API:
    headers = {"Content-Type": "application/json"}
    data = {"text": [text]}
    data = json.dumps(data)
    # Send POST request to API:
    response = requests.post(API_ENDPOINT, data=data, headers=headers)
    return response

if __name__ == '__main__':
    app.run()