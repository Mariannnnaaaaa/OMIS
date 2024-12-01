from StandardAuthorizationHandler import StandardAuthorizationHandler
from model.User import User

class AuthorizationHandler(StandardAuthorizationHandler):
    def check_full_name(self, full_name: str, user: User) -> bool:
        pass

    def handle_password(self, password: str, user: User) -> bool:
        pass