from flask import Flask, jsonify
from delta_rest_client import DeltaRestClient
import os

# Initialize DeltaRestClient
delta_client = DeltaRestClient(
    base_url='https://api.delta.exchange',
    api_key='umRJZmxH6JzMqzKNLKoV68aVeJh8eT',
    api_secret='5XJpQyRkFeo2V5eNsaAGtijIKUYCvvMkVWXYye5hZffOzVSu8tF7HMUAUX54'
)

app = Flask(__name__)

# Define a route to fetch balances
@app.route('/balances', methods=['GET'])
def get_balances():
    try:
        print("Processing Request")
        balances = delta_client.get_balances(5)
        print("Got balances :", balances)
        return jsonify({'available_balance': balances['available_balance']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route("/")
def hello():
    return "hello world", 200

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000), host='0.0.0.0')
