from flask import request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
    get_jti
)
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
import datetime
import json

expires = datetime.timedelta(minutes=30)

class User(object):
    def __init__(self, jti, name: str, expires: datetime):
        self.jti = jti
        self.name = name
        self.expires = expires

class UserEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'jti': o.jti, 'name': o.name}
        return super(UserEncoder, self).default(o)

users = []

def get_user_by_jti(jti) -> User:
    for u in users:
        if u.jti == jti:
            return u
    return None


def get_user_by_name(name: str) -> User:
    for u in users:
        if u.name == name:
            return u
    return None


def token_valid(user: User) -> bool:
    if user and (datetime.datetime.now() < user.expires):
        return True
    return False


def token_update(user: User):
    user.expires = datetime.datetime.now() + expires

def response_token_expired_logout(user: User):
    # Log user out, because token too old
    users.remove(user)
    return {'message': 'Token expired.'}, 401


def response_token_invalid():
    return {'message': 'Token not valid.'}, 401


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        name = body.get('name')
        if get_user_by_name(name):
            return {'error': 'User already logged in.'}, 401

        access_token = create_access_token(identity=name, expires_delta=expires)
        user = User(get_jti(access_token), name, datetime.datetime.now() + expires)
        users.append(user)
        return {'token': access_token}


class LogoutAPI(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        user = get_user_by_jti(jti)
        print(json.dumps(user, cls=UserEncoder))
        if user:
            users.remove(user)
            return {'message': 'You have been logged out.'}
        else:
            return response_token_invalid()


class UserApi(Resource):
    @jwt_required()
    def get(self):
        jti = get_jwt()['jti']
        user = get_user_by_jti(jti)
        if user:
            if token_valid(user):
                token_update(user)
                return {'user': user.name}
            else:
                return response_token_expired_logout(user)
        else:
            return response_token_invalid()

