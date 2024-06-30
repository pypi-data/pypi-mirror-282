from .main import fetch_chat_id, fetch_chat_user_id, fetch_chat_username, fetch_message_info

class TelegramChat:
    @staticmethod
    def id(token):
        return fetch_chat_id(token)
    
    @staticmethod
    def user_id(token):
        return fetch_chat_user_id(token)
    
    @staticmethod
    def username(token):
        return fetch_chat_username(token)

    @staticmethod
    def message_info(token):
        return fetch_message_info(token)

telegram_chat = TelegramChat()
