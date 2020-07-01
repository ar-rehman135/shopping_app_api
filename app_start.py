from flask import Flask, session
from datetime import timedelta
from src.api import home_api, shopkeepers_api, bankacount_api , brands_api,products_api, customers_api,orders_api,product_in_order_api, customer_add_shops_api
from src.database.db import init_db
app = Flask(__name__, instance_relative_config=True,static_folder="static/dist",template_folder="static")
app.config.from_mapping(
    SECRET_KEY = 'DEV')

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)


app.register_blueprint(shopkeepers_api.shopkeeper_bp)
app.register_blueprint(bankacount_api.bankacount_bp)
app.register_blueprint(products_api.product_bp)
app.register_blueprint(brands_api.brands_bp)
app.register_blueprint(home_api.home_bp)
app.register_blueprint(customers_api.customers_bp)
app.register_blueprint(orders_api.orders_bp)
app.register_blueprint(product_in_order_api.products_in_orders_bp)
app.register_blueprint(customer_add_shops_api.customer_add_shops_bp)
if __name__ == "__main__":
    init_db()
    app.run(debug = True,host="192.168.0.109")


