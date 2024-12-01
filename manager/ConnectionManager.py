from model.User import User

class ConnectionManager:
    def __init__(self, sender: User, receiver: User):
        self.sender = sender
        self.receiver = receiver

    def send_message(self, message):
        pass

    def receive_message(self, message: str) :
        pass
