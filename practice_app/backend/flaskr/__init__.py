# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:21:17 2020

@author: BarisAlhan
"""

import os
from flask import Flask, render_template
from . import db
from . import routes_product
from . import routes_createproduct
from . import routes_search


def create_app(test_config = None):
    
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(routes_product.product_bp)
    app.register_blueprint(routes_createproduct.createproduct_bp)
    app.register_blueprint(routes_search.bp)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    
    app.config.from_mapping(
        SECRET_KEY='tursu',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    
    @app.route('/')
    def hello():
        
        products = db.query_db('select * from Product')
        product_list = []
        for product in products:
            

            price_try = product["price"]

            product_dict = {"id": product["id"],
                            "name": product["name"],
                            "price": {
                                "try": price_try
                            },
                            "seller": product["seller"],
                            "description": product["description"],
                            "location": product["location"],
                            "url": product["url"]
                            }
            product_list.append(product_dict)

        return render_template("home.html", products=product_list)
    
    
    db.init_app(app)
    
    return app
