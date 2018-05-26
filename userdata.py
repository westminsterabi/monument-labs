from peewee import *
from playhouse.shortcuts import model_to_dict
import requests

auth_token = 'fake_auth_token'

db = MySQLDatabase('monument.db')

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    email = CharField(unique=True)

    class Meta:
        table_name = 'user'


users = User.select()
users_arr = [{
        'user_id': user.id,
        'email': user.email,
        'name': user.name
    } for user in users]

url = 'https://api.intercom.io/users'
head = {'Authorization': f'Bearer {auth_token}'}

for user_dict in user_arr:
    try:
        requests.post(url, user_dict, headers=head)
    except requests.exceptions.RequestException as e:
        print(e)




