import requests
import os
import json

class TelegramBot:
    def __init__(self, bot_token, group_chat_id):
        self.bot_token = bot_token
        self.group_chat_id = group_chat_id
        self.api_url = f'https://api.telegram.org/bot{bot_token}/'
        self.cookies_file = os.path.join(os.path.dirname(__file__), 'terminalbot_cookies.json')
        self.last_update_id = self.load_last_update_id()

    def get_updates(self):
        params = {'timeout': 100, 'offset': self.last_update_id + 1 if self.last_update_id else None}
        response = requests.get(self.api_url + 'getUpdates', params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_message(self):
        updates = self.get_updates()
        if updates and 'result' in updates:
            for update in updates['result']:
                update_id = update['update_id']
                if self.last_update_id is None or update_id > self.last_update_id:
                    self.last_update_id = update_id
                    self.save_last_update_id()
                    if 'message' in update and 'text' in update['message']:
                        return update['message']['text']
        return None

    def send_message(self, text):
        params = {'chat_id': self.group_chat_id, 'text': text}
        requests.post(self.api_url + 'sendMessage', params=params)

    def load_last_update_id(self):
        if os.path.exists(self.cookies_file):
            try:
                with open(self.cookies_file, 'r') as f:
                    data = json.load(f)
                    if data.get('group_chat_id') != self.group_chat_id:
                        self.save_last_update_id(reset=True)
                        return None
                    return data.get('last_update_id')
            except (json.JSONDecodeError, KeyError):
                self.save_last_update_id(reset=True)
                return None
        return None

    def save_last_update_id(self, reset=False):
        data = {
            'group_chat_id': self.group_chat_id,
            'last_update_id': None if reset else self.last_update_id
        }
        with open(self.cookies_file, 'w') as f:
            json.dump(data, f)

def get_message(bot_token, group_chat_id):
    bot = TelegramBot(bot_token, group_chat_id)
    return bot.get_message()

def send_message(bot_token, group_chat_id, message):
    bot = TelegramBot(bot_token, group_chat_id)
    bot.send_message(message)
