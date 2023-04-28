from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE
from flask import flash

class Item:
    def __init__(self,data):
        self.id = data['id']
        self.category_id = data['category_id']
        self.name = data['name']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,form):

        query = """

                INSERT INTO items(category_id, name, price)
                VALUE(%(category_id)s, %(name)s, %(price)s)
        """

        return connectToMySQL(DATABASE).query_db(query,form)
    
    @classmethod
    def get_all(cls):

        query = """
                SELECT * FROM items;
        """

        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def get_item_by_id(cls,id):
        data = {
            'id':id
        }

        query = """
                SELECT * FROM items
                JOIN categories ON items.category_id = categories.id
                WHERE items.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)

        print(results)

        if results:
            item = cls(results[0])
            item.category_name = results[0]['categories.name']
            return item

    @classmethod
    def update(cls,form):
        
        query = """
                UPDATE items
                SET
                category_id = %(category_id)s,
                name = %(name)s,
                price = %(price)s
                
                WHERE id = %(id)s;
        """
        connectToMySQL(DATABASE).query_db(query,form)
    

    @classmethod
    def delete(cls, id):

        data = {
            'id': id
        }

        query = """
                DELETE FROM
                items
                WHERE id = %(id)s;
        """
        connectToMySQL(DATABASE).query_db(query, data)
    

    @classmethod
    def validate_create(cls, form):

        is_valid = True

        if 'category_id' not in form:
            flash('Please select a category for the dish!')
            is_valid = False

        if len(form['name']) < 1:
            flash('Please enter a name for the dish!')
            is_valid = False


        if len(form['price']) < 1:
            flash('Please give the dish a price!')
            is_valid = False

        return is_valid