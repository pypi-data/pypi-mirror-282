import requests
import time
import argparse

API_URL_TEMPLATE = 'https://api.telegram.org/bot{token}/getUpdates'

def get_updates(token, offset=None):
    url = API_URL_TEMPLATE.format(token=token)
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def fetch_chat_id(token):
    last_update_id = None

    while True:
        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    print(f"Chat ID: {chat_id}")
                    return chat_id  # Exit the function once the chat ID is found

        time.sleep(1)  # Avoid hitting the API too frequently

def fetch_chat_user_id(token):
    last_update_id = None

    while True:
        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update:
                    user_id = update['message']['from']['id']
                    print(f"User ID: {user_id}")
                    return user_id  # Exit the function once the user ID is found

        time.sleep(1)  # Avoid hitting the API too frequently

def fetch_chat_username(token):
    last_update_id = None

    while True:
        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update and 'from' in update['message']:
                    username = update['message']['from'].get('username')
                    if username:
                        print(f"Username: {username}")
                        return username  # Exit the function once the username is found

        time.sleep(1)  # Avoid hitting the API too frequently

def fetch_message_info(token):
    last_update_id = None

    while True:
        updates = get_updates(token, last_update_id)

        if 'result' in updates and len(updates['result']) > 0:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1

                if 'message' in update:
                    message = update['message']
                    user_id = message['from']['id']
                    username = message['from'].get('username', 'N/A')
                    chat_id = message['chat']['id']
                    group_username = message['chat'].get('username', 'N/A')

                    message_info = {
                        'group_id': chat_id,
                        'group_username': group_username,
                        'user_id': user_id,
                        'username': username
                    }

                    print(f"Group ID: {chat_id}")
                    print(f"Group Username: {group_username}")
                    print(f"User ID: {user_id}")
                    print(f"Username: {username}")
                    return message_info  # Exit the function once the message info is found

        time.sleep(1)  # Avoid hitting the API too frequently

def main():
    parser = argparse.ArgumentParser(description="Fetch Telegram group chat ID, user ID, username, and message info")
    parser.add_argument('--token', type=str, required=True, help='Telegram bot token')
    parser.add_argument('--info', type=str, choices=['chat_id', 'user_id', 'username', 'message_info'], required=True, help='Type of information to fetch')
    args = parser.parse_args()

    if args.info == 'chat_id':
        fetch_chat_id(args.token)
    elif args.info == 'user_id':
        fetch_chat_user_id(args.token)
    elif args.info == 'username':
        fetch_chat_username(args.token)
    elif args.info == 'message_info':
        fetch_message_info(args.token)

if __name__ == '__main__':
    main()
