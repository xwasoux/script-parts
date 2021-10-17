# twint
Twitterからツイートをスクレイピングしてくれるtwintというツールの使い方とそのファイルからツイートのみを抽出する方法についてまとめました．

## 1.install 
下のコマンドでインストールする
```
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

## 2.データをスクレイピングする
### CSVファイルの場合
```
# test.csvに出力
$ twint -u username(@は除く) -o test.csv --csv
```
### jsonファイルの場合
```
# test.jsonに出力
$ twint -u username(@は除く) -o test.json --json
```

## 3.落としてきた CSV データからツイート部のみを抽出する
以下のコマンドを実行することでcsvファイルからツイート部分のみを抽出しテキストデータに出力できる
```
$ python3 extraction.py xxxxx.csv zzzzzz(.txtは不要)
```
## 参考資料
[Twintを使ってTweet情報を収集する（Python3）](https://ossyaritoori.hatenablog.com/entry/2020/08/04/Twint%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6Tweet%E6%83%85%E5%A0%B1%E3%82%92%E5%8F%8E%E9%9B%86%E3%81%99%E3%82%8B%EF%BC%88Python3%EF%BC%89)