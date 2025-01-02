from flask import Flask, request, jsonify
from components.feature_extraction import preprocess_products
from components.clustering import cluster
from components.ranking import rank
from components.requirements import update_requirements
from flask_cors import CORS as cors
from components.processProduct import ProcessProduct 

app = Flask(__name__)
cors(app)


@app.route('/process-products', methods=['POST'])
def process_products():
    data = request.json
    products = data.get('products', [])
    processed_products = []
    for product in products:
        processed_products.append(preprocess_products(product))

    clustered_products = cluster(processed_products)

    ranked_products = rank(clustered_products)

    return jsonify({"status": "success", "processed_data": ranked_products})


@app.route('/requirements', methods=['POST'])
def requirements():
    data = request.json
    requirements = data.get('requirements')
    update_requirements(requirements)
    print(requirements)

    return jsonify({"status": "success", "processed_data": ""})

@app.route('/updateProductQuantity', methods=['POST'])
def updateProductQuantity():
    data = request.json
    print('Updated product:', data)
    product = data.get('productName')
    remainingQuantity = data.get('remainingQuantity')
    
    # Get the best product to buy based on the current product and quantity
    best_product = ProcessProduct(product, remainingQuantity)
    
    if best_product:
        return jsonify({"status": "success", "best_product": best_product})
    else:
        return jsonify({"status": "no_update", "message": "No update needed"})


if __name__ == '__main__':
    app.run(debug=True)
