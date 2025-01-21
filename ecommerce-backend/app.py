from flask import Flask
from flask_cors import CORS
from routes.products import products_bp
from routes.requirements import requirements_bp
from routes.updateProductQuantity import updateProductQuantity_bp
from routes.getProductList import getProductList_bp
from routes.predictConsumption import predictConsumption_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(products_bp)
app.register_blueprint(requirements_bp)
app.register_blueprint(updateProductQuantity_bp)
app.register_blueprint(getProductList_bp)
app.register_blueprint(predictConsumption_bp)

if __name__ == '__main__':
    app.run(debug=True)
