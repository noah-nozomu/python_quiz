# data_backend_advanced.py
quiz_list = [
    {
        "id": 201,
        "level": "応用",
        "category": "バックエンド",
        "question": "Pythonのリスト内包表記。 [x*2 for x in range(3)] を実行したときの結果は？",
        "choices": ["[0, 1, 2]", "[0, 2, 4]", "[2, 4, 6]", "エラーになる"],
        "answer": "[0, 2, 4]",
        "explanation": "range(3)は 0, 1, 2 を生成します。それぞれの要素(x)を2倍にして新しいリストを作るため [0, 2, 4] になります。"
    },
    {
        "id": 202,
        "level": "応用",
        "category": "バックエンド",
        "question": "Pythonのクラス内で、インスタンス自身を指すために慣例的に使われる第一引数の名前は？",
        "choices": ["this", "self", "cls", "me"],
        "answer": "self",
        "explanation": "クラスのメソッドを定義する際、第一引数には必ず self を指定し、インスタンス自身への参照を持たせます。"
    },
    {
        "id": 203,
        "level": "応用",
        "category": "バックエンド",
        "question": "Pythonの関数定義で「**kwargs」と書いた場合、渡されたキーワード引数は関数内でどのデータ型として扱われる？",
        "choices": ["リスト", "タプル", "辞書", "文字列"],
        "answer": "辞書",
        "explanation": "**kwargs はキーワード引数を辞書（ディクショナリ）として受け取ります。単一のアスタリスク（*args）はタプルになります。"
    },
    {
        "id": 204,
        "level": "応用",
        "category": "バックエンド",
        "question": "Pythonで名前のない短い関数を1行で定義するときに使うキーワードは？",
        "choices": ["lambda", "anonymous", "def", "inline"],
        "answer": "lambda",
        "explanation": "「lambda 引数: 返り値」のように書き、ちょっとした処理を関数として他の機能に渡したい時などに便利です（ラムダ式）。"
    },
    {
        "id": 205,
        "level": "応用",
        "category": "バックエンド",
        "question": "Streamlitで、データの読み込みなど重い処理の結果を保存して、2回目以降を高速化するデコレータは？",
        "choices": ["@st.memory", "@st.cache_data", "@st.save", "@st.fast"],
        "answer": "@st.cache_data",
        "explanation": "関数に @st.cache_data をつけると、同じ入力があった場合に処理をスキップして前回記憶した結果を瞬時に返してくれます。"
    },
    {
        "id": 206,
        "level": "応用",
        "category": "バックエンド",
        "question": "Streamlitで、サイドバーではなく「メイン画面の中」にタブを作って表示を切り替える関数は？",
        "choices": ["st.tabs()", "st.pages()", "st.sidebar()", "st.expander()"],
        "answer": "st.tabs()",
        "explanation": "tab1, tab2 = st.tabs(['タブ1', 'タブ2']) のように使い、限られた画面スペースを有効活用できます。"
    },
    {
        "id": 207,
        "level": "応用",
        "category": "バックエンド",
        "question": "Streamlitのボタンや入力部品で、値が変更された瞬間に特定の関数を呼び出すための引数は？",
        "choices": ["on_change (または on_click)", "callback", "run", "trigger"],
        "answer": "on_change (または on_click)",
        "explanation": "st.button('押す', on_click=関数名) のように書き、画面が再読み込みされる前に特定の処理を挟むことができます。"
    },
    {
        "id": 208,
        "level": "応用",
        "category": "バックエンド",
        "question": "Streamlitの画面上に表（データフレーム）を、ユーザーが並び替えやスクロールできる形で表示する関数は？",
        "choices": ["st.table()", "st.dataframe()", "st.grid()", "st.excel()"],
        "answer": "st.dataframe()",
        "explanation": "st.table() は静的な（動かせない）表ですが、st.dataframe() を使うとソートや拡大ができるリッチな表を表示できます。"
    },
    {
        "id": 209,
        "level": "応用",
        "category": "バックエンド",
        "question": "DjangoのORMで、価格(price)が「1000以上」のデータを抽出する正しい書き方は？",
        "choices": ["Item.objects.filter(price > 1000)", "Item.objects.filter(price__gte=1000)", "Item.objects.filter(price_gte=1000)", "Item.objects.get(price>=1000)"],
        "answer": "Item.objects.filter(price__gte=1000)",
        "explanation": "Djangoのデータベース操作では、フィールド名の後ろにアンダースコア2つ（__）を繋げて条件を指定します。gteは Greater Than or Equal（以上）の略です。"
    },
    {
        "id": 210,
        "level": "応用",
        "category": "バックエンド",
        "question": "DjangoのHTMLテンプレートで、POST送信するフォーム(form)内に必ず書くべきセキュリティ対策のタグは？",
        "choices": ["{% csrf_token %}", "{{ form.csrf }}", "<input type='secure'>", "{% post_protect %}"],
        "answer": "{% csrf_token %}",
        "explanation": "クロスサイトリクエストフォージェリ（CSRF）というサイバー攻撃を防ぐための暗号トークンを埋め込む必須タグです。"
    },
    {
        "id": 211,
        "level": "応用",
        "category": "バックエンド",
        "question": "Djangoのビュー(views.py)からテンプレート(HTML)へデータを渡す際、通常どのデータ型でまとめる？",
        "choices": ["リスト", "辞書", "文字列", "タプル"],
        "answer": "辞書",
        "explanation": "context = {'items': data} のように辞書型でまとめ、render関数の第3引数として渡すのが基本です。"
    },
    {
        "id": 212,
        "level": "応用",
        "category": "バックエンド",
        "question": "Djangoのurls.pyで、URLの一部を数字の変数（pkなど）としてビューに渡す正しい書き方は？",
        "choices": ["path('item/<pk>/')", "path('item/<int:pk>/')", "path('item/(pk)/')", "path('item/int:pk/')"],
        "answer": "path('item/<int:pk>/')",
        "explanation": "<型:変数名> のように書くことで、URLのその部分（例えば /item/5/ の 5）を整数としてビューで受け取れます。"
    },
    {
        "id": 213,
        "level": "応用",
        "category": "バックエンド",
        "question": "Djangoで、モデル(Model)の設計図から自動的にHTMLの入力フォーム(Form)を生成してくれる便利な機能は？",
        "choices": ["ModelForm", "AutoForm", "FormGenerator", "BaseForm"],
        "answer": "ModelForm",
        "explanation": "forms.py で class Meta: model = Item のように指定するだけで、モデルの項目に合わせたフォームの土台を作ってくれます。"
    },
    {
        "id": 214,
        "level": "応用",
        "category": "バックエンド",
        "question": "Pythonの例外処理(try-except)で、エラーが起きても起きなくても「最後に必ず実行したい処理」を書くブロックは？",
        "choices": ["finally", "else", "end", "always"],
        "answer": "finally",
        "explanation": "ファイルを閉じる処理や、データベースの接続を切る処理など、安全のために絶対に実行させたい後処理を finally に書きます。"
    },
    {
        "id": 215,
        "level": "応用",
        "category": "バックエンド",
        "question": "DjangoのORMで、データベースから条件に合うデータを「1件だけ」確実に取得するメソッドは？",
        "choices": ["filter()", "get()", "first()", "find()"],
        "answer": "get()",
        "explanation": "get() は条件に完全に一致するデータが1件の時だけ成功します。0件だったり複数件見つかったりするとエラーになるため、ID(pk)での検索などに使われます。"
    }
]