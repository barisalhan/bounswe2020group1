from flask import Blueprint, abort, jsonify, request, render_template


from .db import get_db
from .find_similar_words_API import get_words_with_similar_meaning

#TODO Change template folder after decision
bp = Blueprint('Product API Search', __name__, url_prefix='/', template_folder="../frontend")



def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@bp.route('/search/', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if(keyword is not None and keyword !=""):
        keyword.replace("+"," ")
        semantically_close = get_words_with_similar_meaning(keyword)
        search_words = [keyword] + semantically_close
        all_products = query_db('select * from product')
        product_list = []
        for product in all_products:
        	for word in search_words:
        		if(word in product["name"] or word in product["description"]):
        			product_dict = {"id": product["id"],
        							"name": product["name"],
        							"price": product["price"],
        							"description": product["description"],
        							"location": product["location"]
        							}
        			product_list.append(product_dict)
        			break
    else:
        product_list = []
    return render_template("home.html", products=product_list)



