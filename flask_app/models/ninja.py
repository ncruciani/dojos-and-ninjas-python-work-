from flask_app.config.mysqlconnection import connectToMySQL
db = 'dojos_and_ninjas'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.iddojos = data['dojo_iddojos']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']
        


    @classmethod
    def ninjadata(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(db).query_db(query)
        ninja = []
        for data in results:
            ninja.append(cls(data))
        print(results)
        return ninja


    @classmethod
    def save(cls , data):
        query = 'INSERT INTO ninjas ( dojo_iddojos ,  first_name , Last_name , age ) VALUES ( %(dojo_iddojos)s ,%(first_name)s , %(last_name)s , %(age)s );'
        return connectToMySQL(db) .query_db(query , data)
    


    @classmethod
    def getninjasanddojos(cls , banana):
        data = {
            'id' : banana
        }
        query = 'SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_iddojos WHERE dojos.id = %(id)s;'
        results = connectToMySQL(db) .query_db(query , data)
        # ninjadojo = []
        # for data in results:
        #     ninjadojo.append(cls(data))
        # print(results)
        print(results)
        return results


#class NinjaDojo:
    #def __init__(self,data):
        #self.id = data['idninjas']
        #self.first_name = data['first_name']
        #self.last_name = data['last_name']
        #self.age = data['age']
        #self.id = data['iddojos']
        #self.name = data['name']
        #pass




    # @classmethod
    # def joinedninjadojo(cls , data):
    #     query = 'INSERT INTO ninjas (dojo_iddojos , first_name , last_name , age , name) VALLUES( %(first_name)s , %(last_name)s , %(age)s , %(name)s);'
    #     return connectToMySQL(db) .query_db(query , data)