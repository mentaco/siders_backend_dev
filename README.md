# siders_backend_test
API開発のための開発環境の土台として使ってください。\
APIの開発はDockerのデータベースと接続して行う感じでお願いします。\
ある程度開発が進んだら、本番環境にデプロイしていこうと思います。

## ディレクトリ構成
```
siders_backend_test
├── data
├── docker-compose.yaml
├── init
│   └── init.sql
└── server
    ├── siders-server
    ├── requirements.txt
    ├── app.py
    └── api
        ├── __init__.py
        ├── database.py
        ├── db_info.py
        ├── router.py
        └── modules
            ├── __init__.py
            ├── example_modules.py
            └── execute_query.py
```
作成したプログラムは`server/api/modules`に配置してください。\
`execute_query.py`には`exec_query`関数があります。これはSQL文を引数にとり、データーベースへ送信し、結果を返します。必要であればインポートして使用してください。また、引数の詳細はファイルに記入してあります。\
`example_modules.py`にはプログラムの例が記述してあるので参考にしてください。

## 準備
### データベースの立ち上げ
まず、DockerのPostgreSQLをバックグラウンドで立ち上げます。
```
docker-compose up -d
```
データベースに直接入りたい場合は以下のコマンドを実行します。
```
psql -h localhost -d postgres -U postgres
Password for postgres: postgres
```
#### データベースの終了
データベースを終了するには以下のコマンドを実行します。
```
docker-compose down -v
```
`-v`オプションはディレクトリとのマウントを解除するためのオプションであり、無くても終了できます。ただし、データベースを初期化する際には必要です。
#### データベースの初期化
データベースを初期化するには、データベースを修了した後に以下のコマンドで`data/`内をすべて削除してください。
```
rm -rf data/*
```
### 仮想環境
#### 仮想環境の作成
仮想環境を作成するためのパッケージをインストールします。
```
pip3 install virtualenv
```
次に、Pythonの仮想環境を作成します。\
```
cd server
python3 -m virtualenv siders-server
```
#### 仮想環境の起動
次のコマンドで仮想環境を起動します。\
Windowsでは`pip`,`python3`の代わりに`pip`,`python`でないといけないかもしれないです。\
また、Fishを使っている場合は`siders-server/bin/activate`ではなく、`siders-server/bin/activate.fish`を読み込んでください。
```
source siders-server/bin/activate
```
#### パッケージのインストール
仮想環境に入った状態で、以下のコマンドでパッケージをインストールします。
```
pip3 install -r requirements.txt
```
主なパッケージは以下の2つです。
* Flask
* psycopg2

FlaskはWebアプリケーションフレームワークであり、今回はWebAPIを作成するために使います。\
psycopg2はPostgreSQLデータベースを接続・操作するためのパッケージです。

#### 仮想環境の修了
このコマンドで仮想環境を修了します。
```
deactivate
```

## 開発
プログラムはできればパスごとにファイル分けしてしてください。\
作成したAPIは`server/api/router.py`,`server/api/modules/__init__.py`でインポートしてください。\
パッケージを追加した場合は、以下のコマンドを実行して`requirements.txt`記入してください。
```
pip3 freeze > requirements.txt
```
クライアントでは`lib/domain/api_client.dart`にAPIを叩く関数を用意してあります。
