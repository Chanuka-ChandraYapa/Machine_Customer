from flask import Flask
from flask_cors import CORS
from routes.products import products_bp
from routes.requirements import requirements_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(products_bp)
app.register_blueprint(requirements_bp)

if __name__ == '__main__':
    app.run(debug=True)
