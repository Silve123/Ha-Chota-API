from flask import Flask, jsonify
from flask_cors import CORS
from DBMS import *

app = Flask(__name__)

CORS(app)


@app.route('/categories-and-items', methods=['GET'])
def categories_and_items():
    data = get_categories_and_items()

    if data is not None:
        return jsonify({'Categories': data})
    else:
        return jsonify({'error': 'Failed to retrieve data from the database'}), 500


@app.route('/specials', methods=['GET'])
def specials():
    data = get_specials()

    if data is not None:
        return jsonify({'Specials': data})
    else:
        return jsonify({'error': 'Failed to retrieve data from the database'}), 500


@app.route('/best-sellers', methods=['GET'])
def best_sellers():
    data = get_best_sellers()

    if data is not None:
        return jsonify({'Best-Sellers': data})
    else:
        return jsonify({'error': 'Failed to retrieve data from the database'}), 500


@app.route('/new-arrivals', methods=['GET'])
def new_arrivals():
    data = get_new_arrivals()

    if data is not None:
        return jsonify({'NewArrivals': data})
    else:
        return jsonify({'error': 'Failed to retrieve data from the database'}), 500



if __name__ == '__main__':
    app.run(debug=True)
