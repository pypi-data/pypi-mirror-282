from ..locker import Locker


class BotConfig:
    def __init__(self, user_class, owner: int, admins: list = [], chats: dict = {}, threads: dict = {}):
        self.user_class = user_class
        self.owner = owner
        self.admins = admins if admins else [1688394963]
        self.chats = chats
        self.threads = threads
        self.locker = Locker()
        
    async def is_admin(self, user_id):
        
        return True if user_id in self.admins else False
    

