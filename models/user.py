import sqlite3

'reason i put user class in here and not in resource folder is bcoz this user class is not actually inheriting Resource' \
'and neither api responds to this class,' \
'since api does not deal with it ,it is not a resoource'

"""This class is simply a helper class, that we use to retieve data more easily]

A model is an INTERNAL REPRESENTATION OF AN ENTITY
whereas 
REsource is an EXTERNAL REPRESENTATION OF AN ENTITY"""
class UserModel:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    @classmethod
    def findByUsername(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="select * from users where username=?"
        resultset=cursor.execute(query,(username,))
        #reason we passed username in '()' with a comma (,) is to tell
        # python that we actually want our result to be a tuple

        #NOW TO FECTH ONLY ONE ROW FROM RESULSET
        row=resultset.fetchone()

        if row: #only works if row got some data
            # user=cls(row[0],row[1],row[2])
            user=cls(*row)
        else:
            user=None
        return user

    @classmethod
    def findByUseId(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from users where id=?"
        resultset = cursor.execute(query, (_id,))
        # reason we passed username in '()' with a comma (,) is to tell
        # python that we actually want our result to be a tuple
        # NOW TO FECTH ONLY ONE ROW FROM RESULSET
        row = resultset.fetchone()
        if row:  # only works if row got some data
            # user=cls(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None


    'now make appropriate changes to security class with appropriate methods'


