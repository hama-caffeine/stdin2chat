# stdin2chat

## やってること
標準入力で入ってきたテキストを  
Google Chatに飛ばすってだけ。

## 用途
時間がかかるコマンドが終わったときに  
手元に通知が来るのが欲しかったんで、  
そんな感じでの用途を考えてます。

なので、
```bash
$ ls | python3 stdin2chat.py
```
って感じで、出力された内容をそのまま渡せば、  
あらかじめ設定したチャットに  
メッセージとして飛んできます。

既存のテキストファイルでも
```bash
$ cat exsample.txt | python3 stdin2chat.py
```
って感じで飛ばすことができます。

## 用意するもの
Google chatのWebhook

## 設定
webhookの値をご自身の環境のものに書き換えれば  
使えるんじゃないかと

## コード
```python
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
```
## これから
とりあえず動いてる状態での公開。  
手元ではオプションで送信先をSlackや  
別のサービスとかに飛ばせるようにしてるのがあるので、  
きれいに書き直す時間ができたらそちらも公開しようかと。
