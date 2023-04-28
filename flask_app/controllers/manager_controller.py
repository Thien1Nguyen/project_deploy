from flask import render_template, redirect, request, flash, session

from flask_app import app
from flask_app.models.manager_model import Manager
from flask_app.models.category_model import Category
from flask_app.models.item_model import Item

@app.route('/manager_welcome')
def manager_welcome_page():
    return render_template('manager_login.html')

@app.route('/register', methods = ["POST"])
def register():
    if not Manager.validate_registration(request.form):
        # if it doesnt match then boot user back to register route to retry
        return redirect('/manager_welcome')
    
    Manager.create(request.form)

    return redirect('/manager_welcome')

@app.route('/login', methods = ["POST"])
def login():
    # checking if the login info match what we got in the Database
    print(request.form['email'])

    found_manager = Manager.validate_login(request.form)

    # if match then send the user id into session so they can have access into the logged in page
    if found_manager:
        session['manager_id'] = found_manager.id
        return redirect('/manager_dashboard')
    # if it does not match then we redirect them back into the home page to try again
    else:
        return redirect('/manager_welcome')
    
@app.route('/manager_dashboard')
def manager_dashboard():
    if 'manager_id' not in session:
        flash("Please Log In >:(")
        return redirect('/manager_welcome')
    
    catergories_list = Category.get_all()
    items_list = Item.get_all()
    
    if catergories_list:
        return render_template('manager_dashboard.html', catergories_list = catergories_list, items_list = items_list)
    elif not catergories_list:
        return render_template('manager_dashboard.html')
