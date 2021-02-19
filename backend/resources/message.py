from flask import Response, request
from database.models import Message, get_messages
from flask_jwt_extended import jwt_required, get_jwt
from flask_restful import Resource
from .auth import get_user_by_jti, response_token_expired_logout, response_token_invalid, token_valid, token_update

class MessagesApi(Resource):
    @jwt_required()
    def get(self):
        jti = get_jwt()['jti']
        user = get_user_by_jti(jti)
        if user:
            if token_valid(user):
                token_update(user)
                messages = get_messages()
                return Response(messages, mimetype="application/json", status=200)
            else:
                return response_token_expired_logout(user)
        else:
            return response_token_invalid()

    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        body = request.get_json()
        user = get_user_by_jti(jti)
        if user:
            if token_valid(user):
                token_update(user)
                message = Message(user.name, body["message"])
                id = message.save()
                return {'id': id, 'sender': message.sender, 'message': message.message}
            else:
                return response_token_expired_logout(user)
        else:
            return response_token_invalid()