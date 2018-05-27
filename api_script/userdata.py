from peewee import *
import requests

# i don't have a real auth token 
auth_token = 'fake_auth_token'

# define the database object for peewee 
# the real db probably has credentials but I don't have those
db = MySQLDatabase('monument.db')

# setting up base model for ORM
class BaseModel(Model):
    class Meta:
        database = db


# define user model subclass of base model
class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    email = CharField(unique=True)
    # meta class contains details about the database in connection to the class
    class Meta:
        table_name = 'user'


# get all users from the database
users = User.select()
# iterate through user objects and make a dictionary with the info we need
# we could use model_to_dict but because the api requests needs user_id as the PK
# and the DB just calls that 'id' it's better to just iterate through like this
users_arr = [{
        'user_id': user.id,
        'email': user.email,
        'name': user.name
    } for user in users]

# define the url for post requests
url = 'https://api.intercom.io/users'
# define the authorization header
head = {'Authorization': f'Bearer {auth_token}'}

# loop through every user in our array and POST those to the API
# by default the next loop will be blocked as long as the request hasn't returned
# so no need to worry about async 
for user_dict in user_arr:
    try:
        requests.post(url, user_dict, headers=head)
    except requests.exceptions.RequestException as e:
        print(e)




