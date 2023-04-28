from flask import render_template, redirect, request, flash, session

from flask_app import app
from flask_app.models.manager_model import Manager
from flask_app.models.category_model import Category
from flask_app.models.item_model import Item


@app.route('/')
def main():
    catergories_list = Category.get_all()
    items_list = Item.get_all()
    
    return render_template('index.html', catergories_list = catergories_list, items_list = items_list)