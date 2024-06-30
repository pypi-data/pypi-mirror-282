from .main import fetch_chat_id, fetch_chat_user_id, fetch_chat_username, fetch_message_info

class TelegramChat:
    @staticmethod
    def id(token, timeout=60):
        return fetch_chat_id(token, timeout)
    
    @staticmethod
    def user_id(token, timeout=60):
        return fetch_chat_user_id(token, timeout)
    
    @staticmethod
    def username(token, timeout=60):
        return fetch_chat_username(token, timeout)

    @staticmethod
    def message_info(token, timeout=60):
        return fetch_message_info(token, timeout)

telegram_chat = TelegramChat()
