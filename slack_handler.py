import requests
import json
import os



class Slack_Bot:

    def __init__(self):
        self.slack_token = os.getenv('SLACK_AUTH_KEY')
        self.slack_channel = '#rundeck'
        self.slack_icon_emoji = ':see_no_evil:'
        self.slack_user_name = 'Python Slack Handler'


    def post_message_to_slack(self, text, blocks = None):
        return requests.post('https://slack.com/api/chat.postMessage', {
            'token': self.slack_token,
            'channel': self.slack_channel,
            'text': text,
            'icon_emoji': self.slack_icon_emoji,
            'username': self.slack_user_name,
            'blocks': json.dumps(blocks) if blocks else None
        }).json()

