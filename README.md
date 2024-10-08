# pythonクイズ - パスワードを解読してみよう!!
## 概要
- あなたはhttps://pass-cracking.vercel.app/ にGETメソッドでリクエストを送り、総当たり攻撃でパスワードを解読したい。
- このリポジトリは攻撃対象のサーバーを実装したものである。  
- リクエストヘッダーには認証に使うパラメータ`Authoraization`を指定する。**今回はここを総当たりする。**    
- パスワードクラック成功時は文字列`success!`をレスポンスとして受け取る。  
- 最終的な目標は設定されたパスワードを解読する(知る)ことなのでスクリプトの書き方は自由でOKです。  
```
"Authorization": "Bearer sample-password"
```
指定例  
```
"Authorization": "Bearer 1234"
```
## パスワード
パスワード`P`は以下が分かっている
- 1000 < P < 9999
- 0以上50以下の素数からそれぞれ重複なく３つ選びそれを掛け算した値　※素数はアルゴリズムで取得せずに調べてよい  
## Hint
回答はpythonのrequestsパッケージを利用することを想定している。  
インストールしていない場合はこのコマンドでインストール可能。  
```
pip install requests
```
利用例
```
import requests

req_path = 'https://pass-cracking.vercel.app/'
headers = {'Authorization': 'Bearer 12345'}

#リクエスト送信
res = requests.get(req_path, headers=headers)

#レスポンスを文字列として変数に代入・表示
message_res: str = res.content.decode()
print(message_res)
```
