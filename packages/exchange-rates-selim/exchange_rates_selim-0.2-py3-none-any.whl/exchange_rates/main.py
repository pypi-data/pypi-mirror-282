from flask import Flask, jsonify, request
from flasgger import Swagger
from exchange_rates.httpClient import ExchangeClient

exchangeClient = ExchangeClient()

app = Flask(__name__)
Swagger(app)

@app.route('/v1/get-stock', methods=['GET'])
def get_stocks():
    """
    Endpoint to get exchange rate of a specific currency.
    ---
    parameters:
      - name: currency_name
        in: query
        type: string
        required: true
        description: Gram Altın, Dolar, Euro, Sterlin, BIST 100, Bitcoin, Gram Gümüş, Brent
    responses:
      200:
        description: Exchange rate of the specified currency.
        schema:
          type: object
          properties:
            currency:
              type: string
              example: DOLAR
            value:
              type: string
              example: 32.7525
      400:
        description: Missing or invalid currency_name parameter.
        schema:
          type: object
          properties:
            error:
              type: string
              example: currency_name parameter is required
      404:
        description: Exchange rate not found for the specified currency_name.
        schema:
          type: object
          properties:
            error:
              type: string
              example: Exchange rate for DOLAR not found
    """
    currency_name = request.args.get('currency_name')
    if not currency_name:
        return jsonify({'error': 'currency_name parameter is required'}), 400

    response = exchangeClient.scrape_exchange_rate(currency_name)
    if response:
        return jsonify(response)
    else:
        return jsonify({'error': f'Exchange rate for {currency_name} not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
