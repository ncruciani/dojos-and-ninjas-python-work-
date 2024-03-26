from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja 

db = 'dojos_and_ninjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at']
        self.ninja_list = []

    @classmethod
    def dojodata(cls):
        query = 'SELECT * FROM dojos ;'
        results = connectToMySQL(db).query_db(query)
        dojo = []
        for data in results:
            dojo.append(cls(data))
        return dojo


    @classmethod
    def save(cls , data):
        query = 'INSERT INTO dojos (name ) VALUES ( %(name)s);'
        return connectToMySQL(db) .query_db(query , data)
    

    @classmethod
    def getninjasanddojos(cls , dojo_id):
        print('dojo_id' , dojo_id)
        data = {
            'id' : dojo_id
        }
        query = 'SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_iddojos WHERE dojos.id = %(id)s;'
        results = connectToMySQL(db) .query_db(query , data)
        print('results' , results)
        #ninjadojo = []
        one_dojo = cls(results[0])
        for row in results:
            ninja_dict = {
                'id': row ['ninjas.id'] , 
                'first_name' : row['first_name'] ,
                'last_name' : row['last_name'] ,
                'age' : row['age'] ,
                'created_at' : row ['ninjas.created_at'] , 
                'updated_at' : row ['ninjas.updated_at'] ,
                'dojo_iddojos' : row['dojo_iddojos']
            }
            one_dojo.ninja_list.append(ninja.Ninja(ninja_dict))
        print('one_dojo', one_dojo)
        return one_dojo



# @classmethod
# def getninjasanddojos(cls, dojo_id):
#     print('dojo_id', dojo_id)
#     data = {
#         'id': dojo_id
#     }
#     query = 'SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_iddojos WHERE dojos.id = %(id)s;'
#     results = connectToMySQL(db).query_db(query, data)
#     print('results', results)

#     if results:  # Check if results is not empty
#         one_dojo = cls(results[0])
#         for row in results:
#             ninja_dict = {
#                 'id': row['ninjas.id'],
#                 'first_name': row['first_name'],
#                 'last_name': row['last_name'],
#                 'age': row['age'],
#                 'created_at': row['ninjas.created_at'],
#                 'updated_at': row['ninjas.updated_at'],
#                 'dojo_iddojos': row['dojo_iddojos']
#             }
#             one_dojo.ninja_list.append(ninja.Ninja(ninja_dict))
#         print('one_dojo', one_dojo)
#         return one_dojo
#     else:
#         return None  # Return an appropriate value if results is empty





















#@classmethod
#def ninjadojodata(cls):
    #query = 'SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojos_id'
    #results = connectToMySQL
    #ninjadojo[]
    #for data in results:
        #ninjadojo.append(cls(data))
    #return ninjadojo