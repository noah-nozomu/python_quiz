quiz_list = [
    # --- Python 基礎構文 ---
    {
        "id": 1,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonで文字列の中に変数の値を直接埋め込む「f文字列」の正しい書き方はどれ？",
        "choices": ["f'{name}'", "f(name)", "${name}", "&{name}"],
        "answer": "f'{name}'",
        "explanation": "文字列の前に「f」を置き、{}の中に変数名を入れることで、直感的に文字列に変数を組み込めます。"
    },
    {
        "id": 2,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonのリスト（配列）の末尾に新しい要素を追加するメソッドは？",
        "choices": ["add()", "insert()", "append()", "push()"],
        "answer": "append()",
        "explanation": "リスト名.append(追加したい値) と書くことで、リストの一番最後にデータが追加されます。"
    },
    {
        "id": 3,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonで関数を新しく定義（作成）するときに使うキーワードは？",
        "choices": ["function", "def", "create", "func"],
        "answer": "def",
        "explanation": "「def 関数名():」の形で関数を定義します。define（定義する）の略です。"
    },
    {
        "id": 4,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonで「もし〜なら」という条件分岐を作る際、2つ目以降の条件を指定するキーワードは？",
        "choices": ["else if", "elseif", "elif", "case"],
        "answer": "elif",
        "explanation": "Pythonでは「else if」を省略して「elif」と書きます。if → elif → else の順に使います。"
    },
    {
        "id": 5,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonで辞書（辞書型データ）から特定の値を取り出すための正しい書き方は？\ndata = {'name': 'Taro', 'age': 35}",
        "choices": ["data[0]", "data.name", "data['name']", "data(name)"],
        "answer": "data['name']",
        "explanation": "辞書型はキー（見出し）を使って値を取り出します。リストのように数字（インデックス）は使いません。"
    },
    {
        "id": 6,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonでプログラムの実行中にエラーが起きても止まらないようにする「例外処理」の構文は？",
        "choices": ["try...except", "do...catch", "attempt...fail", "on...error"],
        "answer": "try...except",
        "explanation": "tryブロックにエラーが起きそうな処理を書き、エラー発生時はexceptブロックの処理が実行されます。"
    },
    {
        "id": 7,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonの真偽値（正しい/正しくない）を表す正しい書き方はどれ？",
        "choices": ["true / false", "TRUE / FALSE", "True / False", "T / F"],
        "answer": "True / False",
        "explanation": "Pythonの真偽値は先頭だけ大文字の「True」「False」です。小文字や全大文字だとエラーになります。"
    },

    # --- Streamlit 基礎 ---
    {
        "id": 8,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Streamlitで画面にテキストを表示するための最も基本的な関数は？",
        "choices": ["st.print()", "st.show()", "st.display()", "st.write()"],
        "answer": "st.write()",
        "explanation": "st.write()はテキストだけでなく、データフレームやグラフなど様々なものを自動で判別して表示してくれる万能関数です。"
    },
    {
        "id": 9,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Streamlitでボタンを配置し、押されたかどうかを判定する正しい書き方は？",
        "choices": ["if st.button('押す'):", "on_click st.button():", "st.click('押す')", "st.add_button()"],
        "answer": "if st.button('押す'):",
        "explanation": "st.button()は押された瞬間にTrueを返すため、if文と組み合わせて処理を書くのが基本です。"
    },
    {
        "id": 10,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Streamlitで画面が更新（リロード）されてもデータを保持しておくための機能は？",
        "choices": ["st.memory", "st.cache", "st.session_state", "st.save_data"],
        "answer": "st.session_state",
        "explanation": "ボタンを押すたびに画面が再読み込みされるStreamlitにおいて、状態（スコアや入力内容など）を保持する必須機能です。"
    },
    {
        "id": 11,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Streamlitでユーザーに短いテキスト（名前など）を入力させるコンポーネントは？",
        "choices": ["st.input()", "st.text_input()", "st.form()", "st.entry()"],
        "answer": "st.text_input()",
        "explanation": "st.text_input('名前を入力') とすることで、1行のテキスト入力欄を作成できます。"
    },
    {
        "id": 12,
        "level": "基礎",
        "category": "バックエンド",
        "question": "作成したStreamlitアプリ（app.py）をローカル環境で起動する正しいコマンドは？",
        "choices": ["python app.py", "run app.py", "streamlit start app.py", "streamlit run app.py"],
        "answer": "streamlit run app.py",
        "explanation": "ターミナルで「streamlit run ファイル名」と入力することで、ブラウザが立ち上がりアプリが起動します。"
    },

    # --- Django 基礎 ---
    {
        "id": 13,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Djangoの開発用サーバーを起動するためのコマンドは？",
        "choices": ["python manage.py runserver", "django start server", "python manage.py start", "django-admin run"],
        "answer": "python manage.py runserver",
        "explanation": "このコマンドを実行すると、通常「http://127.0.0.1:8000/」で開発用サーバーが立ち上がります。"
    },
    {
        "id": 14,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Djangoでデータベースの設計図（テーブル構造）を書くファイルはどれ？",
        "choices": ["views.py", "models.py", "urls.py", "admin.py"],
        "answer": "models.py",
        "explanation": "models.pyにクラスを定義することで、それがデータベースのテーブルとして作成されます。"
    },
    {
        "id": 15,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Djangoのmodels.pyを変更した後、それをデータベースに反映させるために最初に行うコマンドは？",
        "choices": ["python manage.py migrate", "python manage.py makemigrations", "python manage.py update", "python manage.py dbsync"],
        "answer": "python manage.py makemigrations",
        "explanation": "まずmakemigrationsで「変更の設計図（マイグレーションファイル）」を作り、そのあとにmigrateで実際のDBに適用します。"
    },
    {
        "id": 16,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Djangoで「URL（アドレス）と、実行する処理（ビュー）」を結びつける設定を書くファイルは？",
        "choices": ["routes.py", "paths.py", "views.py", "urls.py"],
        "answer": "urls.py",
        "explanation": "urls.pyの中にurlpatternsというリストを作り、どのURLにアクセスされたらどの処理を呼ぶかを定義します。"
    },
    {
        "id": 17,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Djangoの管理画面（Adminサイト）にログインするための特別なユーザーを作成するコマンドは？",
        "choices": ["python manage.py newadmin", "python manage.py createsuperuser", "python manage.py adduser", "django-admin create"],
        "answer": "python manage.py createsuperuser",
        "explanation": "このコマンドを実行し、ユーザー名、メールアドレス、パスワードを設定することで、/adminのURLから管理画面に入れます。"
    },
    {
        "id": 18,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Djangoでデータベースからすべてのデータを取得する正しい書き方は？（モデル名がOrderの場合）",
        "choices": ["Order.objects.all()", "Order.get_all()", "Order.all()", "Order.fetch_all()"],
        "answer": "Order.objects.all()",
        "explanation": "DjangoのORM（データベース操作機能）では、「モデル名.objects.メソッド」の形でデータを操作します。"
    },
    {
        "id": 19,
        "level": "基礎",
        "category": "バックエンド",
        "question": "Pythonで他のファイルやライブラリの機能を使いたい時に先頭に書くキーワードは？",
        "choices": ["include", "require", "import", "using"],
        "answer": "import",
        "explanation": "「import モジュール名」や「from モジュール名 import 関数名」の形で、外部の便利な機能を読み込みます。"
    },
]    