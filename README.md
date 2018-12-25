# arxiv.org関連ツイートの抽出

1. arxiv.org関連ツイートを検索
2. 検索結果をSlack Webhook APIでチャンネルに送信
3. 取得した最新ツイートのIDをparams.jsonに保存

## Start

* Libraly Install

```
$ pip install --r requirements.txt
```

* Slack Post

```
$ python slack_post.py
```
