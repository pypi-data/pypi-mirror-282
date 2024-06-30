import requests
import time

API_URL_TEMPLATE = 'https://api.telegram.org/bot{token}/getUpdates'

def get_updates(token, offset=None):
    url = API_URL_TEMPLATE.format(token=token)
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def fetch_chat_id(token, timeout=60):
    last_update_id = None
    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            return None

        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update:
                    return update['message']['chat']['id']

        time.sleep(1)

def fetch_chat_user_id(token, timeout=60):
    last_update_id = None
    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            return None

        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update:
                    return update['message']['from']['id']

        time.sleep(1)

def fetch_chat_username(token, timeout=60):
    last_update_id = None
    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            return None

        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update and 'from' in update['message']:
                    username = update['message']['from'].get('username')
                    if username:
                        return username

        time.sleep(1)

def fetch_message_info(token, timeout=60):
    last_update_id = None
    start_time = time.time()

    group_username = None

    while True:
        if time.time() - start_time > timeout:
            return None

        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update:
                    message = update['message']
                    user_id = message['from']['id']
                    username = message['from'].get('username', 'N/A')
                    chat_id = message['chat']['id']
                    group_username = message['chat'].get('username', group_username)

                    message_info = {
                        'group_id': chat_id,
                        'group_username': group_username,
                        'user_id': user_id,
                        'username': username
                    }

                    return message_info

        time.sleep(1)
