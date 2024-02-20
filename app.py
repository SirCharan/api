from flask import Flask, jsonify
from delta_rest_client import DeltaRestClient
from dotenv import loadenv
import os

loadenv()

# Initialize DeltaRestClient
delta_client = DeltaRestClient(
    base_url='https://api.delta.exchange',
    api_key='Tzc7TA1wh3U4UFWdlqdnVJ1A05WJir',
    api_secret='IVZ4SEJtDymNz8EodtcAeou1tDMZ6fWyv4hJ9ZxDI3Y6ESZEkBh7LskJn3jT'
)

app = Flask(__name__)

# Define a route to fetch balances
@app.route('/balances', methods=['GET'])
def get_balances():
    try:
        balances = delta_client.get_balances(5)
        return jsonify({'available_balance': balances['available_balance']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000), host='0.0.0.0')
