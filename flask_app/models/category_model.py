from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE
from flask import flash

class Category:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,form):

        query = """

                INSERT INTO categories(name)
                VALUE(%(name)s);
        """

        return connectToMySQL(DATABASE).query_db(query,form)
    
    @classmethod
    def get_all(cls):
        
        query = """

            SELECT * FROM categories;
        """

        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def validate_create(cls, form):

        is_valid = True

        if len(form['name']) < 1:
            flash('Please enter a name for the category!')
            is_valid = False
        
        return is_valid