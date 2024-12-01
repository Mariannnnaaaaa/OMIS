from model.User import User
from model.SystemComposition import SystemComposition
from ProfileCreationManager import ProfileCreationManager

class UserProfileCreationManager(ProfileCreationManager):
    def __init__(self, user: User):
        self.__user = user

    def create_profile(self):
        pass

    def save_profile(self, composition: SystemComposition):
        pass