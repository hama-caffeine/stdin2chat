'''
	input
		STDIN
	output
		Google Chat

	sample
		$ ls | python3 stdin2chat.py
'''
import sys
import textwrap
import requests
import json

# google chat Webhook
Webhook  = 'https://chat.googleapis.com/v1/spaces/xxxxxxxxxxxx/messages?key=xxxxxxxxxxxxxxxxxxxxxxxxxxx'

ChatText = textwrap.dedent('''
	```
	{StdinText}
	```
''').format(
	StdinText = sys.stdin.read().strip(), 
	).strip()

# Send Webhook
response = requests.post(
    Webhook,
    json={"text": ChatText}
)
