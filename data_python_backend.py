# data_python_backend.py

questions = {
    "初級": [
        {
            "question": "Pythonで文字や数値を画面に表示するための関数は？", 
            "choices": ["input()", "print()", "show()", "display()"], 
            "answer": "print()",
            "example": "print(\"Hello World\")"
        },
        {
            "question": "Pythonで変数に値を代入する正しい書き方は？", 
            "choices": ["x = 10", "x : 10", "x == 10", "int x = 10"], 
            "answer": "x = 10",
            "example": "score = 100\nprint(score)"
        },
        {
            "question": "Pythonでコードに「コメント（メモ）」を書く時に使う記号は？", 
            "choices": ["//", "/* */", "#", "--"], 
            "answer": "#",
            "example": "# ここはコメントです\nprint(\"ここは動きます\")"
        },
        {
            "question": "Pythonのデータ型で「整数」を表すものは？", 
            "choices": ["int", "str", "float", "bool"], 
            "answer": "int",
            "example": "age = 20  # これは int (整数) です"
        },
        {
            "question": "Pythonのデータ型で「文字列（テキスト）」を表すものは？", 
            "choices": ["int", "str", "float", "bool"], 
            "answer": "str",
            "example": "name = \"Taro\"  # これは str (文字列) です"
        },
        {
            "question": "リスト（配列）の一番最初の要素を取り出す正しいインデックス（番号）は？", 
            "choices": ["0", "1", "-1", "first"], 
            "answer": "0",
            "example": "fruits = [\"apple\", \"banana\"]\nprint(fruits[0])  # apple"
        },
        {
            "question": "辞書（ディクショナリ）から、キーを使って値を取り出す書き方は？", 
            "choices": ["data[\"key\"]", "data.key", "data(key)", "data->key"], 
            "answer": "data[\"key\"]",
            "example": "user = {\"name\": \"Jiro\"}\nprint(user[\"name\"])"
        },
        {
            "question": "条件分岐「もし〜なら」を書くための構文は？", 
            "choices": ["if 条件:", "when 条件:", "check 条件:", "case 条件:"], 
            "answer": "if 条件:",
            "example": "if score > 80:\n    print(\"合格\")"
        },
        {
            "question": "条件分岐で「それ以外なら」を書くための構文は？", 
            "choices": ["else:", "other:", "default:", "elif:"], 
            "answer": "else:",
            "example": "if score > 80:\n    print(\"合格\")\nelse:\n    print(\"不合格\")"
        },
        {
            "question": "「関数」を定義する時に使うキーワードは？", 
            "choices": ["func", "def", "function", "define"], 
            "answer": "def",
            "example": "def hello():\n    print(\"こんにちは\")"
        },
        {
            "question": "関数から値を「返す」時に使うキーワードは？", 
            "choices": ["return", "back", "send", "result"], 
            "answer": "return",
            "example": "def add(a, b):\n    return a + b"
        },
        {
            "question": "リストの要素の数（長さ）を調べる関数は？", 
            "choices": ["count()", "size()", "len()", "length()"], 
            "answer": "len()",
            "example": "items = [1, 2, 3]\nprint(len(items))  # 3"
        },
        {
            "question": "外部のモジュールやライブラリを読み込むためのキーワードは？", 
            "choices": ["include", "require", "using", "import"], 
            "answer": "import",
            "example": "import math\nprint(math.pi)"
        },
        {
            "question": "文字列の中に変数を埋め込む便利な書き方（f-strings）は？", 
            "choices": ["f\"Hello {name}\"", "f\"Hello (name)\"", "\"Hello {name}\".format", "\"Hello \" + name"], 
            "answer": "f\"Hello {name}\"",
            "example": "name = \"Ken\"\nprint(f\"Hello {name}\")"
        },
        {
            "question": "「等しい」かどうかを比較する演算子は？", 
            "choices": ["=", "==", "===", "equals"], 
            "answer": "==",
            "example": "if x == 10:\n    print(\"xは10です\")"
        }
    ],
    "中級": [
        {
            "question": "Pythonの軽量なWebフレームワークで、「マイクロフレームワーク」と呼ばれるものは？", 
            "choices": ["Django", "Flask", "Pyramid", "Bottle"], 
            "answer": "Flask",
            "example": "from flask import Flask\napp = Flask(__name__)"
        },
        {
            "question": "PythonのフルスタックWebフレームワークで、管理画面や認証機能が標準でついているものは？", 
            "choices": ["Flask", "Django", "FastAPI", "Tornado"], 
            "answer": "Django",
            "example": "# Djangoは機能が豊富で、大規模開発に向いています"
        },
        {
            "question": "Flaskで、URLと関数を紐付ける（ルーティングする）ためのデコレータは？", 
            "choices": ["@app.route()", "@app.url()", "@app.path()", "@app.link()"], 
            "answer": "@app.route()",
            "example": "@app.route(\"/\")\ndef hello():\n    return \"Hello!\""
        },
        {
            "question": "HTTPメソッドの中で、サーバーからデータを「取得」する時に使われるのは？", 
            "choices": ["POST", "GET", "PUT", "DELETE"], 
            "answer": "GET",
            "example": "# ブラウザでURLを入力してアクセスするのはGETリクエストです"
        },
        {
            "question": "HTTPメソッドの中で、サーバーにデータを「送信・登録」する時に使われるのは？", 
            "choices": ["GET", "POST", "HEAD", "OPTIONS"], 
            "answer": "POST",
            "example": "# フォームの送信などはPOSTリクエストが使われます"
        },
        {
            "question": "HTTPステータスコードで、「リクエスト成功（OK）」を表す数字は？", 
            "choices": ["200", "404", "500", "301"], 
            "answer": "200",
            "example": "# 正常にページが表示された時は200が返っています"
        },
        {
            "question": "HTTPステータスコードで、「ページが見つからない（Not Found）」を表す数字は？", 
            "choices": ["200", "400", "404", "503"], 
            "answer": "404",
            "example": "# 存在しないURLにアクセスすると404エラーになります"
        },
        {
            "question": "PythonでJSONデータを扱うために標準で用意されているモジュールは？", 
            "choices": ["json", "simplejson", "jsonify", "parse"], 
            "answer": "json",
            "example": "import json\ndata = json.loads('{\"key\": \"value\"}')"
        },
        {
            "question": "プロジェクトごとにライブラリを独立して管理するための「仮想環境」を作るコマンドは？", 
            "choices": ["python -m venv .venv", "pip install venv", "python create env", "virtualenv start"], 
            "answer": "python -m venv .venv",
            "example": "# 実行すると .venv フォルダが作成されます"
        },
        {
            "question": "Pythonのパッケージ（ライブラリ）をインストールするためのコマンドは？", 
            "choices": ["python install", "pip install", "npm install", "gem install"], 
            "answer": "pip install",
            "example": "pip install requests"
        },
        {
            "question": "インストールされているパッケージの一覧をファイル（requirements.txt）に書き出すコマンドは？", 
            "choices": ["pip freeze > requirements.txt", "pip list > requirements.txt", "pip save", "pip export"], 
            "answer": "pip freeze > requirements.txt",
            "example": "# これで他の人も同じ環境を再現できます"
        },
        {
            "question": "データベースのテーブルを、Pythonのクラス（オブジェクト）として操作する仕組みを何と呼ぶ？", 
            "choices": ["ORM (Object-Relational Mapping)", "SQL", "DB-API", "QueryBuilder"], 
            "answer": "ORM (Object-Relational Mapping)",
            "example": "# SQLを書かずに user.save() のように直感的に操作できます"
        },
        {
            "question": "SQLで、テーブルからデータを「取得」する命令は？", 
            "choices": ["SELECT", "INSERT", "UPDATE", "DELETE"], 
            "answer": "SELECT",
            "example": "SELECT * FROM users;"
        },
        {
            "question": "SQLで、データを取得する際の「条件」を指定する句は？", 
            "choices": ["WHERE", "IF", "WHEN", "FILTER"], 
            "answer": "WHERE",
            "example": "SELECT * FROM users WHERE id = 1;"
        },
        {
            "question": "Pythonスクリプトが直接実行された時だけ処理を行うための、有名な書き出しは？", 
            "choices": ["if __name__ == \"__main__\":", "if __run__ == \"__main__\":", "if main():", "def main():"], 
            "answer": "if __name__ == \"__main__\":",
            "example": "if __name__ == \"__main__\":\n    app.run()"
        },
        {
            "question": "Djangoなどのテンプレートエンジンで、変数を埋め込む時の記号は？", 
            "choices": ["{{ variable }}", "{% variable %}", "[[ variable ]]", "< variable >"], 
            "answer": "{{ variable }}",
            "example": "<p>こんにちは、{{ user_name }}さん</p>"
        },
        {
            "question": "Djangoで管理者ユーザー（スーパーユーザー）を作成するコマンドは？", 
            "choices": ["python manage.py createsuperuser", "python manage.py admin", "django-admin create", "python manage.py user add"], 
            "answer": "python manage.py createsuperuser",
            "example": "# 実行するとメールアドレスやパスワードの設定が始まります"
        },
        {
            "question": "Flaskで、HTMLファイルを置いておくデフォルトのフォルダ名は？", 
            "choices": ["templates", "views", "html", "pages"], 
            "answer": "templates",
            "example": "# render_template('index.html') は templates/index.html を探します"
        },
        {
            "question": "プログラム同士が連携するための窓口や規約のことを何と呼ぶ？", 
            "choices": ["API (Application Programming Interface)", "GUI", "CUI", "IDE"], 
            "answer": "API (Application Programming Interface)",
            "example": "# 天気予報APIからデータを取得する、など"
        },
        {
            "question": "Web APIの設計スタイルのひとつで、URLがリソースを表し、HTTPメソッドで操作を表すものは？", 
            "choices": ["REST (Representational State Transfer)", "SOAP", "GraphQL", "RPC"], 
            "answer": "REST (Representational State Transfer)",
            "example": "# GET /users/1 (取得), DELETE /users/1 (削除) のような形式"
        },
        {
            "question": "データ操作の基本となる4つの機能（作成、読み出し、更新、削除）の頭文字をとった言葉は？", 
            "choices": ["CRUD", "REST", "ACID", "JSON"], 
            "answer": "CRUD",
            "example": "# Create, Read, Update, Delete"
        },
        {
            "question": "Flaskなどで、URLの一部を変数として受け取る（パスパラメータ）書き方は？", 
            "choices": ["<int:id>", "{id}", "[id]", "(id)"], 
            "answer": "<int:id>",
            "example": "@app.route('/users/<int:user_id>')\n# /users/123 にアクセスすると user_id=123 になる"
        },
        {
            "question": "URLの末尾につく「?key=value」のようなパラメータを何と呼ぶ？", 
            "choices": ["クエリパラメータ", "パスパラメータ", "ボディパラメータ", "ヘッダー"], 
            "answer": "クエリパラメータ",
            "example": "# https://example.com/search?q=python"
        },
        {
            "question": "HTTPステータスコードで、「サーバー内部エラー」を表す数字は？", 
            "choices": ["500", "503", "400", "200"], 
            "answer": "500",
            "example": "# プログラムがバグでクラッシュした場合などに返されます"
        },
        {
            "question": "APIキーなどの機密情報をコードに直書きせず、OS側で管理する変数を何と呼ぶ？", 
            "choices": ["環境変数", "グローバル変数", "ローカル変数", "システム変数"], 
            "answer": "環境変数",
            "example": "# GitHubなどにパスワードを公開しないための必須知識です"
        },
        {
            "question": "Pythonで環境変数を取得するために使う標準モジュールは？", 
            "choices": ["os", "sys", "env", "path"], 
            "answer": "os",
            "example": "import os\nsecret = os.environ.get('API_KEY')"
        },
        {
            "question": "Pythonから外部のWebサイトやAPIにHTTPリクエストを送るための、非常に有名な外部ライブラリは？", 
            "choices": ["requests", "urllib", "http", "fetch"], 
            "answer": "requests",
            "example": "import requests\nres = requests.get('https://google.com')"
        },
        {
            "question": "Pythonの辞書型（dict）をJSON形式の文字列に変換する関数は？", 
            "choices": ["json.dumps()", "json.loads()", "json.dump()", "json.str()"], 
            "answer": "json.dumps()",
            "example": "json_str = json.dumps({'id': 1})"
        },
        {
            "question": "JSON形式の文字列をPythonの辞書型（dict）に変換する関数は？", 
            "choices": ["json.loads()", "json.dumps()", "json.load()", "json.parse()"], 
            "answer": "json.loads()",
            "example": "data = json.loads('{\"id\": 1}')"
        },
        {
            "question": "データベースの定義（スキーマ）の変更を管理し、コードに合わせてDB構造を更新する仕組みは？", 
            "choices": ["マイグレーション (Migration)", "コミット (Commit)", "プッシュ (Push)", "デプロイ (Deploy)"], 
            "answer": "マイグレーション (Migration)",
            "example": "# Djangoなどでは必須の作業です"
        }
    ],
    "上級": [
        {
            "question": "Pythonで「非同期処理（並行処理）」を行うための構文で、関数の前につけるキーワードは？", 
            "choices": ["async def", "await def", "sync def", "parallel def"], 
            "answer": "async def",
            "example": "async def main():\n    print('Hello')"
        },
        {
            "question": "非同期関数（コルーチン）の実行完了を待つために使うキーワードは？", 
            "choices": ["await", "wait", "async", "yield"], 
            "answer": "await",
            "example": "result = await fetch_data()"
        },
        {
            "question": "PythonのWebアプリとWebサーバーをつなぐための、従来の標準的なインターフェース仕様は？", 
            "choices": ["WSGI (Web Server Gateway Interface)", "ASGI", "CGI", "API"], 
            "answer": "WSGI (Web Server Gateway Interface)",
            "example": "# FlaskやDjango（同期版）はWSGIアプリケーションです"
        },
        {
            "question": "WSGIの後継で、非同期処理（WebSocketなど）に対応したインターフェース仕様は？", 
            "choices": ["ASGI (Asynchronous Server Gateway Interface)", "WSGI 2.0", "AsyncWSGI", "AIOHTTP"], 
            "answer": "ASGI (Asynchronous Server Gateway Interface)",
            "example": "# FastAPIやDjango（非同期版）はASGIアプリケーションです"
        },
        {
            "question": "アプリケーションと実行環境を「コンテナ」としてパッケージ化し、どこでも同じように動かせる技術は？", 
            "choices": ["Docker", "Kubernetes", "VirtualBox", "Vagrant"], 
            "answer": "Docker",
            "example": "# docker build -t myapp ."
        },
        {
            "question": "Webアプリの脆弱性のひとつで、フォーム入力などに悪意あるSQLを混ぜてデータを盗む攻撃は？", 
            "choices": ["SQLインジェクション", "XSS (クロスサイトスクリプティング)", "CSRF", "ブルートフォース"], 
            "answer": "SQLインジェクション",
            "example": "# 対策：プレースホルダーやORMを使って値をバインドする"
        },
        {
            "question": "Webアプリの脆弱性のひとつで、ユーザーが意図しない操作（送金や投稿など）を勝手にさせられる攻撃は？", 
            "choices": ["CSRF (クロスサイトリクエストフォージェリ)", "XSS", "DoS攻撃", "フィッシング"], 
            "answer": "CSRF (クロスサイトリクエストフォージェリ)",
            "example": "# 対策：CSRFトークンをフォームに埋め込む"
        },
        {
            "question": "パスワードをデータベースに保存する際、平文ではなくハッシュ化（暗号化）するために使われるPythonライブラリは？", 
            "choices": ["bcrypt / passlib", "hashlib", "encrypt", "secrets"], 
            "answer": "bcrypt / passlib",
            "example": "# 復号できない一方向のハッシュ関数を使います"
        },
        {
            "question": "データベースへのクエリ回数が多くなりすぎてパフォーマンスが低下する、ORMでよくある問題は？", 
            "choices": ["N+1問題", "デッドロック", "スロークエリ", "オーバーヘッド"], 
            "answer": "N+1問題",
            "example": "# 1回の検索で済むところを、データ数(N)+1回クエリを投げてしまう現象"
        },
        {
            "question": "関数の引数や戻り値の型を明記して、エディタの補完や静的解析を助ける機能は？", 
            "choices": ["型ヒント (Type Hinting)", "型キャスト", "型チェック", "ダックタイピング"], 
            "answer": "型ヒント (Type Hinting)",
            "example": "def add(x: int, y: int) -> int:\n    return x + y"
        },
        {
            "question": "ファイルを開いた後に自動で閉じてくれる `with open(...)` のような構文を支える仕組みは？", 
            "choices": ["コンテキストマネージャ", "デコレータ", "ジェネレータ", "イテレータ"], 
            "answer": "コンテキストマネージャ",
            "example": "with open('file.txt') as f:\n    print(f.read()) # ブロックを抜けると自動でcloseされる"
        },
        {
            "question": "関数を修飾して、元のコードを変えずに機能（ログ出力や認証など）を追加する仕組みは？", 
            "choices": ["デコレータ", "アダプタ", "ラッパー", "プロキシ"], 
            "answer": "デコレータ",
            "example": "@login_required\ndef my_page(): ...\n# 関数定義の上に@で書くやつ"
        },
        {
            "question": "大量のデータを一度にリストにせず、1つずつ取り出してメモリを節約する関数（`yield`を使うもの）は？", 
            "choices": ["ジェネレータ", "リスト内包表記", "ラムダ式", "コンストラクタ"], 
            "answer": "ジェネレータ",
            "example": "def count_up():\n    yield 1\n    yield 2"
        },
        {
            "question": "Pythonで人気の、シンプルかつ強力なテストフレームワークは？", 
            "choices": ["pytest", "unittest", "nose", "doctest"], 
            "answer": "pytest",
            "example": "def test_add():\n    assert add(1, 1) == 2"
        },
        {
            "question": "異なるドメイン（オリジン）からのAJAX通信を許可するための仕組みは？", 
            "choices": ["CORS (Cross-Origin Resource Sharing)", "CSRF", "CSP", "SSL"], 
            "answer": "CORS (Cross-Origin Resource Sharing)",
            "example": "# APIサーバーとフロントエンドのドメインが違う場合に設定が必要"
        },
        {
            "question": "データベースの検索を高速化するために、特定の列に作成するデータ構造は？", 
            "choices": ["インデックス (Index)", "ビュー (View)", "トリガー (Trigger)", "カーソル (Cursor)"], 
            "answer": "インデックス (Index)",
            "example": "# 本の「索引」と同じで、データが増えても検索が速くなる"
        },
        {
            "question": "一連のデータベース処理において、「全て成功するか、全て失敗するか」を保証する仕組みは？", 
            "choices": ["トランザクション", "マイグレーション", "レプリケーション", "バックアップ"], 
            "answer": "トランザクション",
            "example": "# 送金処理などで、片方だけ減って片方が増えない…という事態を防ぐ"
        },
        {
            "question": "認証に使われる、JSON形式のデータを署名付きでやり取りするトークン規格は？", 
            "choices": ["JWT (JSON Web Token)", "Cookie", "Session ID", "OAuth"], 
            "answer": "JWT (JSON Web Token)",
            "example": "# ログイン状態をサーバーのメモリに持たずに管理できる"
        },
        {
            "question": "GoogleやX（Twitter）などのアカウントを使って、自分のアプリにログインさせるための認可プロトコルは？", 
            "choices": ["OAuth 2.0", "OpenID Connect", "SAML", "LDAP"], 
            "answer": "OAuth 2.0",
            "example": "# 「Googleでログイン」機能の実装に使われる"
        },
        {
            "question": "PythonのWSGIアプリケーションを本番環境で動かすための、有名なWSGIサーバーは？", 
            "choices": ["Gunicorn", "Apache", "Nginx", "IIS"], 
            "answer": "Gunicorn",
            "example": "# gunicorn app:app で起動し、Nginxの後ろで動かすのが一般的"
        },
        {
            "question": "FastAPIなどのASGIアプリケーションを動かすための、高速なASGIサーバーは？", 
            "choices": ["Uvicorn", "Gunicorn", "Waitress", "Hypercorn"], 
            "answer": "Uvicorn",
            "example": "# uvicorn main:app --reload"
        },
        {
            "question": "コードの変更を検知して、自動でテストやデプロイを行う仕組みは？", 
            "choices": ["CI/CD (継続的インテグレーション/デリバリー)", "DevOps", "Agile", "Scrum"], 
            "answer": "CI/CD (継続的インテグレーション/デリバリー)",
            "example": "# GitHub Actionsなどで自動化する"
        },
        {
            "question": "Pythonコードの型ヒントを元に、実行前に型エラーをチェックしてくれる静的解析ツールは？", 
            "choices": ["mypy", "pylint", "flake8", "black"], 
            "answer": "mypy",
            "example": "# mypy script.py で型の矛盾を検出できる"
        },
        {
            "question": "データを格納するためのクラスを簡単に作れる、Python 3.7で導入されたデコレータは？", 
            "choices": ["@dataclass", "@struct", "@record", "@model"], 
            "answer": "@dataclass",
            "example": "@dataclass\nclass User:\n    name: str\n    age: int"
        },
        {
            "question": "クラスのインスタンスが常に1つしか存在しないことを保証するデザインパターンは？", 
            "choices": ["シングルトン (Singleton)", "ファクトリー", "オブザーバー", "プロキシ"], 
            "answer": "シングルトン (Singleton)",
            "example": "# データベース接続や設定管理などで使われる"
        },
        {
            "question": "PythonでCPUの計算力をフルに使うために、スレッドではなくプロセスを並列化するライブラリは？", 
            "choices": ["multiprocessing", "threading", "asyncio", "concurrent"], 
            "answer": "multiprocessing",
            "example": "# PythonにはGIL（グローバルインタプリタロック）があるため、計算処理にはプロセス並列が有効"
        },
        {
            "question": "オブジェクトが必要とする依存関係（DB接続など）を、外部から注入する設計パターンは？", 
            "choices": ["Dependency Injection (DI)", "Inversion of Control", "Factory Pattern", "Singleton"], 
            "answer": "Dependency Injection (DI)",
            "example": "# テスト時にモック（偽物）に差し替えるのが容易になる"
        },
        {
            "question": "巨大な一つのアプリ（モノリス）ではなく、小さなサービスを組み合わせてシステムを作るアーキテクチャは？", 
            "choices": ["マイクロサービス", "サーバーレス", "SOA", "分散システム"], 
            "answer": "マイクロサービス",
            "example": "# 各サービスを独立して開発・デプロイできる"
        },
        {
            "question": "リスト内包表記 `[x for x in range(10)]` と似ているが、`()` で囲むと作られるものは？", 
            "choices": ["ジェネレータ式", "タプル内包表記", "セット内包表記", "辞書内包表記"], 
            "answer": "ジェネレータ式",
            "example": "g = (x*x for x in range(10)) # メモリ効率が良い"
        },
        {
            "question": "クラスの中で `__call__` メソッドを定義すると、そのインスタンスはどうなる？", 
            "choices": ["関数のように `obj()` で呼び出せるようになる", "print時に呼ばれる", "初期化時に呼ばれる", "エラーになる"], 
            "answer": "関数のように `obj()` で呼び出せるようになる",
            "example": "class Adder:\n    def __call__(self, x): return x + 1\nadd = Adder()\nprint(add(10))"
        }
    ]
}