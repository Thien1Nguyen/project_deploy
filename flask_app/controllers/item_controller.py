from flask import render_template, redirect, request, flash, session

from flask_app import app
from flask_app.models.manager_model import Manager
from flask_app.models.item_model import Item
from flask_app.models.category_model import Category

@app.route('/menu_add')
def menu_add():
    if 'manager_id' not in session:
        flash("Please Log In >:(")
        return redirect('/')
    
    categories_list = Category.get_all()
    
    return render_template('add_to_menu_page.html', categories_list = categories_list )

@app.route('/add_category', methods = ['POST'])
def add_category():
    if 'manager_id' not in session:
        flash("Please Log In >:(")
        return redirect('/manager_welcome')


    if not Category.validate_create(request.form):
        return redirect("/menu_add")
    
    Category.create(request.form)

    return redirect('/manager_dashboard')

@app.route('/add_item', methods = ['POST'])
def add_item():

    if 'manager_id' not in session:
        flash("Please Log In >:(")
        return redirect('/manager_welcome')


    if not Item.validate_create(request.form):
        return redirect("/menu_add")
    
    Item.create(request.form)

    return redirect('/manager_dashboard')

@app.route('/edit_page/<int:id>')
def edit_item(id):
    if 'manager_id' not in session:
        flash("Please Log In >:(")
        return redirect('/manager_welcome')
    
    item = Item.get_item_by_id(id)
    categories_list = Category.get_all()
    
    return render_template('edit.html', item=item, categories_list = categories_list)

@app.route('/updated_item', methods = ['POST'])
def update_item():
    if 'manager_id' not in session:
        flash("Please Log In >:(")
        return redirect('/manager_welcome')

    if not Item.validate_create(request.form):
        return redirect(f'/edit_page/{request.form["id"]}')

    Item.update(request.form)

    return redirect('/manager_dashboard')

@app.route('/delete/<int:id>')
def delete(id):
    Item.delete(id)
    return redirect('/manager_dashboard')

