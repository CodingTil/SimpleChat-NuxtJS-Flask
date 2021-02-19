from .auth import LoginApi, LogoutAPI, UserApi
from .message import MessagesApi

def initialize_routes(api):
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(LogoutAPI, '/api/logout')
    api.add_resource(UserApi, '/api/user')
    api.add_resource(MessagesApi, '/api/message')