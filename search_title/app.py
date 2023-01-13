from flask import render_template, Blueprint, request
from function import search_title

search_title_blueprint = Blueprint("search_title_blueprint", __name__, template_folder='templates')


@search_title_blueprint("/movie/<str:title>")
def search(title):

    return search_title(title)
